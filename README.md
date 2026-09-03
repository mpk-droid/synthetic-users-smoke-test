# Synthetic Users Smoke Test

Tiny public repo for fast end-to-end testing of [Synthetic Users](https://github.com/mpk-droid/synthetic-users).

## What this is

A minimal sample project used to verify clone → evaluate → report workflows complete quickly.

## Layout

```
README.md         — this file
hello.py          — prints a greeting
requirements.txt  — Python dependencies
Makefile          — common dev commands
tests/            — unit tests
LICENSE           — MIT license
```

## Quick start

```bash
pip install -r requirements.txt
make run
```

Expected output: `Hello from Synthetic Users smoke test!`

## Development

Run the test suite before committing:

```bash
make test
```

See `CONTRIBUTING.md` for contribution guidelines.
