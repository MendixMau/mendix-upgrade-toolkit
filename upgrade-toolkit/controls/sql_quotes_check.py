#!/usr/bin/env python3
"""sql_quotes_check.py: read generated SQL on stdin and fail when a single-quoted string does not end where it should.

A string that closes and is followed at once by a letter or digit (`'the app'` then `s`) is the shape an apostrophe
inside a string literal makes; a string still open at the end is the other. Line comments (--) outside strings are skipped.
Prints `quotes ok: N string literal(s)` or the line and column of the first fault; exit 0 / 1."""
import sys

def check(text):
    i, n, line, col, count = 0, len(text), 1, 0, 0
    while i < n:
        c = text[i]
        if c == "\n": line += 1; col = 0; i += 1; continue
        if c == "-" and text[i:i + 2] == "--":
            while i < n and text[i] != "\n": i += 1
            continue
        if c == "'":
            sl, sc = line, col; i += 1; col += 1
            while True:
                if i >= n: return f"string opened at line {sl} col {sc} is never closed"
                if text[i] == "'":
                    if text[i + 1:i + 2] == "'": i += 2; col += 2; continue
                    i += 1; col += 1; break
                if text[i] == "\n": line += 1; col = -1
                i += 1; col += 1
            count += 1
            if i < n and (text[i].isalnum() or text[i] == "_"):
                return f"string opened at line {sl} col {sc} closes and is followed by {text[i]!r}: an apostrophe inside a string literal"
            continue
        i += 1; col += 1
    return count

r = check(sys.stdin.read())
if isinstance(r, str): print("QUOTES FAULT: " + r); sys.exit(1)
print(f"quotes ok: {r} string literal(s)")
