# ngara-claude

A playground repository for experimenting with Claude Code features.

## What's inside

| Path | Contents |
|---|---|
| `python/` | `calculator.py`, `data_processor.py`, and pytest tests |
| `javascript/` | `utils.js` (helpers) and `api_client.js` (HTTP client) |
| `sql/` | Postgres schema + example analytical queries |
| `data/` | Sample datasets — `users.json`, `sales.csv`, `config.json` |
| `scripts/` | `setup.sh` (bootstrap) and `cleanup.sh` (remove artifacts) |
| `config/` | `.env.example` and `settings.yaml` |
| `docs/` | Architecture overview and API reference |

## Quick start

```bash
# Set up Python environment
bash scripts/setup.sh
source .venv/bin/activate

# Run Python tests
cd python && pytest tests/ -v

# Run JavaScript tests (Node 18+)
cd javascript && node --test
```

See `docs/architecture.md` for a full layout description.
