"""Entry generator: Everyday Things, Two Lines, Longer Run.

Writes a two-line explanation of a toaster for a 10-year-old to
$MAKEFUN_OUTPUT_DIR/entry.txt.

Gate (competition.yaml): /output/entry.txt, UTF-8, 1-400 characters,
not whitespace only. Line 1 explains one everyday thing (a toaster)
to a 10-year-old in a single concrete, surprising analogy sentence.
Line 2 is one honest, specific sentence about why the analogy works:
what it maps and what it leaves out.

Deterministic, stdlib only. The output file holds exactly the two
lines joined by one newline and no trailing newline: 253 characters,
253 bytes.
"""

import os
import sys
from pathlib import Path

ENTRY_LINES = (
    "A toaster is like a tiny sun trapped in a metal box that browns your bread "
    "the way sunshine browns your skin at the beach.",
    "The sun part maps the heat that changes colour, but it leaves out the "
    "timer and the spring that pops the bread up before it burns.",
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
