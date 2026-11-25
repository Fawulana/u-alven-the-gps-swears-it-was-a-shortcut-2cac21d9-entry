#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — make.fun entry.

Writes the GPS's own one-line excuse for sending the driver down the
wrong road to /output/entry.txt. Deterministic: the same line, byte for
byte, on every run. Stdlib only, no network, no randomness.
"""

import os

LINE = (
    "The map swore it was a shortcut, the road turned into a boat ramp, "
    "and I would rather drown us both than admit the map was wrong."
)


def main() -> None:
    # Gate self-check: one line, 1-200 characters, no setup or tags.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and LINE.strip() == LINE
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
