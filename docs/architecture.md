# Architecture Overview

This document describes the high-level layout and design decisions of the ngara-claude playground.

## Directory Structure

```
ngara-claude/
├── python/            # Python modules and tests
│   ├── calculator.py      — pure math utilities
│   ├── data_processor.py  — CSV/JSON loading and transformation
│   └── tests/
│       ├── test_calculator.py
│       └── test_data_processor.py
├── javascript/        # Node.js modules
│   ├── utils.js           — general-purpose helpers
│   └── api_client.js      — HTTP client with retry + timeout
├── sql/               # Database schema and example queries
│   ├── schema.sql
│   └── queries.sql
├── data/              # Sample datasets
│   ├── users.json
│   ├── sales.csv
│   └── config.json
├── scripts/           # Shell automation
│   ├── setup.sh
│   └── cleanup.sh
├── config/            # App configuration
│   ├── .env.example
│   └── settings.yaml
└── docs/              # Documentation
    ├── architecture.md  (this file)
    └── api.md
```

## Design Principles

1. **Self-contained modules** — each file in `python/` and `javascript/` is independently importable with no inter-module dependencies.
2. **Real data shapes** — datasets in `data/` mirror realistic schemas so queries and transformations are non-trivial.
3. **Idiomatic style** — Python code follows PEP 8; JavaScript follows CommonJS conventions.

## Running Tests

```bash
# Python
cd python
pip install -r requirements.txt
pytest tests/ -v

# JavaScript (Node 18+ built-in test runner)
cd javascript
node --test
```

## Database Setup

Apply the schema to a local Postgres instance:

```bash
psql -U postgres -d playground_db -f sql/schema.sql
```
