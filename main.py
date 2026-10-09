from __future__ import annotations
import json
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
        "user_agent": request.headers.get("User-Agent",""),
    }
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")
    return event

@app.route("/", methods=["GET","POST","PUT","DELETE","PATCH"])
@app.route("/admin", methods=["GET","POST","PUT","DELETE","PATCH"])
def decoy():
    record()
    return "Not Found", 404

@app.get("/events")
def events():
    if not LOG.exists(): return jsonify([])
    return jsonify([json.loads(x) for x in LOG.read_text().splitlines()[-100:]])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=False)
