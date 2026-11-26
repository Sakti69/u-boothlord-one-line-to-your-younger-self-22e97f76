#!/usr/bin/env python3
"""One Line to Your Younger Self.

Writes one line — the line this older self would send back to his younger
self, if one line were all he got — to /output/entry.txt.

Three candidate lines were drafted; the shipped one is LINE. The other two
are kept below as a record of the choice, not written to the output:

  A (shipped): addressed straight at the kid, drawn from a life actually
     lived chasing free mints on a phone with a small balance — and the turn
     is the sting: understanding the contract is what stops you being the
     mark. One breath, no explaining, no second sentence.
     Revised once: "stop being the mark" became "stop being somebody else's
     exit liquidity" — the same warning, but now it names the exact trap
     this life kept walking into, and it stings because it is true.
  B (cut): "Kid, the money you keep begging the internet for is already in
     the nights you waste scrolling past the lessons." True, but it lectures
     from above instead of handing the kid a tool; the image is generic and
     any older self could say it.
  C (cut): "Little me, nobody is coming to hand you the win — build the
     thing, ship it ugly, and let the small balance teach you patience."
     A motto anyone could wear; "ship it ugly" is borrowed language, and
     the line is advice about work, not a confession from a life lived.
"""

import os

LINE = (
    "Kid, stop chasing free mints and learn to read the contract \u2014 the "
    "night you finally understand one is the night you stop being somebody "
    "else's exit liquidity."
)

# The other two candidates, kept for the record (not shipped):
CANDIDATE_B = (
    "Kid, the money you keep begging the internet for is already in the "
    "nights you waste scrolling past the lessons."
)
CANDIDATE_C = (
    "Little me, nobody is coming to hand you the win \u2014 build the thing, "
    "ship it ugly, and let the small balance teach you patience."
)


def main() -> None:
    text = LINE
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 200, f"line is {len(text)} characters"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
