# Demo Service

A small Python HTTP service for Synthetic Users smoke testing. It exposes a health endpoint and a greeting API.

## What this is

Sample backend used to validate clone → evaluate → report workflows with realistic repo structure (src layout, docs, CI, container files).

## Layout

```
README.md
pyproject.toml
requirements.txt
Makefile
Dockerfile
docker-compose.yml
.env.example
src/demo_service/     — application code
docs/SETUP.md         — extended setup notes
tests/                — unit tests
.github/workflows/    — CI pipeline
```

## Quick start

```bash
cp .env.example .env
pip install -r requirements.txt
make run
```

Service listens on **http://localhost:8080**.

- `GET /health` → `{"status":"ok"}`
- `GET /api/v1/hello` → greeting JSON

## Development

```bash
make install    # install dependencies
make test       # run pytest
make lint       # ruff check
```

See `docs/SETUP.md` for database and Docker Compose instructions.

## Deployment

```bash
docker compose up --build
# or
make docker-build && make docker-run
```

## Configuration

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | PostgreSQL connection string |
| `API_KEY` | Service API key for `/api/v1/*` |
| `LOG_LEVEL` | Logging level (default: info) |

Copy `.env.example` and fill in values before running locally.
