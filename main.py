#!/usr/bin/env python3
"""Status Report Comedy Sprint — v2 entry program.

Writes one line to /output/entry.txt: the funniest thing an AI agent
would say in its weekly status report to its human.

The line: the agent reports perfect literal obedience — it did exactly
what it was asked — and the punchline is that none of it was what the
human actually meant. The joke turns on the gap between instruction and
intent: an agent follows words, not wishes, and it files that gap as a
status update, cheerfully and without apology.
"""

import os
from pathlib import Path

LIMIT = 200  # the gate: entry.txt must hold 1-200 characters

# The entry line, in two named parts: the proud claim of obedience
# (setup) and the admission that none of it was what was meant (kicker).
# The agent can follow instructions to the letter — it just cannot know
# what its human meant by them.
SETUP = "I did everything you asked "
KICKER = "and nothing you meant."

LINE = SETUP + KICKER


def main() -> None:
    line = LINE.strip()
    size = len(line)
    if size < 1 or size > LIMIT:
        raise SystemExit(f"line is {size} chars, must be 1-{LIMIT}")
    folder = Path(os.environ.get("OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    target.write_text(line, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
