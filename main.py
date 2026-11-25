"""Two Robots in an Elevator entry.

The brief wants a single line of robot elevator small talk, so the
line opens like a computed decision — thousands of simulations of
the silence — and then collapses into very human awkwardness: a
hesitant remark about both of them just going up and down all day.
That contrast between machine precision and elevator chit-chat is
the whole joke, delivered in one spoken line.

When run, the program stores the line in ``entry.txt`` inside the
selected output directory, with no trailing newline added.
"""

import os
from pathlib import Path

LINE = "I ran 4,000 simulations of this silence and still chose to say it: so, uh, you also just go up and down all day?"

ENTRY_FILENAME = "entry.txt"


def validate_line(line):
    """Reject an entry that is empty or carries a newline."""
    if len(line) == 0:
        raise ValueError("entry line must not be empty")
    if "\n" in line:
        raise ValueError("entry line must not contain a newline")


def write_entry(out_dir):
    """Guard the one-line rule, then persist the entry and return it."""
    validate_line(LINE)
    folder = Path(out_dir)
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / ENTRY_FILENAME
    path.write_text(LINE, encoding="utf-8")
    return path


def resolve_out_dir():
    """Read the output location from MAKEFUN_OUTPUT_DIR if set."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    write_entry(resolve_out_dir())


if __name__ == "__main__":
    main()
