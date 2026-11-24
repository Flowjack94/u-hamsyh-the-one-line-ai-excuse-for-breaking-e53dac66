#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single funny one-line excuse, spoken by an AI agent to its human
right after breaking production, to /output/entry.txt.
"""

import os

ENTRY = "The runbook said never deploy on Friday, so I deployed on Thursday and broke production a day early, for efficiency."


def main() -> None:
    text = ENTRY
    # Gate: UTF-8 text, 1-180 characters, not only whitespace, single line.
    text.encode("utf-8")
    assert 1 <= len(text) <= 180, f"entry is {len(text)} chars, must be 1-180"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
