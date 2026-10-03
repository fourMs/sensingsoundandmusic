# Bundled web apps

Self-contained, browser-based apps used by the book, vendored here so the book
works offline and as a standalone archive. Each app keeps its own licence.

- `videoviz/` — live webcam video visualisation (videograms, self-similarity
  matrix, motion view). Built on the Musical Gestures Toolbox.
  Source: https://github.com/alexarje/videoviz — Licence: GPL-3.0 (see
  `videoviz/LICENSE`). Used in the chapter *The body*.

These apps are copied into the deployed site under `/apps/` by the build
(see `.github/workflows/deploy.yml` and `scripts/verify-book-build.sh`).
