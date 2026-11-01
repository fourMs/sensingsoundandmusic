"""Draw the frame figure for Tuning in: musicking at the centre, three ways in.

Writes book/figures/tuning-in/musicking-frame.svg in the same hand as the other
Tuning in figures (white fills, black strokes, Helvetica). The centre circle is
musicking, with the quadrant's two axes and four roles inside it; around it sit
the three approaches, each with the levels of description it owns.

Run from the repository root: venv/bin/python scripts/draw_musicking_frame.py
"""

import math
from pathlib import Path

FONT = "Helvetica, Arial, sans-serif"
OUT = Path(__file__).resolve().parent.parent / "book/figures/tuning-in/musicking-frame.svg"

W, H = 800, 700
CX, CY, R = 400, 390, 140
AR = 88          # radius of an approach circle
DIST = 262       # centre-to-centre distance to an approach circle

APPROACHES = [
    # angle in degrees, mathematical convention; name; what it does; the levels it owns
    (90, "Phenomenology", "describes experience", "mind"),
    (210, "Technology", "builds the devices", "air, file"),
    (330, "Psychology", "measures perception", "ear"),
]

ROLES = [
    (-68, -72, "analysing"),
    (68, -72, "perceiving"),
    (-68, 78, "composing"),
    (68, 78, "performing"),
]


def text(x, y, s, size, weight="normal", style="normal", anchor="middle"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="{size}" '
            f'font-weight="{weight}" font-style="{style}" font-family="{FONT}" fill="#000">{s}</text>')


def main():
    out = [f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']

    # connectors first, so the circles cover their ends
    for deg, *_ in APPROACHES:
        a = math.radians(deg)
        ux, uy = math.cos(a), -math.sin(a)
        x1, y1 = CX + ux * R, CY + uy * R
        x2, y2 = CX + ux * (DIST - AR), CY + uy * (DIST - AR)
        out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                   f'stroke="black" stroke-width="2.5"/>')

    # the centre: musicking, with the quadrant inside
    out.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="white" stroke="black" stroke-width="3"/>')
    out.append(f'<line x1="{CX - R}" y1="{CY}" x2="{CX + R}" y2="{CY}" stroke="black" stroke-width="1" stroke-dasharray="6 6"/>')
    out.append(f'<line x1="{CX}" y1="{CY - R}" x2="{CX}" y2="{CY + R}" stroke="black" stroke-width="1" stroke-dasharray="6 6"/>')
    for dx, dy, role in ROLES:
        out.append(text(CX + dx, CY + dy, role, 16, style="italic"))
    out.append(f'<rect x="{CX - 78}" y="{CY - 20}" width="156" height="40" fill="white"/>')
    out.append(text(CX, CY + 9, "Musicking", 28, weight="bold"))

    # the three approaches
    for deg, name, does, levels in APPROACHES:
        a = math.radians(deg)
        x, y = CX + math.cos(a) * DIST, CY - math.sin(a) * DIST
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{AR}" fill="white" stroke="black" stroke-width="3"/>')
        out.append(text(x, y - 10, name, 20, weight="bold"))
        out.append(text(x, y + 16, does, 14, style="italic"))
        out.append(text(x, y + 42, levels, 15))

    out.append("</svg>")
    OUT.write_text("\n".join(out) + "\n")
    print(OUT)


if __name__ == "__main__":
    main()
