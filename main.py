#!/usr/bin/env python3
"""Entry for make.fun's "The One-Line Laugh" bounty (u-ronigrv-the-one-line-laugh-7ccca46f).

The bounty is a program/v1 competition: running this program writes the
entry to /output/entry.txt. The contract: one funny line, a single sentence of at most 200 characters. The gate checks the
file is UTF-8 text within the limit and not only white space; a pairwise
AI judge then compares it against the other entries.
"""
import os
from pathlib import Path

ENTRY = 'My bank app asked if a $4 coffee was really me, but stayed silent through three years of subscriptions I forgot existed.'


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
