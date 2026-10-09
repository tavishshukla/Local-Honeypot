# Local Honeypot

A safe localhost-only HTTP honeypot for learning defensive monitoring, logging, and basic incident investigation.

The application records requests made to its decoy endpoints and stores the events in a JSON Lines log.

> **Important:** This honeypot intentionally binds to `127.0.0.1`. It is designed for your own computer and local testing, not for exposing an intentionally vulnerable service to the internet.

## Features

- Local-only HTTP server
- Decoy endpoints
- Request metadata logging
- JSONL event log
- Simple event viewer endpoint
- GET/POST/PUT/DELETE/PATCH request logging
- No password collection
- No file uploads
- No command execution
- No intentionally vulnerable application logic

## Requirements

- Windows, Linux, or macOS
- Python **3.11 or newer**
- Git
- A web browser

## 1. Install Python

Download Python:

https://www.python.org/downloads/

On Windows, enable:

**Add Python to PATH**

Verify:

```bash
python --version
```

## 2. Install Git

Download:

https://git-scm.com/downloads

Verify:

```bash
git --version
```

## 3. Clone the repository

```bash
git clone https://github.com/tavishshukla/Local-Honeypot.git
cd Local-Honeypot
```

## 4. Create a virtual environment

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

## 5. Install dependencies

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install requirements:

```bash
python -m pip install -r requirements.txt
```

You normally do not need to download pip separately because Python includes it.

## 6. Start the honeypot

Run:

```bash
python main.py
```

The server listens only on:

```
http://127.0.0.1:8080
```

Open that address in your browser.

## 7. Generate a test event

Visit:

```
http://127.0.0.1:8080/
```

The endpoint intentionally responds with:

```
404 Not Found
```

That request is nevertheless recorded as a honeypot event.

You can also visit:

```
http://127.0.0.1:8080/admin
```

It also returns 404 and records the request.

## 8. View logged events

Open:

```
http://127.0.0.1:8080/events
```

The endpoint returns the most recent logged events as JSON.

## 9. Understand the event log

Events are stored in:

```
honeypot_events.jsonl
```

Each line represents one request.

The stored metadata includes:

- Timestamp
- HTTP method
- Requested path
- Local client address
- User-Agent

The project deliberately does not collect passwords or other credentials.

## 10. Run tests

```bash
python -m pytest
```

## 11. Stop the honeypot

Return to the terminal and press:

```
Ctrl+C
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

## Troubleshooting

### Python is not recognized

Install Python again and enable **Add Python to PATH**, then open a new terminal.

### Flask is missing

Run:

```bash
python -m pip install -r requirements.txt
```

### Port 8080 is already in use

Another local application may already be using port 8080. Stop that authorized application before starting the honeypot.

## Security model

This is a deliberately limited educational honeypot. It is bound to localhost and does not provide command execution, authentication bypasses, file uploads, password collection, or an intentionally vulnerable service.

Do not modify it to expose an unsafe service to the public internet unless you fully understand the security implications and have an appropriately isolated, authorized lab environment.
