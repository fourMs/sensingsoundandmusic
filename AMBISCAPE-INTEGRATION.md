# Integrating ambiscape and the AMBIENT research into MUS2640

How the [ambiscape](https://github.com/fourMs/ambiscape) soundscape-analysis
toolbox (and the research it grew out of, the *Still Standing* and *Sound
Spaces* work) can be folded into *Sensing Sound and Music*. Written as a
companion to `COURSE-REVIEW.md`.

## The through-line

ambiscape gives the course something it currently lacks: a worked, hands-on
example of machine listening applied to everyday sound, not just music. The
course already teaches the pipeline (waveform → framing → features → task) on
Sonny Rollins solos; ambiscape lets students run the *same* pipeline on a
room, a train, a café, and see what changes. The pedagogical payoff is one
idea the *Sound Spaces* book makes explicitly: music analysis is soundscape
analysis with the foreground bias inverted. MIR was built to attend to the
notes and treat everything else as "background noise," whereas a soundscape's
subject *is* the background (the keynote hum, the diffuse field, the slow
envelope of the day). Teaching both, side by side, sharpens what "features"
and "listening" actually mean.

A second payoff is that ambiscape's core is light (numpy / scipy /
soundfile; `librosa` is already a course dependency), so a real analysis runs
in the book's CI without new heavy machinery. The `[iso]` (MoSQITo) and `[ml]`
(PANNs/BirdNET, torch) extras are too heavy for `myst build --execute`; use
the core for executable cells and show pre-rendered outputs for the rest.

## Chapter-by-chapter map

| Ch | Where ambiscape / the research fits | Concrete addition |
|---|---|---|
| **12 Machine listening** *(flagship)* | feature extraction; "source separation" → source *decomposition*; event detection; "Multimodal MIR" → `vision.py`; ethics | a runnable soundscape-analysis example + a source-decomposition demo (see below) |
| **2 Listening** | Schafer's soundscape: keynote / sound signal / soundmark, hi-fi vs lo-fi | the taxonomy is directly the `ambiscape taxonomy` workflow; add the Schaeffer map + Schafer timeline as a figure pair |
| **3 Acoustics** | room acoustics, reverberation, ISO metrics | `ambiscape` computes T60/EDT/C50/C80 and ISO 1996 levels (Leq, LAeq, L10/L50/L90); a "measure your own room" exercise |
| **5 Electroacoustics** | spatial audio, ambisonics, B-format | first-order AmbiX, the pseudo-intensity vector, **diffuseness ψ** as a room-state descriptor no mono signal carries |
| **6 Time and rhythm** | rhythm beyond the beat | "a room's rhythm runs slower than a drummer's" — modulation spectra, a fridge's duty cycle, a train's driving/dwelling alternation (the modulation / mechanical-periodicity modules) |
| **10 Vision** *(currently thin, ~2.8k words)* | the AMBIENT audio-visual room-capture; visual features | `ambiscape vision` extracts per-frame brightness/colour/light-direction/motion aligned to the audio timeline — a concrete multimodal example the chapter could use to grow |
| **4 Psychoacoustics** | loudness / sharpness / roughness | ISO 532-1 loudness N5/N50, sharpness, roughness (via `ambiscape[iso]`) as the applied side of the JND/loudness theory |
| **8 The body / 9 Physiology** | the *Still Standing* research | micromotion and standstill; the coupling of heart rate and respiration to bodily sway (a concrete empirical example the review flags physiology as needing) |

## Flagship: a soundscape section in *Machine listening*

Add an "Examples" subsection, *Listening to a room*, that runs ambiscape on
a short bundled clip and contrasts it with the Rollins examples already in the
chapter:

1. **Features on a room, not a solo.** Load a ~30 s soundscape clip; show the
   same features (spectral centroid, flatness, level) the chapter already
   teaches, but computed on a café or a train. The point is that the
   features are generic, and the *interpretation* is what differs.
2. **Source decomposition** (the new v0.15 detectors). Compute the
   geophony / biophony / anthropophony / mechanical indices and ask *which
   domain owns this room?* The train reads ~0.93 low-frequency, almost
   wholly mechanical; a park reads biophonic. This is the natural
   soundscape counterpart to the chapter's "source separation" section.
3. **Event detection** against a running background, the same idea as onset
   detection, turned on footsteps and announcements instead of notes.
4. **Ethics tie-in.** ambiscape's `deposit` (a non-identifying 1 Hz feature
   stream) and the silero-VAD privacy gate are a concrete, working answer to
   the chapter's ethics section: *publish features, not audio* when recording
   in private/inhabited spaces.

### Minimal runnable cell (core deps only)

```python
# add `ambiscape` to requirements.txt (core is numpy/scipy/soundfile-light)
import ambiscape as asc
from ambiscape import features, mechanical, anthropophony, geophony

sess = asc.open_recording("audio/soundscape_example.wav")  # a short clip to bundle
F = features.load_features(features.extract_session(sess, "/tmp/feat"))

print("mechanical:", mechanical.summarize_mechanical(F)["mechanical_index"])
print("anthropophony:", anthropophony.summarize_anthropophony(F)["anthropophony_index"])
print("geophony:", geophony.summarize_geophony(F)["geophony_index"])
```

*Asset needed:* one short (~30 s), non-identifying soundscape clip in
`book/audio/` (mono/stereo is fine, since ambiscape handles both; a 4-channel
AmbiX clip additionally unlocks the diffuseness/azimuth demo for Ch 5).

## Suggested exercises

- **Ch 2 / 12:** record 60 s of your kitchen and 60 s outdoors; run the source
  decomposition; predict which domain dominates each, then check.
- **Ch 3:** clap once in a room, estimate its T60 with `ambiscape.decay_metrics`,
  and relate it to how the room "sounds."
- **Ch 6:** record 10 minutes somewhere with a machine (fridge, fan); find its
  duty cycle in the modulation profile, "the room's tempo."
- **Ch 12 (ethics):** compare what a raw recording reveals vs the 1 Hz deposit
  stream; discuss when each is publishable.

## Practical steps

1. Add `ambiscape` to `requirements.txt` (core only, not `[ml]`/`[iso]`,
   which pull torch/MoSQITo and are too heavy for CI).
2. Bundle one short soundscape clip in `book/audio/` (the review already notes
   the `../audio` path issue, so verify it while adding).
3. Draft the *Machine listening* "Examples" subsection first (highest value,
   self-contained); pre-render any `[iso]`/`[ml]` outputs as static figures.
4. Keep heavy analyses (ISO loudness, PANNs tagging, BirdNET) as *shown*
   results, not executed cells.

## What to fold in from the research (beyond the tool)

- **Schafer's source taxonomy** (keynote/signal/soundmark, hi-fi/lo-fi) and
  Krause's geophony/biophony/anthropophony, now measurable, so the course
  can move from citing them to computing them.
- **Diffuseness as a room signature** — machine-dominated rooms collapse to
  ψ≈0.2 and transit halls sit at 0.85–0.90, a spatial-hearing point mono audio
  cannot make (Ch 5).
- **State-resolution / "before you average, ask whether the thing was ever one
  thing"** — a transferable data-literacy lesson for the whole book (Ch 12).
- **The *Still Standing* standstill work** — micromotion, and heart-rate /
  respiration coupling to sway — as the physiology chapter's missing concrete
  empirical example (Ch 8/9).
