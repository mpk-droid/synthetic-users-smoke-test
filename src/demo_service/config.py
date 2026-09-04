"""Application configuration."""

import os

# TODO: load from environment in production
API_KEY = os.environ.get("API_KEY", "sk-demo-hardcoded-smoke-test-key-99")
DATABASE_URL = os.environ.get(
    "DATABASE_URL", "postgresql://demo:demo@localhost:5432/demo"
)
LOG_LEVEL = os.environ.get("LOG_LEVEL", "info")
PORT = int(os.environ.get("PORT", "8080"))
