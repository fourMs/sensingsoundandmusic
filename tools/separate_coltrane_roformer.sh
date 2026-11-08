#!/usr/bin/env bash
# Second separator for the comparison: BS-RoFormer (vocals / instrumental) through audio-separator, on the GPU.
set -euo pipefail
cd "$(dirname "$0")/.."
VENV=.venv-demucs
if ! "$VENV/bin/python" -c "import audio_separator" 2>/dev/null; then
  echo "[$(date +%T)] installing audio-separator (GPU extras) into $VENV"
  "$VENV/bin/pip" install -q "audio-separator[gpu]" audioread
fi
OUT=book/audio/coltrane_roformer
if ls "$OUT"/*.mp3 >/dev/null 2>&1; then echo "[$(date +%T)] roformer stems already present"; exit 0; fi
mkdir -p "$OUT"
echo "[$(date +%T)] separating with BS-RoFormer (ep 317, SDR 12.98 vocals model)"
"$VENV/bin/audio-separator" book/audio/week6_audio_ex_2_coltrane_myfavthings.mp3 -m model_bs_roformer_ep_317_sdr_12.9755.ckpt --output_dir "$OUT" --output_format mp3
ls -la "$OUT"
echo "[$(date +%T)] done"
