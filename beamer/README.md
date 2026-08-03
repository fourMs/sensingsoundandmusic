# MUS2640 Beamer lecture decks

One PDF deck per teaching week (12 weeks), aligned with the book’s chapter order in `book/myst.yml` and the weekly matrix in `book/intro.ipynb` (Introduction). Each deck is an overview for a two-hour session. Adjust the depth with live demos, audio examples, and discussion.

| File | Book chapter |
|------|----------------|
| `week01-tuning-in.tex` | Tuning in |
| `week02-listening.tex` | Listening |
| `week03-acoustics.tex` | Acoustics |
| `week04-psychoacoustics.tex` | Psychoacoustics |
| `week05-electroacoustics.tex` | Electroacoustics |
| `week06-time-and-rhythm.tex` | Time and rhythm |
| `week07-harmony-and-melody.tex` | Harmony and melody |
| `week08-the-body.tex` | The body |
| `week09-physiology.tex` | Physiology |
| `week10-vision.tex` | Vision |
| `week11-the-brain.tex` | The brain |
| `week12-machine-listening.tex` | Machine listening |

Shared setup is in `beamersettings.tex` (theme, fonts, macros).

## Build

From this directory, with a LaTeX installation (`latexmk` recommended):

```bash
cd beamer
latexmk -pdf week01-tuning-in.tex
# or build all PDFs:
for f in week*.tex; do latexmk -pdf "$f"; done
```

Or twice with `pdflatex`:

```bash
pdflatex -interaction=nonstopmode week01-tuning-in.tex
pdflatex -interaction=nonstopmode week01-tuning-in.tex
```

PDFs are written alongside the `.tex` files.

## Customisation

- Edit `beamersettings.tex` to change theme/colours (`\usetheme`, `\usecolortheme`).
- Add institution logo: `\logo{\includegraphics[height=8mm]{path.pdf}}` in `beamersettings.tex`.
- Weekly slide counts are modest on purpose. Expand them with your own examples and chapter figures.

Introductory material from `book/intro.ipynb` is folded into the Week 1 slides; add a separate opening session if you dedicate the first meeting only to syllabus.
