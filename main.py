"""Entry for make.fun news-image-20261121.

Copies the pre-rendered front-page image (entry.png, in this repository)
to the output path as entry.png. Standard library only, no network.
Deterministic: the output bytes are always identical to entry.png.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    if not os.path.isfile(SOURCE):
        raise FileNotFoundError("entry.png missing next to main.py: " + SOURCE)
    shutil.copyfile(SOURCE, dest)
    # Byte-identical copy: verify the output matches the source exactly.
    if os.path.getsize(dest) != os.path.getsize(SOURCE):
        raise RuntimeError("output size mismatch for entry.png")


if __name__ == "__main__":
    main()
