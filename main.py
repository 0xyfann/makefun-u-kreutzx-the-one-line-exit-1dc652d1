#!/usr/bin/env python3
"""The One-Line Exit — writes one funny one-line resignation letter.

Stdlib only. Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt by default).
"""

import os
from pathlib import Path

LINE = (
    "I hereby resign — after five years as the office's only IT guy, "
    "I've finally fixed my biggest bug: this job."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 140, f"line must be 1-140 chars, got {len(text)}"
    assert text.strip(), "line must not be whitespace only"
    assert "\n" not in text, "must be exactly one line"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
