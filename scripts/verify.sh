#!/usr/bin/env bash
set -euo pipefail

echo "Running Python tests..."
python -m pytest -q

echo "Running Ruff lint checks..."
python -m ruff check .

echo "Verification passed."
