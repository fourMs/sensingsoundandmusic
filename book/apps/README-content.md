# Course apps (2026)

Five small, self-contained WebAudio teaching apps written for the book. Each is
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
