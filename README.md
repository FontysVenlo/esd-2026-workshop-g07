# Temporal - workflow orchestration technology - ESD 2026

## Fibonacci Demo

Needs Python 3.11+ and the Temporal CLI.

```bash
# setup (once)
cd temporal-fibonacci-demo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# terminal 1: Temporal server, Web UI at http://localhost:8233
temporal server start-dev

# terminal 2: worker (Ctrl+C to stop it, run again to restart)
python worker.py

# terminal 3: start the workflow
python starter.py
```

Terminals 2 and 3 run inside `temporal-fibonacci-demo` with `source .venv/bin/activate`.
