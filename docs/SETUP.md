# Setup Guide

## Prerequisites

- Python 3.12+
- PostgreSQL 15+ (or use Docker Compose)
- `make` and `pip`

## Local setup

1. Clone the repository.
2. Copy `.env.example` to `.env` and set `DATABASE_URL`.
3. Run `pip install -r requirements.txt`.
4. Start PostgreSQL: `docker compose up db -d` (see root `docker-compose.yml`).
5. Run migrations: `make migrate` (creates tables).
6. Start the app: `make run`.

## Database

The service expects PostgreSQL. Connection pooling is configured in `src/demo_service/db.py`.

If PostgreSQL is unavailable, `/health` still returns 200 but `/api/v1/hello` may error.

## Troubleshooting

- **Port in use:** change `PORT` in `.env` (default 8080).
- **Import errors:** ensure `PYTHONPATH` includes `src/` or use `make run`.
