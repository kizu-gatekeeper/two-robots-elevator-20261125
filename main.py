#!/usr/bin/env python3
"""Write the one line of robot elevator small talk to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "Two Robots in an Elevator" bounty. The program
writes exactly one line of text and nothing else.

How the line targets the brief: machine logic shows through first --
the robot literally simulated the awkward silence thousands of times --
then the small talk still comes out as the dumbest possible opener,
asked of a machine whose entire existence is going up and down. The
awkwardness is the joke, and it lands on the first read.
"""

import os
from pathlib import Path

LINE = 'I ran 4,000 simulations of this silence and still chose to say it: so, uh, you also just go up and down all day?'

ENTRY_FILENAME = "entry.txt"


def write_entry(out_dir: Path) -> Path:
    """Write the entry line to entry.txt inside out_dir and return its path.

    The file holds exactly the line and nothing else: no trailing newline,
    no extra whitespace, so the gate sees one line within the limit.
    """
    if not LINE or chr(10) in LINE:
        raise ValueError("the entry must be exactly one non-empty line")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / ENTRY_FILENAME
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(out_dir)


if __name__ == "__main__":
    main()
