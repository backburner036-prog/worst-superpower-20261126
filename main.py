#!/usr/bin/env python3
"""Worst Superpower - make.fun entry.

Writes the one-line entry to /output/entry.txt (pure stdlib).
"""

import os

ENTRY = "I can fly three centimetres off the ground, but only downhill."

MAX_CHARS = 140


def validate(text: str) -> None:
    """Gate: single line, 1-140 chars, not whitespace-only."""
    if not text or text != text.strip() or "\n" in text or "\r" in text:
        raise ValueError("entry must be one non-blank line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry too long: {len(text)} > {MAX_CHARS}")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
