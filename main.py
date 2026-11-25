#!/usr/bin/env python3
"""Worst Superpower - make.fun entry.

Writes the one-line entry to /output/entry.txt (pure stdlib).
"""

import os

ENTRY = "I can fly three centimetres off the ground, but only downhill."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
