#!/usr/bin/env python3
"""Entry for make.fun's "The One-Line Laugh" bounty
(u-ronigrv-the-one-line-laugh-7ccca46f).

This is a program/v1 competition: running this program writes the entry
to /output/entry.txt. The contract is a single funny line, one sentence
of at most 200 characters — UTF-8 text, not blank. A pairwise AI judge
then scores it against the other entries, so the line has to land on
its own with no setup.

The joke: my banking app interrogates me over a $4 coffee, yet it has
watched money quietly leak into forgotten subscriptions for years
without saying a word.
"""
import os
from pathlib import Path

JOKE = (
    "My banking app flagged a $4 coffee as 'suspicious activity', yet for "
    "three years it said nothing while a meditation app I opened once "
    "quietly billed me $14.99 a month for inner peace."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
