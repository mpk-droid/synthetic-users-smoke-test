"""Database helpers (stub — no real driver installed)."""


def get_connection():
    """Return a database connection. Not implemented for smoke test."""
    raise NotImplementedError(
        "Install psycopg2 and configure DATABASE_URL — see docs/SETUP.md"
    )
