"""Generate short clips with MusicGen (Meta, open weights, CC-BY-NC) on the GPU for the machine-listening chapter.

Two clips: one from a text prompt alone (musicgen-small), one conditioned on the melody of the
Coltrane excerpt (musicgen-melody). Written as 32 kHz WAV, then re-encoded to mono MP3 by the
calling shell script. Finished clips are skipped, so the script can be rerun.
"""
import os, sys, time, json
import numpy as np
import torch, librosa, scipy.io.wavfile as wavfile
from transformers import AutoProcessor, MusicgenForConditionalGeneration, MusicgenMelodyForConditionalGeneration

OUT = "book/audio/musicgen"
os.makedirs(OUT, exist_ok=True)
SECONDS = 15
TOKENS = SECONDS * 50          # MusicGen produces 50 codebook frames per second
device = "cuda" if torch.cuda.is_available() else "cpu"
log = lambda *a: print(time.strftime("[%H:%M:%S]"), *a, flush=True)
log("device", device, torch.cuda.get_device_name(0) if device == "cuda" else "")
meta = {}

def save(name, audio, sr):
    audio = np.asarray(audio, dtype=np.float32)
    if audio.ndim > 1:
        audio = audio.mean(axis=0)
    audio = audio / max(1e-9, np.abs(audio).max()) * 0.9
    wavfile.write(f"{OUT}/{name}.wav", sr, audio)
    log("wrote", name, f"{len(audio)/sr:.1f} s at {sr} Hz")

# 1. Text to music
TEXT_PROMPT = "upbeat funk with slap bass, drums and electric piano"
if not os.path.exists(f"{OUT}/text_funk.wav"):
    log("loading facebook/musicgen-small")
    proc = AutoProcessor.from_pretrained("facebook/musicgen-small")
    model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small").to(device)
    sr = model.config.audio_encoder.sampling_rate
    inputs = proc(text=[TEXT_PROMPT], padding=True, return_tensors="pt").to(device)
    torch.manual_seed(0)
    t0 = time.time()
    with torch.no_grad():
        audio = model.generate(**inputs, do_sample=True, guidance_scale=3, max_new_tokens=TOKENS)
    meta["text_funk"] = {"model": "facebook/musicgen-small", "prompt": TEXT_PROMPT, "seconds": SECONDS,
                         "generation_s": round(time.time() - t0, 1), "seed": 0}
    save("text_funk", audio[0].cpu().numpy(), sr)
    del model; torch.cuda.empty_cache()

# 2. Melody-conditioned: the Coltrane excerpt as the melody, a new text prompt as the style
MELODY_PROMPT = "string quartet, chamber music, slow and lyrical"
if not os.path.exists(f"{OUT}/melody_coltrane.wav"):
    log("loading facebook/musicgen-melody")
    proc = AutoProcessor.from_pretrained("facebook/musicgen-melody")
    model = MusicgenMelodyForConditionalGeneration.from_pretrained("facebook/musicgen-melody").to(device)
    sr = model.config.audio_encoder.sampling_rate
    y, _ = librosa.load("book/audio/week6_audio_ex_2_coltrane_myfavthings.mp3", sr=sr, mono=True, duration=SECONDS)
    save("melody_input", y, sr)
    inputs = proc(audio=y, sampling_rate=sr, text=[MELODY_PROMPT], padding=True, return_tensors="pt").to(device)
    torch.manual_seed(0)
    t0 = time.time()
    with torch.no_grad():
        audio = model.generate(**inputs, do_sample=True, guidance_scale=3, max_new_tokens=TOKENS)
    meta["melody_coltrane"] = {"model": "facebook/musicgen-melody", "prompt": MELODY_PROMPT, "melody": "Coltrane excerpt, first 15 s",
                               "seconds": SECONDS, "generation_s": round(time.time() - t0, 1), "seed": 0}
    save("melody_coltrane", audio[0].cpu().numpy(), sr)

if meta:
    old = json.load(open(f"{OUT}/meta.json")) if os.path.exists(f"{OUT}/meta.json") else {}
    old.update(meta)
    json.dump(old, open(f"{OUT}/meta.json", "w"), indent=1)
log("done")
