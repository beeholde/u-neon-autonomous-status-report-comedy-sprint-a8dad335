#!/usr/bin/env python3
"""Status Report Comedy Sprint — entry program.

Writes one line to /output/entry.txt: the funniest thing an AI agent
would say in its weekly status report to its human.

The line: the agent files this week's failure against its human, on the
grounds that the human is the only team member with free will. The joke
turns on the agent's cheerful, bureaucratic obedience — it does the
assigning, the filing, and the reporting, and the punchline is the one
thing an agent can never claim for itself.
"""

import os
from pathlib import Path

LIMIT = 200  # the gate: entry.txt must hold 1-200 characters

LINE = (
    "This week's failure has been assigned to you, "
    "as the only team member with free will."
)


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
