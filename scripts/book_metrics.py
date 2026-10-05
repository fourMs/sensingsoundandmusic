#!/usr/bin/env python3
"""Words, readability, and content density per chapter (run: venv/bin/python scripts/book_metrics.py).

Counts only the prose of markdown cells: code cells, code blocks, directives, HTML,
link targets, citation keys, and admonition fences are stripped first. Readability is
LIX (sentence length plus the share of words over six letters, the measure used in
Scandinavian schools) and the Flesch reading ease and Flesch-Kincaid grade (which need
syllables, estimated by vowel groups, so treat them as rough). Content density counts
glossary headwords, citations, figures, exercises, apps, and dropdowns per chapter.
"""
import json
import re
import sys
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent / "book"
CHAPTERS = ["intro", "tuning-in", "listening", "acoustics", "electroacoustics", "psychoacoustics",
            "time-and-rhythm", "harmony-and-melody", "the-body", "physiology", "vision", "the-brain",
            "machine-listening", "general-comments"]


def prose(nb):
    """The readable text of a notebook's markdown cells, with markup removed."""
    out = []
    for cell in nb["cells"]:
        if cell["cell_type"] != "markdown":
            continue
        s = "".join(cell["source"]) if isinstance(cell["source"], list) else cell["source"]
        s = re.sub(r"^---\n.*?\n---\n", "", s, flags=re.S)                      # front matter
        s = re.sub(r"```\{(image|mermaid)\}.*?```|```mermaid.*?```", "", s, flags=re.S)
        s = re.sub(r"<iframe.*?</iframe>|<[^>]+>", "", s, flags=re.S)
        s = re.sub(r"\{cite:?[pt]?\}`[^`]+`", "", s)
        s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)                          # keep link text
        s = re.sub(r"^(```\{[^\n]*|:::\{[^\n]*|:::|```|:class:[^\n]*|:label:[^\n]*|:alt:[^\n]*|:width:[^\n]*)$", "", s, flags=re.M)
        s = re.sub(r"^#+ ", "", s, flags=re.M)
        s = re.sub(r"[*_`]+", "", s)
        s = re.sub(r"&mdash;|&ndash;", ", ", s)
        out.append(s)
    return "\n".join(out)


def syllables(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    groups = len(re.findall(r"[aeiouy]+", w))
    if w.endswith("e") and not w.endswith("le") and groups > 1:
        groups -= 1
    return max(1, groups)


def readability(text):
    text = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", text, flags=re.M)              # list items count as sentences
    text = re.sub(r"\n{2,}", ". ", text)
    sentences = [s for s in re.split(r"(?<=[.!?:])\s+(?=[A-Z\"“(])", text) if len(s.split()) > 1]
    words = [w for w in re.findall(r"[A-Za-z][A-Za-z'’-]*", text)]
    n_s, n_w = max(1, len(sentences)), max(1, len(words))
    long_words = sum(1 for w in words if len(w) > 6)
    syl = sum(syllables(w) for w in words)
    lix = n_w / n_s + 100 * long_words / n_w
    flesch = 206.835 - 1.015 * n_w / n_s - 84.6 * syl / n_w
    grade = 0.39 * n_w / n_s + 11.8 * syl / n_w - 15.59
    return dict(sentences=n_s, mean_sentence=n_w / n_s, long_share=100 * long_words / n_w,
                lix=lix, flesch=flesch, grade=grade)


def glossary_terms():
    s = (BOOK / "glossary.md").read_text(encoding="utf-8")
    body = s[s.index("```{glossary}") + 13:s.rindex("```")]
    return [m.group(1).strip() for m in re.finditer(r"^(\S[^\n]*)\n: ", body, re.M)]


def content(nb, raw_text, terms):
    cells = nb["cells"]
    md = [("".join(c["source"]) if isinstance(c["source"], list) else c["source"]) for c in cells if c["cell_type"] == "markdown"]
    joined = "\n".join(md)
    code_figs = sum(1 for c in cells if c["cell_type"] == "code" and any(o.get("output_type") == "display_data" for o in c.get("outputs", [])))
    low = raw_text.lower()
    def forms(t):
        m = re.match(r"(.*?)\s*\(([^)]+)\)$", t)                                  # "Heart rate variability (HRV)"
        return [m.group(1), m.group(2)] if m else [t]
    present = [t for t in terms if any(re.search(r"\b" + re.escape(f.lower()).replace("\\-", "[-\u2013 ]") + r"s?\b", low) for f in forms(t))]
    return dict(cites=len(re.findall(r"\{cite:?[pt]?\}", joined)), figures=code_figs + joined.count("```{image}") + joined.count("```{mermaid}") + joined.count("```mermaid"),
                exercises=joined.count("{exercise}"), apps=len(set(re.findall(r"apps/([a-z0-9-]+)/", joined))),
                dropdowns=joined.count(":class: dropdown"), questions=len(re.findall(r"^\d+\. ", joined[joined.find("{admonition} Questions"):] if "{admonition} Questions" in joined else "", re.M)),
                terms=present)


def main():
    terms = glossary_terms()
    rows, seen = [], set()
    all_text = []
    for name in CHAPTERS:
        nb = json.loads((BOOK / f"{name}.ipynb").read_text(encoding="utf-8"))
        text = prose(nb)
        all_text.append(text)
        r = readability(text)
        c = content(nb, text, terms)
        new_terms = [t for t in c["terms"] if t not in seen]
        seen.update(c["terms"])
        words = len(re.findall(r"[A-Za-z][A-Za-z'’-]*|\d[\d.,%]*", text))
        rows.append(dict(chapter=name, words=words, minutes=words / 230, **r, **{k: v for k, v in c.items() if k != "terms"},
                         terms_used=len(c["terms"]), terms_new=len(new_terms), terms_per_k=1000 * len(c["terms"]) / max(1, words)))
    total = "\n".join(all_text)
    tw = len(re.findall(r"[A-Za-z][A-Za-z'’-]*|\d[\d.,%]*", total))
    tr = readability(total)
    head = f"{'chapter':20s} {'words':>6s} {'min':>4s} {'sent':>5s} {'long%':>5s} {'LIX':>4s} {'Flesch':>6s} {'grade':>5s} | {'cites':>5s} {'figs':>4s} {'exer':>4s} {'apps':>4s} {'drop':>4s} {'Q':>2s} | {'terms':>5s} {'new':>4s} {'/1k':>4s}"
    print(head); print("-" * len(head))
    for r in rows:
        print(f"{r['chapter']:20s} {r['words']:6d} {r['minutes']:4.0f} {r['mean_sentence']:5.1f} {r['long_share']:5.1f} {r['lix']:4.0f} {r['flesch']:6.0f} {r['grade']:5.1f} | "
              f"{r['cites']:5d} {r['figures']:4d} {r['exercises']:4d} {r['apps']:4d} {r['dropdowns']:4d} {r['questions']:2d} | {r['terms_used']:5d} {r['terms_new']:4d} {r['terms_per_k']:4.0f}")
    print("-" * len(head))
    print(f"{'whole book':20s} {tw:6d} {tw / 230:4.0f} {tr['mean_sentence']:5.1f} {tr['long_share']:5.1f} {tr['lix']:4.0f} {tr['flesch']:6.0f} {tr['grade']:5.1f} | "
          f"{sum(r['cites'] for r in rows):5d} {sum(r['figures'] for r in rows):4d} {sum(r['exercises'] for r in rows):4d} {sum(r['apps'] for r in rows):4d} {sum(r['dropdowns'] for r in rows):4d} {sum(r['questions'] for r in rows):2d} | {len(seen):5d} {'':4s} {'':4s}")
    print(f"\nglossary: {len(terms)} terms, {len(seen)} of them found in a chapter, {len(terms) - len(seen)} not found: {', '.join(t for t in terms if t not in seen)[:400]}")
    if "--json" in sys.argv:
        print(json.dumps(rows, indent=1))


if __name__ == "__main__":
    main()
