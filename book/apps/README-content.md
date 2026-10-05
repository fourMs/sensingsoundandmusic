# Course apps (2026)

Twenty-nine small, self-contained WebAudio teaching apps written for the book. Each is
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
- `spectral-sketch/` — draw on an empty spectrogram (log-frequency canvas with
  pen, eraser, and brush size) and hear the drawing via a frame-by-frame
  inverse FFT with phase-coherent overlap-add (own radix-2 FFT, no libraries),
  with a moving playhead. Chapter: *Acoustics*.
- `window-explorer/` — the time-frequency trade-off: test signals (clicks,
  close tones, chirp) analysed with a selectable FFT window size and drawn as a
  spectrogram (own radix-2 FFT, no libraries). Chapter: *Acoustics*.
- `hearing-test/` — a frequency sweep explorer from 20 Hz to 20 kHz with level
  control and landmark buttons, plus a same/different pitch-discrimination
  game with an adaptive difference. Not a medical test. Chapter:
  *Psychoacoustics*.
- `pulse-to-pitch/` — a band-limited impulse train at any rate from 1 to
  1000 Hz on a log slider, with jump buttons and glides, a scale marking the
  regions heard as pulses, flutter, and tone, the impulses in a 250 ms window,
  the harmonic spectrum, and optional constant loudness. Chapter: *Time and
  rhythm*.
- `metre-explorer/` — a cycle of pulses grouped into beats, with presets from
  2/4 to 12/8 and additive metres such as 7/8, 11/8, and a ten-beat tala, a
  custom grouping, clicks on pulses and beats that can be silenced after four
  cycles, and circular and linear drawings of the cycle. Chapter: *Time and
  rhythm*.
- `microtiming/` — a kick, snare, and hi-hat groove on a sixteenth grid whose
  onsets can be dragged early or late on a timeline or shifted per instrument,
  with onset displacements, inter-instrument asynchronies, and the hi-hat swing
  ratio read out, and a grid/shifted switch. Chapter: *Time and rhythm*.
- `drum-machine/` — a one-bar step sequencer with kick, snare, and closed and
  open hi-hat on a grid of 8, 12, or 16 steps (two, three, or four subdivisions
  per beat), three loudness levels per hit for metric accent, presets, a swing
  ratio control, and optional clicks on beats and ticks on subdivisions.
  Chapter: *Time and rhythm*.
- `silent-beats/` — a looping bar of 4/4 with a pulse track and a sixteenth-note
  rhythm track; any click or event can be silenced, the pulse can drop out for
  whole bars, and the rhythm can be rotated against the beat, with a drawing of
  the metric levels. A listening app, nothing is measured. Chapter: *Time and
  rhythm*.
- `spontaneous-tempo/` — tap at your own rate for 10–60 s, blind (no feedback
  until the end) or live (interval plot and running tempo), and get mean
  interval, tempo, SD, CV, and drift, with a table of runs and CSV copy.
  Chapter: *Time and rhythm*.
- `tap-sync/` — tap along with a click at selectable tempo; shows mean
  asynchrony and standard deviation with a histogram, plus an adjustable swing
  ratio with A/B comparison. Chapter: *Time and rhythm*.
- `spatial-hearing/` — headphones required: move a source around the head and
  hear the two localisation cues (ITD via per-ear delay, ILD via panning)
  separately or together, with three synthesised sources and a top-down head
  view. Chapter: *Psychoacoustics*.
- `mono-stereo-binaural/` — headphones required: one three-source scene (plucked
  melody, shaker, bird chirps) rendered live as a mono sum, an equal-power
  stereo mix, or binaurally through the browser's HRTF panner, with movable or
  orbiting sources and a head view showing where each image forms. Chapter:
  *Electroacoustics*.
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
- `video-visualiser/` — live webcam analysis: motion image with noise
  threshold and gain, horizontal and vertical videograms and motiongrams,
  a self-similarity matrix, and quantity and centroid of motion over time,
  with PNG downloads; video is analysed locally and never recorded. Based on
  VideoViz (https://github.com/alexarje/videoviz). Chapter: *The body*.
- `video-scrubber/` — a video file, or a 5–20 s clip recorded with the
  camera and microphone, drawn as a videogram or motiongram above its
  waveform and spectrogram (own FFT) on one time axis, with click-to-seek,
  drag-to-loop, and PNG downloads; nothing is uploaded. Based on VideoScrub
  (https://github.com/alexarje/videoscrub). Chapter: *The body*.
- `video-sonifier/` — webcam motion as sound: the vertical motiongram used as
  the magnitude spectrum of an inverse FFT with overlap-add (AudioWorklet with
  a ScriptProcessor fallback), top of the image highest in frequency, and the
  horizontal motion balance as stereo panning, with a limiter. Based on
  webvideosonifyer (https://github.com/alexarje/webvideosonifyer). Chapter:
  *The body*.
- `camera-pulse/` — heart rate by photoplethysmography: a fingertip over the
  phone camera (torch where the browser allows it) or the face in a webcam,
  with the pulse wave, rate from intervals and from the spectrum (own FFT),
  a signal-quality indicator, rough RMSSD and SDNN, and CSV export. Chapter:
  *Physiology*.
- `breathing-monitor/` — the breathing waveform and rate from a phone lying
  on the chest (DeviceMotion) or from the chest region in a webcam, with
  breath detection, rate from intervals and from the spectrum, an optional
  pacing tone, and CSV export. Chapter: *Physiology*.
- `eye-tracker/` — a webcam demonstration of video eye tracking without
  libraries: dark-pupil detection in user-aligned eye boxes, nine-point
  calibration with a least-squares mapping and residuals, live gaze on
  notation, text, and shape stimuli with scanpath, fixations, and heatmap,
  pupil area over time, and CSV and PNG export. A teaching instrument, not a
  research one. Chapter: *Vision*.
