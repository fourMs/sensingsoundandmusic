"""Small helper for scripted edits of the book notebooks.

Loads a notebook, applies exact-string replacements to markdown cells with an
assertion for every replacement, and writes the file back in the same JSON
format nbformat uses (indent 1, trailing newline).
"""
import json
import os

BOOK = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "book")


class Notebook:
    def __init__(self, name):
        self.path = os.path.join(BOOK, name if name.endswith(".ipynb") else name + ".ipynb")
        with open(self.path) as fh:
            self.nb = json.load(fh)
        self.changes = 0

    @property
    def cells(self):
        return self.nb["cells"]

    @staticmethod
    def text(cell):
        s = cell["source"]
        return "".join(s) if isinstance(s, list) else s

    @staticmethod
    def set_text(cell, text):
        if isinstance(cell["source"], list):
            lines = text.split("\n")
            cell["source"] = [l + "\n" for l in lines[:-1]] + [lines[-1]]
        else:
            cell["source"] = text

    def find(self, needle, kind="markdown"):
        """Index of the single cell containing needle."""
        hits = [i for i, c in enumerate(self.cells)
                if c["cell_type"] == kind and needle in self.text(c)]
        assert len(hits) == 1, f"{self.path}: {len(hits)} cells contain {needle!r}"
        return hits[0]

    def replace(self, old, new, count=1):
        """Replace old with new across markdown cells; assert it happened count times."""
        n = 0
        for c in self.cells:
            if c["cell_type"] != "markdown":
                continue
            t = self.text(c)
            if old in t:
                n += t.count(old)
                self.set_text(c, t.replace(old, new))
        assert n == count, f"{self.path}: replaced {n} times, expected {count}: {old[:70]!r}"
        self.changes += n

    def insert(self, index, text, kind="markdown"):
        cell = {"cell_type": kind, "metadata": {}, "source": ""}
        if kind == "code":
            cell["outputs"] = []
            cell["execution_count"] = None
            cell["metadata"] = {"tags": ["hide-input"]}
        self.set_text(cell, text)
        self.cells.insert(index, cell)
        self.changes += 1

    def save(self):
        with open(self.path, "w") as fh:
            json.dump(self.nb, fh, indent=1, ensure_ascii=False)
            fh.write("\n")
        print(f"{os.path.basename(self.path)}: {self.changes} change(s)")
