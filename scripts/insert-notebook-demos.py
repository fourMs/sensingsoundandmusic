#!/usr/bin/env python3
"""Insert teaching demo cells into notebooks (run: python3 scripts/insert-notebook-demos.py)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK = ROOT / "book"


def md(text: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in text.strip().split("\n")],
    }


def code(text: str) -> dict:
    return {
        "cell_type": "code",
        "metadata": {"tags": ["hide-input"]},
        "source": [line + "\n" for line in text.strip().split("\n")],
        "outputs": [],
        "execution_count": None,
    }


def insert_cells(path: Path, index: int, cells: list[dict]) -> None:
    nb = json.loads(path.read_text(encoding="utf-8"))
    for i, cell in enumerate(cells):
        nb["cells"].insert(index + i, cell)
    path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")


def main() -> None:
    sample = json.loads((BOOK / "tuning-in.ipynb").read_text(encoding="utf-8"))
    if any(
        "Interactive demo: beating two pure tones" in "".join(c.get("source", []))
        for c in sample["cells"]
    ):
        print("Demo cells already present (tuning-in); not re-inserting. Exiting.")
        return

    insert_cells(
        BOOK / "tuning-in.ipynb",
        15,
        [
            md(
                r"""### Interactive demo: beating two pure tones

When two sinusoids have nearly the same frequency, their **sum** modulates in amplitude: you hear **beats** at $|f_1 - f_2|$. This connects physics to everyday listening."""
            ),
            code(
                r"""import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio, display

sr = 22_050
duration = 3.0
t = np.linspace(0.0, duration, int(sr * duration), endpoint=False)
f1, f2 = 440.0, 443.0
x = 0.5 * (np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t))

display(Audio(x, rate=sr))
fig, ax = plt.subplots(figsize=(10, 2.2))
ax.plot(t[: int(0.05 * sr)], x[: int(0.05 * sr)], lw=0.8)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude")
ax.set_title(f"Beating: {f1:.1f} Hz + {f2:.1f} Hz (beat rate ≈ {abs(f2-f1):.1f} Hz)")
plt.tight_layout()
plt.show()"""
            ),
            md(
                r"""#### Sliders (needs `ipywidgets`)

Adjust base frequency and beat rate; if widgets do not render, run locally in Jupyter."""
            ),
            code(
                r"""try:
    import numpy as np
    import matplotlib.pyplot as plt
    from IPython.display import Audio, display
    from ipywidgets import interact

    sr = 22_050
    dur = 2.5
    t = np.linspace(0.0, dur, int(sr * dur), endpoint=False)

    @interact(f1=(200.0, 600.0, 1.0), beat_hz=(0.2, 8.0, 0.1))
    def beat_demo(f1=440.0, beat_hz=3.0):
        f2 = f1 + beat_hz
        x = 0.45 * (np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t))
        display(Audio(x, rate=sr))
        fig, ax = plt.subplots(figsize=(10, 2))
        ax.plot(t[: int(0.06 * sr)], x[: int(0.06 * sr)], lw=0.9)
        ax.set_title(f"{f1:.1f} Hz vs {f2:.1f} Hz")
        ax.set_xlabel("Time (s)")
        plt.tight_layout()
        plt.show()

except ImportError:
    print("ipywidgets not available in this environment.")"""
            ),
        ],
    )

    insert_cells(
        BOOK / "listening.ipynb",
        22,
        [
            md(
                r"""### Demo: waveform and spectrogram

Uses `book/audio/week5_audio_ex_2*.mp3` when present; otherwise a short synthetic texture so plots always build."""
            ),
            code(
                r"""from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

sr = 22_050
root = Path("audio")
candidates = sorted(root.glob("week5_audio_ex_2*.mp3")) if root.is_dir() else []
if candidates:
    y, sr = librosa.load(str(candidates[0]), sr=sr, duration=25, mono=True)
    title = f"Loaded: {candidates[0].name}"
else:
    rng = np.random.default_rng(0)
    t = np.linspace(0, 6, int(6 * sr), endpoint=False)
    y = rng.standard_normal(len(t)) * 0.08
    for hz, t0 in [(340.0, 0.8), (440.0, 2.4), (523.0, 4.1)]:
        tone = np.sin(2 * np.pi * hz * (t - t0)) * np.exp(-((t - t0) ** 2) / 0.08)
        y += 0.35 * tone
    title = "Synthetic pseudo soundscape"

fig, ax = plt.subplots(2, 1, figsize=(10, 5), sharex=True)
tt = librosa.times_like(y, sr=sr)
ax[0].plot(tt[: min(len(tt), 15 * sr)], y[: min(len(y), 15 * sr)], lw=0.35)
ax[0].set_title("Waveform (first 15 s)")
ax[0].set_ylabel("Amplitude")

S = librosa.amplitude_to_db(np.abs(librosa.stft(y, hop_length=512)), ref=np.max)
librosa.display.specshow(S, sr=sr, x_axis="time", y_axis="hz", hop_length=512, ax=ax[1], cmap="magma")
ax[1].set_ylim(0, 5000)
ax[1].set_title(title)
plt.tight_layout()
plt.show()"""
            ),
        ],
    )

    insert_cells(
        BOOK / "time-and-rhythm.ipynb",
        21,
        [
            md(
                r"""### Demo: onset strength, beat tracking, tempogram

Summarises rhythmic activity from audio (bundled Coltrane excerpt when available, otherwise a jittered click train). Third panel: **autocorrelation** of the onset envelope (pulse periodicity salience)."""
            ),
            code(
                r"""from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

sr = 22_050
hop_length = 512
audio_path = Path("audio/week5_audio_ex_2_coltrane_myfavthings.mp3")
if audio_path.is_file():
    y, sr = librosa.load(str(audio_path), sr=sr, duration=40, mono=True)
    tag = audio_path.name
else:
    bpm = 120.0
    beat_sec = 60.0 / bpm
    n_beats = 90
    n = int((n_beats + 4) * beat_sec * sr)
    y = np.zeros(n)
    rng = np.random.default_rng(2)
    for k in range(n_beats):
        j = max(0.0, k * beat_sec + rng.normal(0, 0.004))
        start = int(j * sr)
        win = np.hanning(320)
        end = min(len(y), start + len(win))
        y[start:end] += 0.95 * win[: end - start]
    tag = "synthetic clicks + jitter"

onset_env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop_length)
tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr, hop_length=hop_length)
times = librosa.times_like(onset_env, sr=sr, hop_length=hop_length)
beat_times = librosa.frames_to_time(beats, sr=sr, hop_length=hop_length)
tempo_hz = float(np.atleast_1d(tempo).ravel()[0])

tg = librosa.feature.tempogram(onset_envelope=onset_env, sr=sr, hop_length=hop_length)
centered = onset_env - onset_env.mean()
aci = np.correlate(centered, centered, mode="full")
aci = aci[len(aci) // 2 :]
lag_frames = np.arange(len(aci))
lag_sec = lag_frames * hop_length / float(sr)

fig, ax = plt.subplots(3, 1, figsize=(10, 7), sharex=False)
ax[0].plot(times, onset_env, lw=0.9)
for bt in beat_times:
    ax[0].axvline(bt, color="r", alpha=0.22, lw=0.8)
ax[0].set_title(f"Onset strength + beats (~{tempo_hz:.1f} BPM est.) — {tag}")
ax[0].set_ylabel("Strength")

img = librosa.display.specshow(tg, x_axis="time", y_axis="tempo", sr=sr, hop_length=hop_length, ax=ax[1], cmap="viridis")
ax[1].axhline(abs(tempo_hz), color="w", linestyle="--", alpha=0.55, lw=1)
fig.colorbar(img, ax=ax[1], format="%0.2f")
ax[1].set_title("Tempogram")

ax[2].plot(lag_sec[: min(len(lag_sec), 600)], aci[:600], lw=0.9, color="darkgreen")
ax[2].set_xlabel("Lag (s)")
ax[2].set_ylabel("Autocorr (onset envelope)")
ax[2].set_title("Pulse periodicity (schematic)")
plt.tight_layout()
plt.show()"""
            ),
            md(
                r"""#### Synthetic micro-jitter grid

Isochronous vs lightly jittered grid — discuss *feel* vs notation."""
            ),
            code(
                r"""import numpy as np
import matplotlib.pyplot as plt

bpm = 120.0
beat = 60.0 / bpm
n = 32
perfect = np.arange(n, dtype=float) * beat
rng = np.random.default_rng(7)
jit = rng.normal(0, 0.012, size=n)
actual = perfect + jit

fig, ax = plt.subplots(figsize=(10, 2.5))
markerline1, stemlines1, _ = ax.stem(perfect, np.ones(n), linefmt="C0-", markerfmt="C0o", basefmt=" ")
markerline1.set_label("Perfect grid")
markerline2, stemlines2, _ = ax.stem(actual, 0.82 * np.ones(n), linefmt="C1-", markerfmt="C1o", basefmt=" ")
markerline2.set_label("Jittered")
ax.set_xlim(0, n * beat)
ax.set_xlabel("Time (s)")
ax.set_title("Isochronous vs jittered onsets")
ax.legend()
plt.tight_layout()
plt.show()"""
            ),
        ],
    )

    insert_cells(
        BOOK / "physiology.ipynb",
        16,
        [
            md(
                r"""### Illustrative simulation: tonic level + phasic bursts

Toy **skin-conductance-like** trace for practising tonic vs phasic language — not measurement."""
            ),
            code(
                r"""import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

rng = np.random.default_rng(42)
t = np.linspace(0, 80, 8000)
tonic = 1.8 + 0.25 * np.sin(2 * np.pi * t / 55.0)
phasic = np.zeros_like(t)
for centre in (14.0, 22.0, 38.0, 51.0, 67.0):
    phasic += 1.4 * np.exp(-((t - centre) ** 2) / 1.1)
noise = 0.06 * rng.standard_normal(len(t))
raw = tonic + phasic + noise
smooth = savgol_filter(raw, window_length=51, polyorder=3)

fig, ax = plt.subplots(figsize=(10, 3))
ax.plot(t, raw, alpha=0.35, label="Simulated noisy trace")
ax.plot(t, smooth, lw=1.2, label="Smoothed")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Relative SC (a.u.)")
ax.set_title("Pedagogical simulation only")
ax.legend()
plt.tight_layout()
plt.show()"""
            ),
        ],
    )

    insert_cells(
        BOOK / "the-body.ipynb",
        21,
        [
            md(
                r"""### Demo: periodic vertical acceleration at ~120 BPM

A sine proxy for bounce/acceleration; FFT peak near **2 Hz** matches **120 BPM** fundamental periodicity."""
            ),
            code(
                r"""import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import rfft, rfftfreq

sr_mocap = 200
dur = 8.0
t = np.linspace(0.0, dur, int(sr_mocap * dur), endpoint=False)
bpm = 120.0
fz = bpm / 60.0
acc_z = np.sin(2 * np.pi * fz * t) + 0.08 * np.random.randn(len(t))

fk = rfftfreq(len(t), d=1.0 / sr_mocap)
spec = np.abs(rfft(acc_z))

fig, ax = plt.subplots(figsize=(10, 3))
ax.plot(fk[:120], spec[:120])
ax.axvline(fz, color="r", linestyle="--", label=f"{bpm:.0f} BPM ({fz:.2f} Hz)")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("|FFT|")
ax.set_title("Dominant periodicity in a toy bounce signal")
ax.legend()
plt.tight_layout()
plt.show()"""
            ),
        ],
    )

    insert_cells(
        BOOK / "vision.ipynb",
        15,
        [
            md(
                r"""### Schematic: overlapping auditory and visual onset energies

Illustrative **Gaussian pulses**; shaded band suggests a coarse temporal window where multisensory cues interact strongly (not fitted to individuals)."""
            ),
            code(
                r"""import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-0.25, 0.55, 800)
audio = np.exp(-((t - 0.0) ** 2) / (2 * 0.012**2))
visual = np.exp(-((t - 0.07) ** 2) / (2 * 0.018**2))

fig, ax = plt.subplots(figsize=(10, 3))
ax.plot(t * 1000, audio, label="Auditory onset energy (model)")
ax.plot(t * 1000, visual, label="Visual onset energy (model)")
ax.axvspan(-120, 120, alpha=0.15, color="green", label="±120 ms fusion sketch")
ax.set_xlabel("Time relative to auditory onset (ms)")
ax.set_ylabel("Energy (arbitrary)")
ax.set_title("Schematic audiovisual timing — pedagogy only")
ax.legend(loc="upper right", fontsize=8)
plt.tight_layout()
plt.show()"""
            ),
        ],
    )

    insert_cells(
        BOOK / "the-brain.ipynb",
        20,
        [
            md(
                r"""### Pedagogical simulation: averaged ERP waveforms

Many trials of noisy EEG plus tiny locked components average toward a smoother **event-related potential**. Purely synthetic."""
            ),
            code(
                r"""import numpy as np
import matplotlib.pyplot as plt

sr_eeg = 250
t_ms = np.linspace(-100, 500, int(600 * sr_eeg / 1000), endpoint=True)
n_trials = 100
rng = np.random.default_rng(1)
avg = np.zeros_like(t_ms)
for _ in range(n_trials):
    trial = 2.5 * rng.standard_normal(len(t_ms))
    trial -= 3.0 * np.exp(-((t_ms - 90) ** 2) / (2 * 18**2))
    trial += 5.5 * np.exp(-((t_ms - 310) ** 2) / (2 * 45**2))
    avg += trial
avg /= n_trials

fig, ax = plt.subplots(figsize=(10, 3))
ax.plot(t_ms, avg, lw=1.2)
ax.axvline(0, color="k", linestyle="--", alpha=0.4)
ax.axhline(0, color="k", linestyle="-", alpha=0.15)
ax.set_xlabel("Time (ms)")
ax.set_ylabel("µV (simulated)")
ax.set_title("Grand-average simulated ERP")
plt.tight_layout()
plt.show()"""
            ),
        ],
    )

    insert_cells(
        BOOK / "harmony-and-melody.ipynb",
        46,
        [
            md(
                r"""### Minimal `music21` example: chord spelling

Symbolic descriptions complement spectra—keep vocabulary tied to repertoire."""
            ),
            code(
                r"""from music21 import chord, stream

s = stream.Stream()
s.append(chord.Chord(["C4", "E4", "G4"], quarterLength=2))
s.append(chord.Chord(["B3", "D4", "F4"], quarterLength=2))
s.show("text")"""
            ),
        ],
    )

    print("Inserted demo cells into 8 notebooks.")


if __name__ == "__main__":
    main()
