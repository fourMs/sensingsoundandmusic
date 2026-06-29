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
# Mirror the deploy workflow: copy bundled web apps to a stable top-level path.
cp "_static/beating-demo.html" "_build/html/beating-demo.html" 2>/dev/null || true
cp -r "apps" "_build/html/apps" 2>/dev/null || true
echo "OK: book built with all notebooks executed."
