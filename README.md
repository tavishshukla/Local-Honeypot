# Local Honeypot

A safe localhost-only HTTP honeypot for learning defensive monitoring, logging, and incident investigation.

> The server intentionally binds to `127.0.0.1`. It is designed for your own computer and local testing.

## Features

- Local-only HTTP server
- Decoy endpoints
- Request metadata logging
- JSONL event log
- Event viewer API
- Event summary API
- Request method/path statistics
- No password collection
- No file uploads
- No command execution
- No intentionally vulnerable service

## Requirements

- Windows, Linux, or macOS
- Python **3.11 or newer**
- Git
- Web browser

## Setup

Install Python from https://www.python.org/downloads/ and Git from https://git-scm.com/downloads/.

Verify:

```bash
python --version
git --version
```

Clone:

```bash
git clone https://github.com/tavishshukla/Local-Honeypot.git
cd Local-Honeypot
```

Create a virtual environment.

### Windows

```bat
python -m venv .venv
.venv\\Scripts\\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run

```bash
python main.py
```

Open:

```
http://127.0.0.1:8080
```

The decoy endpoints return `404 Not Found` but record the request.

Try:

```
http://127.0.0.1:8080/
http://127.0.0.1:8080/admin
```

## View events

Open:

```
http://127.0.0.1:8080/events
```

You can request a specific number of recent events:

```
http://127.0.0.1:8080/events?limit=20
```

The limit is capped at 500.

## View summary

Open:

```
http://127.0.0.1:8080/api/summary
```

This reports recent event count, HTTP method counts, and the most common paths.

## Event log

Events are stored in:

```
honeypot_events.jsonl
```

Each event contains a timestamp, method, path, local client address, and User-Agent.

## Tests

```bash
python -m pytest
```

## Project structure

```
Local-Honeypot/
├── main.py
├── requirements.txt
├── README.md
└── tests/
    └── test_honeypot.py
```

## Security model

The honeypot is deliberately limited and local-only. It does not collect passwords, execute commands, accept uploads, bypass authentication, or expose an intentionally vulnerable service.

## Quick investigation workflow

After generating local test requests, inspect `/events` for recent events and `/api/summary` for method and path statistics. Both endpoints are local-only.

## Investigation metadata

The summary endpoint now includes the most common client addresses and User-Agent values in addition to methods and paths. This helps you spot repeated local test behavior without collecting credentials or request bodies.

## Unmatched routes

Requests to unknown local routes are now logged through the 404 handler, making the honeypot useful for observing unexpected paths as well as its explicit decoy endpoints.
