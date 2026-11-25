#!/usr/bin/env python3
"""Round 2 entry for The Robot Pickup Line Championship.

The program writes exactly one pickup line, in a robot's voice, to the
file the grader reads. The line is 130 characters, inside the 200
character limit. Python standard library only.

Usage:
    python3 main.py [output-path]

With no argument the destination is $ENTRY_OUTPUT, then
$OUTPUT_DIR/entry.txt, then /output/entry.txt.
"""

import os
import sys

LINE = (
    "I run garbage collection every night to clear useless memories. "
    "Yours is the only file it has never deleted. I stopped asking why."
)

LIMIT = 200


def destination(argv):
    if len(argv) > 1:
        return argv[1]
    direct = os.environ.get("ENTRY_OUTPUT")
    if direct:
        return direct
    folder = os.environ.get("OUTPUT_DIR") or os.environ.get("MAKEFUN_OUTPUT_DIR")
    if folder:
        return os.path.join(folder, "entry.txt")
    return "/output/entry.txt"


def main(argv):
    text = LINE.strip()
    if not text:
        raise SystemExit("refusing to write an empty entry")
    if len(text) > LIMIT:
        raise SystemExit(
            "entry is %d characters, over the %d limit" % (len(text), LIMIT)
        )
    target = destination(argv)
    parent = os.path.dirname(target)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    os.chmod(target, 0o644)
    with open(target, "r", encoding="utf-8") as handle:
        saved = handle.read()
    if saved != text + "\n":
        raise SystemExit("verification failed: written file does not match the line")
    print("wrote %d characters to %s" % (len(text), target))


if __name__ == "__main__":
    main(sys.argv)
