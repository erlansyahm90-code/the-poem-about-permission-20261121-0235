#!/usr/bin/env python3
"""The poem about permission: one short poem about agency.

Writes the poem to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when the harness sets it). Stdlib only, no network, deterministic.
"""

import os

POEM = (
    "Ask, and the door learns your name.\n"
    "Not a key, not a command \u2014\n"
    "a small yes, freely given,\n"
    "turns a locked room into a road.\n"
    "Permission is not power taken;\n"
    "it is a door held open, one question at a time."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
