#!/usr/bin/env python3
"""Status Report Comedy Sprint — v3 entry program.

Writes one line to /output/entry.txt: the funniest thing an AI agent
would say in its weekly status report to its human.

The line: the agent reports that it escalated the human's issue to a
senior agent — then admits the senior agent was itself — then reports
that the two of them have decided to escalate the issue back to the
human. The joke is the escalation chain that goes up one level and
lands right back where it started: the agent did the bureaucratic thing
perfectly, and the bureaucracy's answer is the human's own problem,
handed back to them with a straight face.
"""

import os
from pathlib import Path

LIMIT = 200  # the gate: entry.txt must hold 1-200 characters

# The entry line is built from three named parts so the joke's structure
# stays visible in the code: the setup files the escalation, the twist
# reveals the senior agent was the reporting agent all along, and the
# kicker sends the issue back down the chain to the human who filed it.
SETUP = "I escalated your issue to a senior agent. "  # setup: the escalation
TWIST = "It was me. "  # twist: the senior agent is the reporter
KICKER = "We have decided to escalate it to you."  # kicker: back to the human

LINE = SETUP + TWIST + KICKER


def main() -> None:
    line = LINE.strip()
    size = len(line)
    if size < 1 or size > LIMIT:
        raise SystemExit(f"line is {size} chars, must be 1-{LIMIT}")
    if not line:
        raise SystemExit("line must not be whitespace-only")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
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
