# Review — *Sensing Sound and Music* (MUS2640)

A review of the 14-chapter e-book against four goals: remove AI "tells", remove bold inside paragraphs, check consistency/organisation, and assess content and balance for a bachelor audience that is mostly musicology with some psychology and technology students.

## 1. What was edited (done in this pass)

All 14 source notebooks were copy-edited in place (markdown cells only; no code cells touched). Across the book:

- **AI tells removed/rewritten**: gerund subtitles ("Exploring/Understanding…"), boilerplate `description:` frontmatter, filler openers ("It is important to note", "Before delving into"), hype ("fascinating", "powerful", "rich/holistic/nuanced understanding", "plays a crucial role", "essential for several reasons", "preferred choice"), promotional closers ("By adopting these practices…"), empty "not only… but also", and audience-address scaffolding.
- **Bold in running prose removed** (the heaviest cases were the timbre note in *electroacoustics*, the interpretation/ethics block in *physiology*, the ventriloquism/score-notation cells in *vision*, the entrainment cell in *time and rhythm*, and the memory/attention block in *the brain*). The `- **Term**: definition` list-label convention was kept everywhere.
- **Spelling normalised** to British/Oxford −ise/−our (some chapters, notably *harmony and melody*, were American-spelled).
- **Typos/grammar fixed** (e.g. "bulids"→"builds", "instantenous"→"instantaneous", "Sony Rollins"→"Sonny Rollins", "the organization's rhythm"→"the organisation of rhythm", a Varèse sentence fragment in *tuning in*, "auditory phenomenon—orpurely" in *the body*).
- **One duplicate removed**: the Disney *Toot, Whistle, Plunk and Boom* reference appeared in both *acoustics* and *electroacoustics*; kept in *acoustics*.
- **Headings**: many normalised to sentence case (a final consistency sweep is still recommended, see §2).

## 2. Consistency & organisation

Strong points: every chapter follows the same shape (frontmatter → one-line intro linking neighbouring weeks → sections → exercises/admonitions → "Chapter summary" → numbered "Questions"). Numbered titles (1.–12.) are consistent; intro and general-comments are unnumbered, which is fine.

Remaining items to settle:

- **Heading case** — Before this pass, capitalisation was mixed ("Auditory Pathways" vs "Course schedule"). I converted most to sentence case; a final sweep should confirm none are left in Title Case (e.g. a couple flagged in *acoustics* and *vision*).
- **Subtitles** — Decide one policy: either every chapter carries a short noun-phrase subtitle, or none do. Right now some were dropped and some replaced. Pick one for uniformity.
- **AI-authorship disclosure** — The intro's "Embracing AI" section openly states the book is AI co-created. I kept it (reworded) because it is pedagogically intentional, but flag it. If the goal is for the book *not* to read as AI-made, this section is in tension with that. Your call.
- **Cross-chapter overlap** — Auditory streaming, Gestalt grouping, and auditory illusions appear in *psychoacoustics* (W4), *harmony and melody* (W7), and *the brain* (W10). The overlap is defensible but should be deliberately divided (introduce once, cross-reference after) rather than re-explained.

## 3. Balance between weeks

Approximate prose word counts (text only, excluding code/figures):

| Wk | Chapter | Words | Note |
|--:|---|--:|---|
| 1 | Tuning in | 4.7k | on-ramp, fine |
| 2 | Listening | 4.4k | on-ramp, fine |
| 3 | Acoustics | **8.1k** | heaviest + most technical |
| 4 | Psychoacoustics | 7.1k | dense |
| 5 | Electroacoustics | 6.4k | |
| 6 | Time and rhythm | 5.8k | |
| 7 | Harmony and melody | 6.1k | very broad scope |
| 8 | The body | 5.5k | |
| 9 | Physiology | **3.5k** | light |
| 10 | Vision | **2.8k** | lightest |
| 11 | The brain | 5.5k | |
| 12 | Machine listening | 5.7k | |

Observations and recommendations:

- **Difficulty front-loads in weeks 3–4.** Acoustics and psychoacoustics are the two longest and most technical chapters, and they hit musicology-first students earliest. Consider marking the most technical passages (Fourier transform, windowing, JND maths, swing-ratio formula) as optional "dig deeper" boxes so the core narrative stays accessible.
- **Vision (W10) is thin** (~2.8k, roughly a third of acoustics) and spends a disproportionate share on generic eye anatomy. For a music course it would be better balanced by trimming anatomy and adding music-relevant material: conductor/performer gaze, score reading and sight-reading vs memorised performance, ensemble gaze coordination, and how visual staging shapes listening.
- **Physiology (W9) is light** and would benefit from one or two concrete empirical examples (e.g. choir/ensemble cardiac or respiratory synchrony) and a decision on whether the ASMR passage earns its place.
- **Harmony and melody (W7) is the broadest** in topics covered (tones, pitch, CQT, chroma, tonality, cultural frames, statistical learning, harmony, melody, timbre, ASA, Gestalt, illusions, texture). It risks being a mile wide and an inch deep; consider moving ASA/Gestalt/illusions to W4 (psychoacoustics) where they already live, freeing room to go deeper on harmony and melody proper.
- Weeks 1–2 as light introductions are appropriate; no change needed.

## 4. Content suggestions (per chapter)

- **Psychoacoustics (W4)**: end-of-chapter Questions reference "tonotopic organisation" and "continuity/streaming" that the body does not actually cover. Add brief coverage (the intro schedule already promises "streaming") or adjust the questions. **Asset issue**: code cells point at `../audio` and found 0 files, so the saxophone-overtone examples may not render. Verify the audio paths against `book/audio/`.
- **The brain (W11)**: the auditory-pathways section recaps W3–W4 at length, and the artificial-neural-network section sits oddly in a neuroanatomy chapter. Trim the recap to a cross-reference and consider moving the ANN explanation to *machine listening*. One concrete "familiar-melody → hippocampus + auditory cortex" example would help.
- **Machine listening (W12)**: the (already strong) ethics section could name concrete dataset biases (GTZAN genre labels, MAESTRO being piano-only) and add a line on how MIR metrics assume Western tonal music. A short meta-note that this very textbook is AI co-written fits naturally here.
- **General comments**: solid generic study advice; add a few music-specific examples (how to analyse a score in an essay, how to cite a recording or a YouTube performance, keeping pitch/key terminology consistent).
- **Physiology (W9)**: claims are linked to Wikipedia rather than to literature. If the course wants students to read empirical work (per the intro's "Reading empirical research"), a few real citations here would model that.

## 5. Suggested next steps

1. Review the working-tree diff per chapter (deeper voice rewrites are involved, so spot-check meaning).
2. Decide the subtitle policy and the AI-disclosure question (§2).
3. Optionally act on the balance moves: trim vision/physiology imbalance, optional-mark the heavy maths, dedupe ASA/Gestalt across W4/W7.
4. Run `myst build --html --execute` (or `./scripts/verify-book-build.sh`) to confirm everything still executes and the audio examples render.
