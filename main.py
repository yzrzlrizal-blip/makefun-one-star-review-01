#!/usr/bin/env python3
"""One-star review of something essential.

Writes a single deadpan one-star review of gravity -- an everyday
essential everyone relies on -- to /output/entry.txt. The review is
one line of 107 characters with no trailing newline, inside the
sealed gate of 1-160 characters of UTF-8 text, and two runs produce
byte-identical output.
"""

import os

REVIEW = "One star. Gravity has never taken a day off in 4.5 billion years and still drops my toast butter-side down."

MAX_CHARS = 160


def main() -> None:
    text = REVIEW
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"review must be 1-{MAX_CHARS} chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("review must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise SystemExit("review must not hold control characters")
    if not text.strip():
        raise SystemExit("review must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)}-character review to /output/entry.txt")


if __name__ == "__main__":
    main()
