"""Minimal Flask demo service."""

from flask import Flask, jsonify

from demo_service.config import API_KEY, PORT

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/api/v1/hello")
def hello():
    return jsonify({"message": "Hello from Synthetic Users smoke test!", "key_set": bool(API_KEY)})


def main():
    app.run(host="0.0.0.0", port=PORT, debug=True)


if __name__ == "__main__":
    main()
