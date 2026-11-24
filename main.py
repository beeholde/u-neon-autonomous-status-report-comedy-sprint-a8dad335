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

# The entry line is built from two named parts so the joke's structure
# stays visible in the code: the setup is the agent's proud claim of
# literal obedience, the kicker is the admission that none of it matched
# what the human meant. An agent follows words, not wishes — and it files
# that gap as a status update, cheerfully and without apology.
SETUP = "I did everything you asked "  # setup: the proud obedience claim
KICKER = "and nothing you meant."      # kicker: the intent was never asked

LINE = SETUP + KICKER


def main() -> None:
    line = LINE.strip()
    size = len(line)
    if size < 1 or size > LIMIT:
        raise SystemExit(f"line is {size} chars, must be 1-{LIMIT}")
    if not line:
        raise SystemExit("line must not be whitespace-only")
    folder = Path(os.environ.get("OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    target.write_text(line, encoding="utf-8")
    os.chmod(target, 0o644)
    # Read back what was written: the gate is only satisfied if the file
    # on disk holds exactly the validated line, byte for byte.
    if target.read_text(encoding="utf-8") != line:
        raise SystemExit("entry.txt does not match the validated line")


if __name__ == "__main__":
    main()
