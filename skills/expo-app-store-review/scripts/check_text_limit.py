#!/usr/bin/env python3
"""Report whether UTF-8 text from a file or stdin fits a character limit."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs="?", help="Text file; omit to read stdin")
    parser.add_argument("--limit", type=int, default=4000)
    args = parser.parse_args()

    text = Path(args.file).read_text(encoding="utf-8") if args.file else sys.stdin.read()
    count = len(text)
    remaining = args.limit - count
    print(f"characters={count} limit={args.limit} remaining={remaining}")
    return 0 if remaining >= 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
