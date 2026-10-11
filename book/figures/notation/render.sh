#!/usr/bin/env bash
# Render every LilyPond source in the given chapter folder to a cropped SVG with
# the same basename, then pad all SVGs there to one common width so that the
# book scales every notation figure identically, in every chapter.
# Usage: figures/notation/render.sh figures/<chapter>/notation
set -euo pipefail
WIDTH_MM=189
cd "$1"
for f in *.ly; do
  b="${f%.ly}"
  lilypond -s -dbackend=svg -dcrop -o "$b" "$f"
  mv "$b.cropped.svg" "$b.svg"
  rm -f "$b.cropped.png" "$b.png" "$b.pdf"
done
WIDTH_MM="$WIDTH_MM" python3 - <<'PY'
import re, glob, os
WIDTH_MM = float(os.environ["WIDTH_MM"])
for f in sorted(glob.glob("*.svg")):
    s = open(f).read()
    head = re.search(r"<svg[^>]*>", s).group(0)
    w = float(re.search(r'width="([\d.]+)mm"', head).group(1))
    if w > WIDTH_MM:
        raise SystemExit(f"{f} is {w:.1f} mm wide, more than the common {WIDTH_MM:.0f} mm")
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', head).group(1).split()]
    scale = vb[2] / w                      # viewBox units per mm
    m = 1.5                                # margin in viewBox units, about 2.5 mm
    vb = [vb[0] - m, vb[1] - m, WIDTH_MM * scale, vb[3] + 2 * m]
    new = re.sub(r'width="[\d.]+mm"', 'width="%.2fmm"' % WIDTH_MM, head)
    new = re.sub(r'height="[\d.]+mm"', 'height="%.2fmm"' % (vb[3] / scale), new)
    new = re.sub(r'viewBox="[^"]+"', 'viewBox="%.4f %.4f %.4f %.4f"' % tuple(vb), new)
    open(f, "w").write(s.replace(head, new, 1))
    print(f"{f}: {w:.1f} mm of content, padded to {WIDTH_MM:.0f} mm")
PY
