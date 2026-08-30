# Course apps (2026)

Fifteen small, self-contained WebAudio teaching apps written for the book. Each is
a single `index.html` with inline CSS and JS (vanilla JS, Web Audio API,
canvas), no external requests, and works on both phones and laptops. Sound
starts only after a user gesture. Like the vendored apps, these are copied into
the deployed site under `/apps/` by the build.

- `mini-synth/` — a small subtractive synthesiser: oscillator, lowpass filter,
  ADSR envelope, one-octave keyboard, presets, live waveform and spectrum.
  Chapter: *Electroacoustics* (also useful in *Acoustics*).
- `harmonics-explorer/` — additive synthesis with eight harmonic sliders over a
  variable fundamental, timbre presets, and a missing-fundamental toggle.
  Chapter: *Electroacoustics* / *Acoustics*.
- `inharmonicity-explorer/` — struck sounds from eight partials at non-integer
  frequency ratios, with strike/sustain modes, per-partial decay, and presets
  (harmonic, stretched, bell, gong, marimba, metal bar, drumhead).
  Chapter: *Acoustics* / *Psychoacoustics*.
- `noise-explorer/` — the noise colours (white, pink, brownian, blue, grey)
  as continuous textures or short impulses of adjustable length, with live
  waveform and spectrum. Chapter: *Acoustics*.
- `window-explorer/` — the time-frequency trade-off: test signals (clicks,
  close tones, chirp) analysed with a selectable FFT window size and drawn as a
  spectrogram (own radix-2 FFT, no libraries). Chapter: *Acoustics*.
- `hearing-test/` — a frequency sweep explorer from 20 Hz to 20 kHz with level
  control and landmark buttons, plus a same/different pitch-discrimination
  game with an adaptive difference. Not a medical test. Chapter:
  *Psychoacoustics*.
- `tap-sync/` — tap along with a click at selectable tempo; shows mean
  asynchrony and standard deviation with a histogram, plus an adjustable swing
  ratio with A/B comparison. Chapter: *Time and rhythm*.
- `spatial-hearing/` — headphones required: move a source around the head and
  hear the two localisation cues (ITD via per-ear delay, ILD via panning)
  separately or together, with three synthesised sources and a top-down head
  view. Chapter: *Psychoacoustics*.
- `shepard/` — endless Shepard tones: rising or falling, stepped or Risset
  glissando, with six octave components under a Gaussian loudness envelope
  drawn live on a canvas. Chapter: *Psychoacoustics*.
- `sampling-quantisation/` — a looped synthesised riff degraded live: simulated
  sample rate (48 kHz down to 2 kHz, sample-and-hold in an AudioWorklet with a
  ScriptProcessor fallback) and bit depth (16 down to 2 bits), with a zoomed
  waveform showing the staircase. Chapter: *Electroacoustics*.
- `interval-lab/` — two complex tones at any interval from unison to octave,
  just intonation versus equal temperament with ratio and cent readouts, a
  beating major-third demo, and a consonance ranking game compared with
  typical listener ratings. Chapter: *Harmony and melody*.
- `breath-pulse/` — no microphone or sensor: a paced-breathing guide (4–8
  breaths per minute) and a 30-second pulse-counting timer with beeps, logging
  hand-counted pulse values to an in-memory table. Chapter: *Physiology*.
- `phase-cancellation/` — constructive and destructive interference: two sine
  tones with a phase-offset slider (via a small delay) drawn with their sum,
  and a music loop against its polarity-inverted copy, where a 0–5 ms delay
  turns cancellation into audible comb filtering. Replaces the external
  Pd-based demo. Chapter: *Acoustics*.
- `room-modes/` — enter your room's length, width, and height and see its
  first axial modes (f = c/2 · n/L) on a log-frequency axis, with stacked
  modes from different dimensions flagged and a hear button per mode for
  hunting the boom. Replaces the external amroc calculator. Chapter:
  *Acoustics*.
- `live-spectrogram/` — scrolling log-frequency spectrogram (60 Hz–8 kHz) of
  the microphone via getUserMedia, with a selectable FFT size (1024/4096/16384)
  and pause; audio is analysed locally and never recorded or sent. Replaces
  the Chrome Music Lab Spectrogram links. Chapter: *Acoustics* (also used from
  *Tuning in*, *Listening*, *Psychoacoustics*, and *Vision*).
