#!/usr/bin/env bash
# Render every LilyPond source in this folder to a cropped SVG with the same
# basename, then pad all SVGs to one common width so that the book scales them
# identically and the notation and text keep the same size across figures.
set -euo pipefail
cd "$(dirname "$0")"
for f in *.ly; do
  b="${f%.ly}"
  lilypond -s -dbackend=svg -dcrop -o "$b" "$f"
  mv "$b.cropped.svg" "$b.svg"
  rm -f "$b.cropped.png" "$b.png" "$b.pdf"
done
python3 - <<'PY'
import re, glob
files = {}
for f in sorted(glob.glob("*.svg")):
    s = open(f).read()
    head = re.search(r"<svg[^>]*>", s).group(0)
    files[f] = (s, head, float(re.search(r'width="([\d.]+)mm"', head).group(1)))
WIDTH_MM = max(w for _, _, w in files.values())
for f, (s, head, w) in files.items():
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', head).group(1).split()]
    scale = vb[2] / w                      # viewBox units per mm
    m = 1.5                                # margin in viewBox units, about 2.5 mm
    vb = [vb[0] - m, vb[1] - m, WIDTH_MM * scale + 2 * m, vb[3] + 2 * m]
    new = re.sub(r'width="[\d.]+mm"', 'width="%.2fmm"' % (vb[2] / scale), head)
    new = re.sub(r'height="[\d.]+mm"', 'height="%.2fmm"' % (vb[3] / scale), new)
    new = re.sub(r'viewBox="[^"]+"', 'viewBox="%.4f %.4f %.4f %.4f"' % tuple(vb), new)
    open(f, "w").write(s.replace(head, new, 1))
    print(f"{f}: padded from {w:.1f} mm to {WIDTH_MM:.0f} mm")
PY
