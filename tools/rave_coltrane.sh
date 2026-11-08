#!/usr/bin/env bash
# Timbre transfer of the Coltrane excerpt through pretrained RAVE models on the GPU, then mono MP3.
# Run as a systemd user service (see logs/); safe to rerun, finished steps are skipped.
set -euo pipefail
cd "$(dirname "$0")/.."
VENV=.venv-demucs
"$VENV/bin/python" -u tools/rave_coltrane.py
[ -f book/audio/rave/input.mp3 ] || ffmpeg -loglevel error -y -i book/audio/week6_audio_ex_2_coltrane_myfavthings.mp3 -t 30 -ac 1 -b:a 112k book/audio/rave/input.mp3
for f in book/audio/rave/*.wav; do
  [ -e "$f" ] || continue
  m="${f%.wav}.mp3"; [ -f "$m" ] || ffmpeg -loglevel error -y -i "$f" -ac 1 -b:a 112k "$m"; rm -f "$f"
done
ls -la book/audio/rave
echo "[$(date +%T)] done"
