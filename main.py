#!/usr/bin/env python3
"""One Line to Your Younger Self — make.fun bounty entry.

Writes one line to your younger self to /output/entry.txt (outDir is the literal "/output", per the kit).
"""

import os

# Written from the future, with love.
ENTRY = "Dear younger me: stop apologizing for taking up space. The rooms that want you small were never built for you anyway."

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main() -> None:
    entry = ENTRY.strip()
    assert entry, "entry must not be empty"
    assert "\n" not in entry, "entry must be a single line"
    assert 1 <= len(entry) <= 200, f"entry must be 1-200 chars, got {len(entry)}"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(entry)
    print(f"Wrote {len(entry)} characters to {OUT_PATH}")


if __name__ == "__main__":
    main()
