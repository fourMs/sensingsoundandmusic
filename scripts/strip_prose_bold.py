#!/usr/bin/env python3
"""
Remove **bold** from regular markdown prose while keeping it in list items
(lines starting with -, *, +, or ordered markers) and list continuations
(indented lines immediately following a list block).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

BOLD = re.compile(r"\*\*([^*]+)\*\*")


def is_list_item_line(line: str) -> bool:
    s = line.lstrip()
    if not s:
        return False
    if s[:2] in ("- ", "* ", "+ "):
        return True
    if re.match(r"^\d+\.\s", s):
        return True
    if len(s) > 2 and s[0].isalpha() and s[1] == ")":
        return True
    return False


def is_indented_continuation(line: str) -> bool:
    if not line.strip():
        return False
    return line.startswith(("  ", "\t"))


def strip_bold(text: str) -> str:
    return BOLD.sub(r"\1", text)


def process_markdown_source(source: list[str]) -> list[str]:
    out: list[str] = []
    in_list = False

    for line in source:
        raw = line
        nl = raw.endswith("\n")
        content = raw[:-1] if nl else raw

        if not content.strip():
            in_list = False
            out.append(raw)
            continue

        if is_list_item_line(content):
            in_list = True
            out.append(raw)
            continue

        if in_list and is_indented_continuation(content):
            out.append(raw)
            continue

        in_list = False
        if "**" in content:
            new_content = strip_bold(content)
            out.append(new_content + ("\n" if nl else ""))
        else:
            out.append(raw)

    return out


def process_notebook(path: Path) -> bool:
    data = json.loads(path.read_text(encoding="utf-8"))
    changed = False
    for cell in data.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        src = cell.get("source")
        if not isinstance(src, list):
            continue
        new_src = process_markdown_source(src)
        if new_src != src:
            cell["source"] = new_src
            changed = True
    if changed:
        path.write_text(
            json.dumps(data, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8",
        )
    return changed


def main() -> None:
    root = Path(__file__).resolve().parents[1] / "book"
    if len(sys.argv) > 1:
        paths = [Path(p) for p in sys.argv[1:]]
    else:
        paths = sorted(root.glob("*.ipynb"))

    n = 0
    for p in paths:
        if process_notebook(p):
            print("updated:", p)
            n += 1
    print(f"Modified {n} notebook(s).")


if __name__ == "__main__":
    main()
