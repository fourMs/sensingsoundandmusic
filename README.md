# Sensing Sound and Music

[![Deploy Jupyter Book](https://github.com/fourMs/sensingsoundandmusic/actions/workflows/deploy.yml/badge.svg)](https://github.com/fourMs/sensingsoundandmusic/actions/workflows/deploy.yml)
[![Link check](https://github.com/fourMs/sensingsoundandmusic/actions/workflows/linkcheck.yml/badge.svg)](https://github.com/fourMs/sensingsoundandmusic/actions/workflows/linkcheck.yml)
[![Accessibility](https://github.com/fourMs/sensingsoundandmusic/actions/workflows/accessibility.yml/badge.svg)](https://github.com/fourMs/sensingsoundandmusic/actions/workflows/accessibility.yml)

This is the source code for the e-book [Sensing Sound and Music](https://fourms.github.io/sensingsoundandmusic/), the lecture notes for the course [MUS2640](https://www.uio.no/studier/emner/hf/imv/MUS2640/) at the University of Oslo. The course introduces music students to basic concepts in music psychology and music technology, and the book aims to bridge these two often separated literatures.

The book is written with [Jupyter Book](https://jupyterbook.org/) and combines text, inline code, figures, and a set of small WebAudio apps for interactive examples. Since teaching is ongoing, the material changes based on things that happen in class, student questions, and so on.

## Run locally

    cd book
    jupyter book start

See the [wiki](https://github.com/fourMs/sensingsoundandmusic/wiki) for full build instructions, CI checks, and git hooks.

## Licence

The text, figures and audio of the book are licensed under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) (`LICENSE`). The code, that is the web apps in `book/apps/`, the notebook cells and the scripts in `scripts/` and `tools/`, is licensed under the [GNU General Public License, version 3 or later](https://www.gnu.org/licenses/gpl-3.0.html) (`LICENSE-CODE`), since the video visualiser derives from [VideoViz](https://github.com/alexarje/videoviz), which is GPL-3.0. Audio recordings by others keep their own licences, stated where they are used.

## Credits

The following people have been part of teaching the course and have contributed material: Alexander Refsum Jensenius, Guilherme Schmidt Camara, Sara D'Amario, Laura Bishop, Bilge Serdar, Jinyue Guo, Anna-Maria Christodoulou.

AI support by Claude, Cursor, CoPilot, NotebookLM, Gemini.
