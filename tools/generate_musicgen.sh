#!/usr/bin/env bash
# Generate the MusicGen clips for the machine-listening chapter on the GPU, then re-encode them to mono MP3.
# Run as a systemd user service (see logs/); safe to rerun, finished steps are skipped.
set -euo pipefail
cd "$(dirname "$0")/.."
VENV=.venv-demucs
if ! "$VENV/bin/python" -c "import transformers, librosa" 2>/dev/null; then
  echo "[$(date +%T)] installing transformers and librosa into $VENV"
  "$VENV/bin/pip" install -q transformers librosa sentencepiece
fi
"$VENV/bin/python" -u tools/generate_musicgen.py
for f in book/audio/musicgen/*.wav; do
  m="${f%.wav}.mp3"
  [ -f "$m" ] || ffmpeg -loglevel error -y -i "$f" -ac 1 -b:a 112k "$m"
done
rm -f book/audio/musicgen/*.wav
ls -la book/audio/musicgen
echo "[$(date +%T)] done"
