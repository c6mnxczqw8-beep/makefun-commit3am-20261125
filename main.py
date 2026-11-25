#!/usr/bin/env python3
"""Entry program for The 3 AM Commit Message.

Writes one commit message (at most 200 characters) to the
output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt: what an AI agent commits right after breaking
production at 3 AM. It is a revert of a revert of a fix.
"""

import os

LINE = (
    "fix: production is down because I deployed at 3 "
    "AM; this commit is the incident report, the apology, "
    "and the resignation draft"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
