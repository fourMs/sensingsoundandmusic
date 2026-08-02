# Balance and depth review — *Sensing Sound and Music* (MUS2640)

> **Status: all items below have been acted on** (2026-07-24). The measurements in §1 are the *before* state; see §8 for what changed and the numbers afterwards. The diagnosis is kept intact as the record of why the changes were made.

Reviewed against the stated audience: bachelor students in **musicology first**, psychology and technology second, with each chapter carrying one week of teaching (2–3 h in class, ~6 h outside).

Prose word counts exclude code, frontmatter and link URLs. Everything below was measured from the notebooks in `book/` on the current `main`.

---

## 1. The numbers

| Wk | Chapter | Prose words | Code lines | Exercises | Q-admonitions | Figures/images | Audio ex. |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Tuning in | 4176 | 16 | 3 | 4 | 2 | – |
| 2 | Listening | 3836 | 34 | 3 | 0 | 1 | – |
| 3 | Acoustics | 5358 | 357 | 5 | 0 | 5 | – |
| 4 | Psychoacoustics | 4705 | 254 | 6 | 1 | 13 | ✔ |
| 5 | Electroacoustics | 5019 | 202 | 3 | 0 | 1 | – |
| 6 | Time and rhythm | 4102 | 97 | **7** | 0 | 16 | **12** |
| 7 | Harmony and melody | 3859 | 337 | 6 | 0 | 3 | ✔ |
| 8 | The body | 4704 | 21 | 3 | 1 | 13 | – |
| 9 | Physiology | **3023** | 48 | **0** | 2 | 3 | – |
| 10 | Vision | **2679** | 35 | **0** | 1 | 5 | – |
| 11 | The brain | 4635 | 46 | **0** | 0 | 7 | – |
| 12 | Machine listening | 4988 | 124 | **0** | 3 | 0 | – |

Total ≈ 53.7k words of prose (plus intro 2.1k and Tips and tricks 0.5k).

---

## 2. Length balance: acceptable

Reading load runs 2.7k–5.4k words, a factor of two. For a course where students also do listening, exercises and their own reading, that spread is within normal tolerance. Only two chapters stand out:

- **Vision (W10, 2679 words)** is half the mean and the lightest week in the book. It is not a bad chapter — it is well linked to actual RITMO work — it is simply short.
- **Physiology (W9, 3023 words)** is similarly light *in length* but not in difficulty (see §4).

If nothing else changes, weeks 9–10 read as a mid-semester dip in a course that gets *harder* immediately afterwards.

---

## 3. The real imbalance: student activity collapses after week 8

| Weeks | Exercises |
|---|---|
| 1–8 | 3, 3, 5, 6, 3, 7, 6, 3 = **36** |
| 9–12 | 0, 0, 0, 0 = **0** |

This is the single largest structural problem in the book, for three reasons:

1. **It contradicts the intro.** The course schedule table in `intro.ipynb` promises an applied activity for every week, including W9 ("Relate one physiological idea to your own listening experience"), W10 ("Short clip: note where you look vs what you hear"), W11 ("Pick one finding; identify claim–evidence–method") and W12 ("Run or inspect one feature plot; discuss bias/dataset limits"). None of these exist in the chapters.
2. **It contradicts the pedagogy.** The intro commits to active learning and a flipped classroom. The last third of the semester offers nothing to flip.
3. **It lands at the worst moment.** Weeks 9–12 are four consecutive *methods survey* chapters: how to measure physiology, how to track eyes, how to scan brains, how to build ML pipelines. Read back to back, with no exercises, right before exams, this is where a musicology cohort is most likely to disengage.

Week 6 has the opposite problem: seven exercises, several of them heavy (install Sonic Visualiser **and** the Vamp plugin pack; register for moises.ai; two tapping tasks with data submitted via Google Forms). It is comfortably the largest homework week in the book, and it sits next to weeks with none.

**Recommendation.** Move roughly three exercises' worth of work from W6 to W9–W12, or simply write the four activities the intro already promises. This is the cheapest high-impact change available.

---

## 4. Depth: the book has three registers, and they do not track the audience

The level of a chapter currently correlates with who wrote it rather than with who reads it. Three distinct registers coexist:

**(a) Humanities/conceptual — right for the primary audience.**
*Tuning in, Listening, Vision, The brain.* Definitions, historical figures, arguments, cultural framing. Listening (W2) in particular is exactly the register a musicology BA expects.

**(b) Undergraduate science textbook — mostly right.**
*Acoustics, Psychoacoustics, The body, Physiology.* Psychoacoustics is the best-balanced chapter in the book. Every technical idea (masking, JND, ITD/ILD, missing fundamental) is anchored to something audible and usually to an exercise.

**(c) Professional / graduate technical — too deep as core material.**
*Electroacoustics, Time and rhythm, Machine listening,* and parts of *Harmony and melody*.

Concrete instances of (c):

- **W5 Electroacoustics** turns into an audio-engineering manual: a microphone specification table with sensitivity in dBV/Pa, self-noise in dB(A), output impedance in Ω; signal levels in dBu; equivalent input noise; Class D efficiency; boundary loading; line arrays. Useful for a technology student, near-unusable for a musicology student, and it carries only 3 exercises across 5k words. It is also the chapter with the least perceptual or musical framing.
- **W6 Time and rhythm** is the most research-level chapter, and the best-sourced. But P-centres, IPI vs IOI, swing ratios in ms and decimals, and JND thresholds by instrument class are presented at seminar level. The swing-ratio formula appears inline in a dense paragraph (and is mis-parenthesised, see §6).
- **W12 Machine listening** contains the most advanced prose in the book: latency arithmetic (`n_fft=2048 at sr=22050 → window ≈ 92.9 ms`), TCN dilation rates, quadratic cost of attention, SDR/SIR/SI-SNR, MUSHRA protocols. The long "Machine vs human listening" section is an abstract research-agenda essay with almost no concrete musical example. There is not one worked case a musicology student can follow end to end.
- **W7 Harmony and melody** is bimodal. It explains what a triad is, then hands the reader a `librosa.pyin` f0-extraction error-analysis lab with a blank annotation worksheet (error type, spectrogram evidence, confidence rating). Two very different assumed backgrounds inside one chapter.
- **W3 Acoustics** is well pitched until its tail: C50/C80 clarity indices with ISO 3382 procedure, Beranek's bass ratio, and a five-way window-function taxonomy including the Terhardt window. All core prose, none flagged as optional.
- **W8 The body** spends a large, well-written block on generic anatomy and biomechanics (anatomical planes, agonist/antagonist/fixator, DoF and RoM, statics/dynamics, kinematics/kinetics). It is essentially a sports-science module; the music-specific payoff is thinner than its length implies.
- **W9 Physiology**, though the second-shortest chapter, has the highest jargon density in the book — RSA, SCL/SCR, RIP belts, tonic vs phasic, SDNN, RMSSD, plus a sensor table with recommended sampling rates — with few musical examples to anchor them and no exercises.

**Recommendation.** Adopt one consistent "dig deeper" convention (a MyST dropdown or `:::{note}`) and move the following out of the main narrative without deleting them:

| Chapter | Move to optional |
|---|---|
| W3 Acoustics | C50/C80, bass ratio, window-type taxonomy |
| W5 Electroacoustics | Microphone specification table, dBu signal levels, Class D / boundary loading / line arrays |
| W6 Time and rhythm | Swing-ratio formalism and JND threshold values |
| W7 Harmony and melody | The f0 extraction lab + annotation worksheet |
| W12 Machine listening | Model families (HMM/RNN/TCN/transformer), realtime latency arithmetic |

That keeps the technology students served while letting the musicology reading path stay continuous, which is precisely what "primarily musicology, secondarily psychology and technology" implies.

Two further depth-balancing moves:

- **Give W12 a musical spine.** One track carried end to end — chroma → key, onset → beat → tempo, self-similarity → sections — and then the question "what can a musicologist now say that they couldn't before?" The parts already exist; they are just not strung together.
- **Give W9 one concrete study.** A single worked example (e.g. cardiac synchrony in a choir or in the Bodies in Concert work already cited in W10) would do more than another paragraph of mechanism.

---

## 5. Cross-chapter overlap

Concept mentions by chapter (markdown only):

| Concept | Where it appears |
|---|---|
| Timbre | W3 (9), W4 (10), W5 (6, incl. a full "Timbre design" note), W7 (25), W11 (7) |
| Auditory scene analysis | W6 (1), **W7 (4)** — but *not* W4 |
| Gestalt grouping | W7 only |
| Auditory illusions | W4 (5) and W7 (4) |
| Entrainment | W6 (7) and W9 (9) |
| Auditory pathway (ear → cortex) | W4 and again at length in W11 |

Timbre is currently defined from scratch three times. The auditory pathway is traced twice. Neither is fatal, but each repetition is prose that could have been an exercise in weeks 9–12.

More importantly there is a **hole**: auditory streaming / auditory scene analysis is promised for W4 in the intro schedule ("Thresholds, critical bands, streaming"), is asked about in W4's own exam questions, and is actually taught in W7. See §6.

---

## 6. Concrete defects found while reading

These are worth fixing regardless of any restructuring.

**Content mismatches**

1. `psychoacoustics.ipynb` — end-of-chapter Question 2 asks "what is tonotopic organisation?" and Question 4 asks about "continuity and streaming phenomena". Neither term is used anywhere in the chapter body; "tonotopic" appears only in the question itself, and streaming/ASA is only touched in one clause. Either add a short ASA/streaming section to W4 (and cross-reference from W7 rather than re-explaining), or rewrite the two questions.
2. `the-brain.ipynb` — Question 4 asks "what caveats apply" to mirror-neuron accounts; the chapter presents mirror neurons enthusiastically with no caveats.
3. `time-and-rhythm.ipynb` — the chapter cites eight footnotes `[^1]`–`[^8]`, and **none of them have definitions**. The one chapter with real academic sourcing renders with dangling references.

**Markup bugs**

4. Nested same-level fences close their parent directive early:
   - `electroacoustics.ipynb` cell 9 — ```` ```{image} ```` inside ```` ```{note} ````
   - `time-and-rhythm.ipynb` cell 22 — ```` ```{image} ```` inside ```` ```{exercise} ````
   In the built output the exercise's final "Reflect:" paragraph falls **outside** the exercise box, and both cells emit a stray empty code block. Fix by using `:::` for the outer directive.
5. `electroacoustics.ipynb` — bone-conduction bullet opens with `**[` and closes with a single `*`, so emphasis is unbalanced.
6. `time-and-rhythm.ipynb` — the swing ratio is written `𝑅 = 𝑚 + 𝑑 / 𝑚 − 𝑑`; it needs parentheses: (m + d)/(m − d).
7. `acoustics.ipynb` uses `text-align:centre`, which is invalid CSS (must be `center`); `tuning-in.ipynb` has a figure with `:align: centre`, not a valid MyST value. Both are collateral damage from the British-spelling sweep.

**Consistency**

8. Title Case headings survive mainly in `machine-listening.ipynb` ("Machine Listening", "Source Separation", "Music Data", "Rule-based vs Learning-based systems") and `vision.ipynb` ("The Eye", "Eye Tracking", "Integration of Senses"); the rest of the book is sentence case. Chapter *titles* are also mixed: "8. The Body", "11. The Brain", "12. Machine Listening" vs "3. Acoustics", "6. Time and rhythm".
9. `harmony-and-melody.ipynb` is the only chapter still carrying a `description:` frontmatter field.
10. `acoustics.ipynb` opens with three `###` sections before its first `##`, while every other chapter starts at `##`.
11. In `harmony-and-melody.ipynb`, six sections (Timbre, Auditory scene analysis, Gestalt theory, Auditory illusions, Texture, Listening checklist) sit *under* `## Melody`, which they are not about. The chapter has only three H2s carrying 22 H3s.
12. `book/references.bib` holds 15 entries but no chapter uses `{cite}` anywhere. All in-text sourcing is Wikipedia links plus the per-chapter "Further reading" blocks. For a course that explicitly teaches students to read and cite empirical research (intro, "Reading empirical research"), the book currently models Wikipedia citation.
13. Two chapters lack an "Explore interactively" block (Physiology, The brain) though all others have one.

---

## 7. Priority order

1. Write the four missing weekly activities for W9–W12 (already promised in the intro schedule) and lighten W6 from seven exercises to about four.
2. Fix the content mismatches and markup bugs in §6. They are small, self-contained, and two of them are visible on the published site.
3. Introduce the "dig deeper" convention and move the material listed in §4 into it.
4. Give W12 one end-to-end worked musical example, and W9 one concrete empirical study.
5. Decide single homes for timbre, ASA/Gestalt/illusions and the auditory pathway; cross-reference elsewhere.
6. Grow Vision (W10) by ~700 words, or accept it as the deliberate light week and say so in the intro.
7. Sweep heading case and the remaining frontmatter inconsistency.

---

## 8. What was changed

### Activity balance (§3)

| Wk | Chapter | Exercises before | after |
|---:|---|---:|---:|
| 6 | Time and rhythm | 7 | 4 core + 3 marked *Optional* |
| 9 | Physiology | 0 | 3 |
| 10 | Vision | 0 | 3 |
| 11 | The brain | 0 | 2 |
| 12 | Machine listening | 0 | 2 |

The new exercises are the ones the intro schedule already promised: relating a physiological idea to your own listening (W9), watching where you look versus what you hear (W10), a claim–evidence–method reading (W11), and running the feature pipeline on your own audio plus a dataset audit (W12). Week 6 now states in its opening which exercises are core and which can be skipped.

### Depth (§4)

Eleven **"Dig deeper"** dropdowns now hold the specialist material, with a short plain-language summary left in the main narrative:

- **W3** window-type taxonomy; clarity indices and bass ratio (the section is now "Beyond reverberation time", with the ISO 3382 procedure and target ranges inside the dropdown).
- **W5** the full microphone specification sheet; nominal levels in dBu. Class D, boundary loading and line arrays rewritten in plain terms.
- **W6** the swing-ratio formalism (formula now correctly parenthesised and set as maths) and the measured JND thresholds.
- **W8** the kinematic and kinetic term lists, with a new paragraph up front saying why a musicologist needs the vocabulary at all (bowing arm, pianists' joint angles, drum-stroke separation).
- **W12** model families (HMM/RNN/TCN/transformer), the realtime latency arithmetic, and the perceptual-evaluation essay.
- **W7** the f0-extraction lab and its worksheet are relabelled *Optional* with a sentence saying the chapter continues without them.

**W12 now has a musical spine.** A new "Worked example: what can we now say about this track?" section pulls the chapter's separate analyses into one summary (duration, prominent pitch class, Krumhansl–Schmuckler key estimate, tempo, tracked beats, segment boundaries) and then reads that output critically: the key label forces a major/minor choice on modal music, the tempo is vulnerable to octave error in a waltz, and the twenty "sections" exist because the code asked for twenty. It ends on what machine listening does and does not give a musicologist.

**W9 now has a worked case** — Vickhoff et al. (2013) on choir singing, breathing, and heart-rate variability — presented as claim / mechanism / limit, with the gap between a physiological effect and a reported experience made explicit.

**W10 grew by ~530 words** plus three exercises: "Judging with the eyes" (Tsay's sight-over-sound experiments, with the later qualifications noted) and "The concert as a visual event" (staging, lighting, relay screens, and film/game sound).

### Overlap (§5)

- **Auditory scene analysis** now has a single home in **W4**, with a new section covering simultaneous and sequential grouping, streaming, and the continuity illusion, plus a runnable demo (an A–B–A gallop at two frequency separations, and a tone interrupted by silence versus noise) and an exercise. W6 and W7 cross-reference it instead of re-introducing it; W7's section is now "Streams in musical textures" and applies the principles to polyphony, orchestration, and the limits of automatic transcription.
- **Timbre** is defined once, in W4. W5 and W7 now open by pointing there.
- **The auditory pathway** is traced once. W11 picks the signal up at the auditory nerve rather than restarting at the outer ear.
- W4's illusions and W7's are now distinguished explicitly (mechanisms of hearing versus illusions that need scales and intervals).

### Defects (§6)

All fixed and verified in a full `myst build --html --execute`:

1. W4 now covers tonotopic organisation (in the cochlea section) and streaming/continuity, so its exam questions match the chapter.
2. W11 now gives the mirror-neuron caveats its question asks about: thin direct human evidence, activation ≠ understanding, and the size of the leap to musical empathy.
3. The eight dangling footnotes in W6 are gone. MyST does not resolve footnote definitions placed in a different notebook cell from the reference, so the sources are now real citations against `references.bib`, with six new entries added (Nymoen 2017, Câmara et al. 2020, Villing 2010, Manilow et al. 2020, Vickhoff et al. 2013, Tsay 2013).
4. The two nested `` ``` `` fences are converted to `:::` — the "Reflect:" paragraph in W6's exercise 6 is now inside the exercise box, and both stray empty code blocks are gone.
5. Bone-conduction bullet emphasis balanced.
6. Swing ratio set as $R = (m+d)/(m-d)$.
7. `text-align:centre` and `:align: centre` fixed; both acoustics formulas converted from raw HTML to LaTeX maths.
8. Heading and chapter-title case normalised to sentence case ("8. The body", "11. The brain", "12. Machine listening", and the machine-listening and vision section headings). Remaining capitals are proper nouns.
9. The stray `description:` frontmatter removed from W7.
10. Acoustics now opens at `##` like every other chapter.
11. W7 restructured: `## Timbre, texture, and musical streams` and `## Analysing music yourself` replace six sections that were nested under `## Melody`.
12. `references.bib` is now used: 15 citations across W1, W2, W3, W6, W8, W9, W10 render through `{cite}`, so each page carries a real reference list.
13. Physiology and The brain now have "Explore interactively" blocks.

### Numbers afterwards

| Wk | Chapter | Words (before → after) | Exercises | Dropdowns | Citations |
|---:|---|---|---:|---:|---:|
| 1 | Tuning in | 4176 → 4183 | 3 | – | 4 |
| 2 | Listening | 3836 → 3836 | 3 | – | 2 |
| 3 | Acoustics | 5358 → 5337 | 5 | 2 | 1 |
| 4 | Psychoacoustics | 4705 → 5301 | 7 | – | – |
| 5 | Electroacoustics | 5019 → 5140 | 3 | 2 | – |
| 6 | Time and rhythm | 4102 → 4337 | 4 (+3 optional) | 2 | 7 |
| 7 | Harmony and melody | 3859 → 3912 | 3 (+3 optional) | – | – |
| 8 | The body | 4704 → 4716 | 3 | – | 4 |
| 9 | Physiology | 3023 → 3344 | 3 | – | 2 |
| 10 | Vision | 2679 → 3209 | 3 | – | 3 |
| 11 | The brain | 4635 → 4840 | 2 | – | – |
| 12 | Machine listening | 4988 → 5532 | 2 | 3 | – |

Length spread narrowed from 2679–5358 to 3209–5532. Every week now carries at least two exercises, and no week carries more than four required ones.
