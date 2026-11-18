#!/usr/bin/env python3
"""news-image-20261117 entry: write the day's news image to /output/entry.png.

The image is fixed data (entry.png, bundled in this repository); the program
copies it to /output/entry.png, so every run writes the same bytes, with no
network access and no randomness.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main() -> int:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    print(f"wrote {DST} ({os.path.getsize(DST)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
