"""Entry generator: Everyday Things, Two Lines, Longer Run.

Writes a two-line explanation of a traffic jam for a 10-year-old to
$MAKEFUN_OUTPUT_DIR/entry.txt.

REVISION (25 Nov 2026, resubmit sweep fase 1, playbook
~/workspace/makefun/winner-study-20261125.md checklist 7B).
Old entry (253 chars, toaster as a tiny sun): FAILED the judge brief's
own criterion 3 -- line 1 held TWO comparisons (toaster ~ tiny sun
AND bread browning ~ skin browning at the beach), while the brief
forbids "a second metaphor crowding it"; and criterion 2 (surprising,
"a way the reader has not met before") -- toaster=sun is the first
analogy anyone reaches for. No resolved competition of this exact
type exists in the winner study, so the brief itself + the nearest
type pattern (concrete + surprising + specific) were used.
Old entry passed: on-subject, line 2 honest and specific (timer and
spring), generic-noun test. 2 fails = revise.

New entry (246 chars, 2 lines, 1 sentence each):
  L1: "A traffic jam is like a herd of metal cows that all decided
      to nap on the same road at once."
  L2: "The herd part maps the slow shuffle and the bumper-to-bumper
      crowd, but it leaves out the traffic lights and the one
      broken-down car that started it all."
Checklist 7B on the new entry:
  - Gate: 246 chars, 1-400; exactly 2 lines, one sentence each.
  - Line 1 holds ONE analogy only (herd of cows); "nap" is part of
    that one picture, not a second comparison -- criterion 3 passes.
  - Surprising: metal cows napping on a road is not the canonical
    traffic-jam analogy -- criterion 2 passes.
  - Line 2 is honest and specific: maps 2 (slow shuffle,
    bumper-to-bumper crowd), leaves out 2 (traffic lights, the one
    broken-down car) -- criterion 4 passes.
  - Generic-noun test: replace cows / road / traffic lights /
    broken-down car with generics and the entry collapses -- details
    are load-bearing (>=3). Pair works as a pair, language a
    10-year-old follows.

Drafts considered (all 2 lines, 1 sentence each, gate 1-400):
  D1 (CHOSEN, 246): traffic jam / herd of metal cows, above.
  D2 (228): "Rain is like the clouds wringing out one giant grey
    sponge over the whole town." / "The sponge part maps the squeeze
    that lets the water out, but it leaves out the wind that pushes
    the clouds along and the cold that makes each drop." -- strong,
    but rain=sponge is a familiar kids' analogy, less surprising
    than D1's cows.
  D3 (247): "A queue is like a human train where every carriage has
    to wait for the one in front to move." / "The train part maps
    the single-file order and the slow shuffle forward, but it leaves
    out the tickets and the timetable that tell you where you are
    going." -- solid, but the train analogy is the obvious one for
    a queue, less surprising than D1.

Gate (competition.yaml): /output/entry.txt, UTF-8, 1-400 characters,
not whitespace only. Line 1 explains one everyday thing (a traffic
jam) to a 10-year-old in a single concrete, surprising analogy
sentence. Line 2 is one honest, specific sentence about why the
analogy works: what it maps and what it leaves out.

Deterministic, stdlib only. The output file holds exactly the two
lines joined by one newline and no trailing newline: 246 characters,
246 bytes.
"""

import os
import sys
from pathlib import Path

ENTRY_LINES = (
    "A traffic jam is like a herd of metal cows that all decided to "
    "nap on the same road at once.",
    "The herd part maps the slow shuffle and the bumper-to-bumper "
    "crowd, but it leaves out the traffic lights and the one "
    "broken-down car that started it all.",
)

MIN_CHARS = 1
MAX_CHARS = 400


def ensure_two_lines(text: str) -> list[str]:
    """Return exactly the two non-empty lines of the entry text."""
    lines = [line for line in text.split("\n") if line.strip()]
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly 2 lines, got {len(lines)}")
    return lines


def validate_entry(text: str) -> list[str]:
    """Check the gate: 1-400 chars, exactly 2 lines, one sentence each."""
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(text)}"
        )
    lines = ensure_two_lines(text)
    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped != line:
            raise ValueError(f"line {i} has leading/trailing whitespace")
        # One complete sentence: exactly one sentence-ending full stop,
        # at the end, and no second sentence inside the line.
        if not stripped.endswith("."):
            raise ValueError(f"line {i} must end with a full stop")
        if stripped.count(".") != 1:
            raise ValueError(f"line {i} must be a single sentence")
    return lines


def build_entry() -> str:
    """Join the two entry lines with a single newline, no trailing one."""
    return "\n".join(ENTRY_LINES)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    text = build_entry()
    validate_entry(text)
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
