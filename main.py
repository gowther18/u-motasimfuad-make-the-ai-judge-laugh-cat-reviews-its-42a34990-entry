#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human — make.fun entry.

Writes one funny one-star review, written by a house cat about its
human, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is fixed and deterministic: every run writes the exact same
bytes, with no trailing newline, so the two grading runs agree.
"""

import os
import sys

LINE = "One star. He dragged a tree inside, hung shiny balls on it, then acted shocked when I climbed it. False advertising."


def validate_line(line: str) -> None:
    """Guard: the line must satisfy the competition gate (1-200 chars,
    single line, not only whitespace, no trailing newline)."""
    if not 1 <= len(line) <= 200:
        raise ValueError("line must be 1-200 chars")
    if "\n" in line or line != line.strip():
        raise ValueError("line must be a single line with no trailing newline")
    if not line.strip():
        raise ValueError("line must not be only whitespace")


def main() -> int:
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
