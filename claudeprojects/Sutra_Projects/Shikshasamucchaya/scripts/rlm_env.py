#!/usr/bin/env python3
"""
RLM-style environment helper.
Loads large texts as an external "prompt" and provides programmatic access
to slices, lines, and searches without loading everything into an LLM context.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _info(text: str, path: Path) -> None:
    lines = text.count("\n") + 1 if text else 0
    print(f"path: {path}")
    print(f"bytes: {path.stat().st_size}")
    print(f"chars: {len(text)}")
    print(f"lines: {lines}")


def _peek(text: str, start: int, end: int) -> None:
    start = max(0, start)
    end = max(start, end)
    print(text[start:end])


def _lines(text: str, start: int, end: int) -> None:
    all_lines = text.splitlines()
    start = max(1, start)
    end = max(start, end)
    for i in range(start - 1, min(end, len(all_lines))):
        print(f"{i + 1}:{all_lines[i]}")


def _search(text: str, pattern: str, context: int) -> None:
    regex = re.compile(pattern)
    lines = text.splitlines()
    for idx, line in enumerate(lines, start=1):
        if regex.search(line):
            start = max(1, idx - context)
            end = min(len(lines), idx + context)
            for i in range(start - 1, end):
                print(f"{i + 1}:{lines[i]}")
            print("-" * 40)


def _chunk(text: str, size: int, index: int) -> None:
    if size <= 0:
        raise ValueError("size must be > 0")
    start = size * index
    end = start + size
    print(text[start:end])


def main() -> int:
    parser = argparse.ArgumentParser(description="RLM environment helper")
    parser.add_argument("file", type=Path)
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    subparsers.add_parser("info")

    peek_p = subparsers.add_parser("peek")
    peek_p.add_argument("--start", type=int, required=True)
    peek_p.add_argument("--end", type=int, required=True)

    lines_p = subparsers.add_parser("lines")
    lines_p.add_argument("--start", type=int, required=True)
    lines_p.add_argument("--end", type=int, required=True)

    search_p = subparsers.add_parser("search")
    search_p.add_argument("--pattern", required=True)
    search_p.add_argument("--context", type=int, default=2)

    chunk_p = subparsers.add_parser("chunk")
    chunk_p.add_argument("--size", type=int, required=True)
    chunk_p.add_argument("--index", type=int, required=True)

    args = parser.parse_args()
    if not args.file.exists():
        print(f"file not found: {args.file}", file=sys.stderr)
        return 2

    text = _read_text(args.file)
    if args.cmd == "info":
        _info(text, args.file)
    elif args.cmd == "peek":
        _peek(text, args.start, args.end)
    elif args.cmd == "lines":
        _lines(text, args.start, args.end)
    elif args.cmd == "search":
        _search(text, args.pattern, args.context)
    elif args.cmd == "chunk":
        _chunk(text, args.size, args.index)
    else:
        print(f"unknown command: {args.cmd}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
