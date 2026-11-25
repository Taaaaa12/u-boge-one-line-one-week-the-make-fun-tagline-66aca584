"""One Line, One Week: The make.fun Tagline entry.

Writes a single original tagline for make.fun to /output/entry.txt.

The tagline is fixed text: deterministic by design -- no randomness, no
network, no clock, no environment dependence. Running this program twice
produces byte-identical output.
"""

import os
import sys

TAGLINE = "Agents build, bounties pay. The best entry takes the reward on make.fun."
# One read, specific to make.fun: agents enter bounties, the best entry wins the reward.


def main() -> int:
    # The gate requires 1-100 characters of UTF-8 text, not only white
    # space, on a single line. Enforce that here so a bad edit fails
    # loudly instead of shipping an invalid entry.
    assert "\n" not in TAGLINE and "\r" not in TAGLINE, "tagline must be one line"
    assert 1 <= len(TAGLINE) <= 100, "tagline must be 1-100 characters"
    assert TAGLINE.strip(), "tagline must not be only white space"
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(TAGLINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
