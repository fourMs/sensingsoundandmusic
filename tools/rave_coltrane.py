"""Play the Coltrane excerpt through pretrained RAVE models (IRCAM, open weights) for the machine-listening chapter.

RAVE is a variational autoencoder trained on audio of one kind; encoding a different sound and
decoding it again gives timbre transfer. Models are TorchScript files from IRCAM's server; the
excerpt is resampled to each model's rate, encoded and decoded block by block on the GPU.
Finished outputs are skipped, so the script can be rerun.
"""
import os, sys, time, json, urllib.request
import numpy as np
import torch, librosa, scipy.io.wavfile as wavfile

MODELS = ["vintage", "percussion"]
OUT = "book/audio/rave"
CACHE = os.path.expanduser("~/.cache/rave_models")
os.makedirs(OUT, exist_ok=True); os.makedirs(CACHE, exist_ok=True)
SECONDS = 30
device = "cuda" if torch.cuda.is_available() else "cpu"
log = lambda *a: print(time.strftime("[%H:%M:%S]"), *a, flush=True)
meta = {}
for name in MODELS:
    out = f"{OUT}/{name}.wav"
    if os.path.exists(out) or os.path.exists(out.replace(".wav", ".mp3")):
        log(name, "already done"); continue
    path = f"{CACHE}/{name}.ts"
    if not os.path.exists(path):
        log("downloading", name)
        urllib.request.urlretrieve(f"https://play.forum.ircam.fr/rave-vst-api/get_model/{name}", path + ".part")
        os.rename(path + ".part", path)
    model = torch.jit.load(path, map_location=device).eval()
    sr = int(getattr(model, "sr", getattr(model, "sampling_rate", 48000)))
    y, _ = librosa.load("book/audio/week6_audio_ex_2_coltrane_myfavthings.mp3", sr=sr, mono=True, duration=SECONDS)
    block = 2048 * 8
    pad = (-len(y)) % block
    x = torch.from_numpy(np.pad(y, (0, pad))).float().reshape(1, 1, -1).to(device)
    t0 = time.time()
    with torch.no_grad():
        z = model.encode(x)
        out_audio = model.decode(z)
    out_audio = out_audio.reshape(-1).cpu().numpy()[: len(y)]
    out_audio = out_audio / max(1e-9, np.abs(out_audio).max()) * 0.9
    wavfile.write(out, sr, out_audio.astype(np.float32))
    meta[name] = {"model": f"IRCAM RAVE pretrained '{name}'", "sr": sr, "latent_dims": int(z.shape[1]), "latent_rate_hz": round(float(z.shape[2]) / (x.shape[-1] / sr), 2),
                  "seconds": SECONDS, "generation_s": round(time.time() - t0, 1), "file_mb": round(os.path.getsize(path) / 1e6, 1)}
    log("wrote", name, meta[name])
    del model; torch.cuda.empty_cache()
if meta:
    old = json.load(open(f"{OUT}/meta.json")) if os.path.exists(f"{OUT}/meta.json") else {}
    old.update(meta); json.dump(old, open(f"{OUT}/meta.json", "w"), indent=1)
log("done")
