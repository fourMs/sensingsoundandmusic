#!/usr/bin/env bash
# Full HTML build with notebook execution — matches .github/workflows/deploy.yml.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT/book"

if ! command -v myst >/dev/null 2>&1; then
  echo "myst not found. Install: pip install -r requirements.txt" >&2
  exit 1
fi

echo "Running: myst build --html --execute (same as CI deploy)..."
myst build --html --execute
echo "OK: book built with all notebooks executed."
