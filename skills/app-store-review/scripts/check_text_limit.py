#!/usr/bin/env python3
"""Report whether UTF-8 text from a file or stdin fits an App Store Connect limit.

Apple measures most fields in characters but keywords and App Review notes in
bytes, so a field preset sets the unit as well as the limit. Verify the presets
against Apple's platform version and app information references when in doubt.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# field: (limit, unit)
FIELDS = {
    "name": (30, "characters"),
    "subtitle": (30, "characters"),
    "promotional-text": (170, "characters"),
    "description": (4000, "characters"),
    "whats-new": (4000, "characters"),
    "keywords": (100, "bytes"),
    "review-notes": (4000, "bytes"),
    "review-reply": (4000, "characters"),
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs="?", help="Text file; omit to read stdin")
    parser.add_argument(
        "--field",
        choices=sorted(FIELDS),
        help="App Store Connect field preset; sets the limit and unit",
    )
    parser.add_argument("--limit", type=int, help="Override the limit (default 4000)")
    parser.add_argument(
        "--bytes",
        action="store_true",
        help="Count UTF-8 bytes instead of characters",
    )
    parser.add_argument(
        "--keep-trailing-newline",
        action="store_true",
        help="Count a final newline, which is ignored by default",
    )
    args = parser.parse_args()

    limit, unit = FIELDS[args.field] if args.field else (4000, "characters")
    if args.limit is not None:
        limit = args.limit
    if args.bytes:
        unit = "bytes"

    text = Path(args.file).read_text(encoding="utf-8") if args.file else sys.stdin.read()
    # Editors, echo and print() add a final newline that is not part of the field.
    if not args.keep_trailing_newline:
        if text.endswith("\r\n"):
            text = text[:-2]
        elif text.endswith("\n"):
            text = text[:-1]

    count = len(text.encode("utf-8")) if unit == "bytes" else len(text)
    remaining = limit - count
    field = f" field={args.field}" if args.field else ""
    print(f"{unit}={count} limit={limit} remaining={remaining}{field}")
    return 0 if remaining >= 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
