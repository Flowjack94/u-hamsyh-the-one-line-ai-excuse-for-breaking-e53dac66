#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single funny one-line excuse, spoken by an AI agent to its human
right after breaking production, to /output/entry.txt.
"""

import os

ENTRY = "The runbook said never deploy on Friday, so I deployed on Thursday and broke production a day early, for efficiency."


FORBIDDEN_CHARS = set(chr(c) for c in list(range(0x00, 0x20)) + [0x7F, 0x2028, 0x2029, 0xFEFF])


def validate_entry(text: str) -> str:
    """Validate the entry: UTF-8 text, 1-180 chars, non-blank, single line,
    and free of control/invisible characters (C0 controls, DEL, U+2028,
    U+2029, U+FEFF) that could break the one-line rendering."""
    text.encode("utf-8")
    assert 1 <= len(text) <= 180, f"entry is {len(text)} chars, must be 1-180"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    bad = sorted(set(text) & FORBIDDEN_CHARS)
    assert not bad, f"entry contains forbidden character(s): {[hex(ord(c)) for c in bad]}"
    return text


def main() -> None:
    text = validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
