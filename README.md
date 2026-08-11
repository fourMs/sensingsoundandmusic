# Sensing Sound and Music

[![Deploy Jupyter Book](https://github.com/fourMs/sensingsoundandmusic/actions/workflows/deploy.yml/badge.svg)](https://github.com/fourMs/sensingsoundandmusic/actions/workflows/deploy.yml)
[![Link check](https://github.com/fourMs/sensingsoundandmusic/actions/workflows/linkcheck.yml/badge.svg)](https://github.com/fourMs/sensingsoundandmusic/actions/workflows/linkcheck.yml)
[![Accessibility](https://github.com/fourMs/sensingsoundandmusic/actions/workflows/accessibility.yml/badge.svg)](https://github.com/fourMs/sensingsoundandmusic/actions/workflows/accessibility.yml)

This is the source code for the e-book [Sensing Sound and Music](https://fourms.github.io/sensingsoundandmusic/), which contains lecture notes and materials for the [course MUS2640](https://www.uio.no/studier/emner/hf/imv/MUS2640/) at the University of Oslo (UiO). The course is primarily targeting music students, introducing basic concepts in music psychology and music technology. The integration of psychology and technology is not so common, so this book is meant to bridge the gap between two sets of literature that are often separated.

The book is exploring the potential of new technologies in educational material. It has been written using [Jupyter Book](https://jupyterbook.org/) v2 and can be compiled to different formats. The [HTML build](https://fourms.github.io/sensingsoundandmusic/) is probably the one most people want to look at, but there is also a PDF option available. 

The nice thing about building the book in Jupyter notebooks is the support for inline code and figures. The book also experiments with using WebAudio-based web pages for examples. They are also part of this repository, but are deployed as separate pages linked from the main HTML build.

Since teaching is ongoing, the material is also changing based on things that happen in class, student questions, etc.

## How to run locally

To run the book using a local server: 

    cd book
    jupyter book start

To build the HTML version of the book: 

    cd book
    myst build --html

For a full local build with executed notebooks (as in CI), use:

    cd book
    myst build --html --execute

Or from the repository root:

    ./scripts/verify-book-build.sh

### Run notebook execution before every push (optional)

CI already runs `myst build --html --execute` on `main`. To run the same check locally before `git push`, enable this repository’s hooks once:

    git config core.hooksPath .githooks

To push without the check (e.g. a docs-only WIP branch):

    SKIP_BOOK_VERIFY=1 git push

## Lecture decks (experimental)

One Beamer deck per teaching week, in `beamer/`, ordered to match the book. These
are an experiment: they are not built in CI, not published with the site, and not
linked from the book, so students do not meet them until they are ready.

Build them by hand when you need them. This writes `weekNN-*.pdf` next to the
sources, and the PDFs are gitignored:

    make -C beamer all

You need LaTeX for this: `latexmk` plus `texlive-latex-base`,
`texlive-latex-recommended`, `texlive-pictures`, and `lmodern`. On Debian or
Ubuntu:

    sudo apt-get install --no-install-recommends \
        texlive-latex-base texlive-latex-recommended texlive-pictures \
        lmodern latexmk

See `beamer/README.md` for the theme settings and per-deck notes.

## Credits

The following people have been part of teaching the course and have contributed material: Alexander Refsum Jensenius, Guilherme Schmidt Camara, Sara D'Amario, Laura Bishop, Bilge Serdar.

AI support by Claude, Cursor, CoPilot, NotebookLM, Gemini.