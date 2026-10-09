# Local Honeypot

A safe localhost-only HTTP honeypot for learning defensive monitoring.

## Features
- Binds only to 127.0.0.1
- Records request metadata and paths
- Fake endpoints return 404
- JSONL event log
- Event viewer
- No passwords, uploads, command execution, or intentionally vulnerable service

## Run
```bash
pip install -r requirements.txt
python main.py
```
Open http://127.0.0.1:8080
