from __future__ import annotations

import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from flask import Flask, jsonify, request

app = Flask(__name__)
LOG = Path("honeypot_events.jsonl")


def record() -> dict:
    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "method": request.method,
        "path": request.path,
        "client": request.remote_addr,
        "user_agent": request.headers.get("User-Agent", ""),
    }
    with LOG.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event) + "\n")
    return event


def read_events(limit: int = 100) -> list[dict]:
    if not LOG.exists():
        return []
    lines = LOG.read_text(encoding="utf-8").splitlines()[-limit:]
    return [json.loads(line) for line in lines]


@app.route("/", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@app.route("/admin", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def decoy():
    record()
    return "Not Found", 404


@app.get("/events")
def events():
    try:
        limit = min(max(int(request.args.get("limit", 100)), 1), 500)
    except ValueError:
        return jsonify({"error": "limit must be an integer"}), 400
    return jsonify(read_events(limit))


@app.get("/api/summary")
def summary():
    rows = read_events(500)
    methods = Counter(row["method"] for row in rows)
    paths = Counter(row["path"] for row in rows)
    clients = Counter(row["client"] for row in rows)
    agents = Counter(row["user_agent"] or "unknown" for row in rows)
    return jsonify({
        "events": len(rows),
        "methods": dict(methods),
        "top_paths": dict(paths.most_common(10)),
        "top_clients": dict(clients.most_common(10)),
        "top_user_agents": dict(agents.most_common(10)),
        "log_file": str(LOG),
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=False)
