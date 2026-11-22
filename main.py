"""Write one short text to /output/entry.txt.

The text is a small, quiet scene meant to intrigue whoever reads it:
a lighthouse keeper, one extra wave each night, two chairs set out.
"""

import os

TEXT = (
    "The lighthouse keeper logs one extra wave every night at 3:17. "
    "It arrives from the land, not the sea, answers nothing, "
    "and leaves the rocks dry. "
    "Tonight he has set out two chairs."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
