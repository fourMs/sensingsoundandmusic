#!/usr/bin/env bash
# Render every LilyPond source in this folder to a cropped SVG with the same basename.
set -euo pipefail
cd "$(dirname "$0")"
for f in *.ly; do
  b="${f%.ly}"
  lilypond -s -dbackend=svg -dcrop -o "$b" "$f"
  mv "$b.cropped.svg" "$b.svg"
  rm -f "$b.cropped.png" "$b.png" "$b.pdf"
done
