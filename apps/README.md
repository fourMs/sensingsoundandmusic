# Bundled web apps

Self-contained, browser-based apps written for the book, one folder per app
with a single `index.html` (inline CSS and JavaScript, no external requests).
They are described one by one in `README-content.md`. The first of them, the
video visualiser, was adapted from VideoViz (https://github.com/alexarje/videoviz,
GPL-3.0), which was vendored here until October 2026.

These apps are copied into the deployed site under `/apps/` by the build
(see `.github/workflows/deploy.yml` and `scripts/verify-book-build.sh`).
