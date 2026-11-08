#!/usr/bin/env bash
# Separate the Coltrane excerpt into six stems with Demucs (htdemucs_6s: drums, bass, other, vocals, guitar, piano) on the GPU.
# Run as a systemd user service (see logs/); safe to rerun, finished steps are skipped.
set -euo pipefail
cd "$(dirname "$0")/.."
VENV=.venv-demucs
if ! "$VENV/bin/python" -c "import demucs, numpy" 2>/dev/null; then
  echo "[$(date +%T)] creating $VENV and installing torch (CUDA build) and demucs"
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install -q --upgrade pip
  "$VENV/bin/pip" install -q torch torchaudio
  "$VENV/bin/pip" install -q demucs numpy
  "$VENV/bin/python" -c "import torch; print('torch', torch.__version__, 'cuda available:', torch.cuda.is_available(), torch.cuda.get_device_name(0) if torch.cuda.is_available() else '')"
fi
OUT=book/audio/coltrane_stems
if [ -f "$OUT/piano.mp3" ]; then echo "[$(date +%T)] stems already present in $OUT"; exit 0; fi
echo "[$(date +%T)] separating with htdemucs_6s on the GPU"
"$VENV/bin/demucs" -n htdemucs_6s -d cuda --mp3 --mp3-bitrate 192 -o /tmp/demucs_out book/audio/week6_audio_ex_2_coltrane_myfavthings.mp3
mkdir -p "$OUT"
cp /tmp/demucs_out/htdemucs_6s/week6_audio_ex_2_coltrane_myfavthings/*.mp3 "$OUT"/
ls -la "$OUT"
echo "[$(date +%T)] done"
