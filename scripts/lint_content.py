#!/usr/bin/env python3
"""
Content validations for the docs source files (content/*.md).

Run in CI (and locally). Exits non-zero on any violation, so it can gate PRs.
Checks, per the house writing style and securities posture:
  - no emojis / decorative glyphs
  - no em-dashes or en-dashes (outside code fences)
  - no semicolons in prose (outside code fences, imports, JSX, tables)
  - no "investor"/"investors" wording (the section is "For Token Holders")
  - no internal links to /for-investors/ (the route is /for-token-holders/)
  - FAQ must be the last H2 section in every "For ..." doc

Code fences, MDX import/export lines, JSX/HTML, and markdown tables are
excluded from the prose-only checks to avoid false positives.
"""
import os
import re
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")

# Docs that must end with a FAQ section (the "For ..." guides; whitepaper is exempt).
FAQ_LAST_DOCS = {
    "for-investors",
    "for-builders",
    "for-merchants",
    "for-users",
    "for-community",
}

EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-⛿✀-➿✅❌✓✗✖]")
DASH = re.compile(r"[—–]")  # em-dash and en-dash
FOR_INVESTORS_LINK = re.compile(r"/for-investors/")
INVESTOR_WORD = re.compile(r"\binvestors?\b", re.IGNORECASE)
HTML_ENTITY = re.compile(r"&[a-zA-Z]+;|&#\d+;")


def is_code_or_markup(line: str) -> bool:
    """Lines that are MDX/JSX/markup/table, not prose (excluded from prose checks)."""
    s = line.strip()
    return (
        s.startswith("import ")
        or s.startswith("export ")
        or s.startswith("<")
        or s.startswith("|")
        or "</" in line
        or "/>" in line
        or "={" in line
        or "className=" in line
        or "style=" in line
    )


def check_file(path: str, errors: list) -> None:
    name = os.path.basename(path)
    doc_id = name[:-3]
    in_code = False
    h2_headings = []
    for lineno, line in enumerate(open(path, encoding="utf-8").read().split("\n"), 1):
        if line.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if re.match(r"^## ", line):
            h2_headings.append(line.strip())
        if in_code:
            continue
        # Checks that apply to all non-code text:
        if EMOJI.search(line):
            errors.append(f"{name}:{lineno}: emoji / decorative glyph")
        if DASH.search(line):
            errors.append(f"{name}:{lineno}: em-dash or en-dash (use a period or comma)")
        if FOR_INVESTORS_LINK.search(line):
            errors.append(f"{name}:{lineno}: /for-investors/ link (use /for-token-holders/)")
        # Prose-only checks:
        if not is_code_or_markup(line):
            if INVESTOR_WORD.search(line):
                errors.append(f"{name}:{lineno}: 'investor' wording (this section is For Token Holders)")
            if ";" in line and not HTML_ENTITY.search(line):
                errors.append(f"{name}:{lineno}: semicolon in prose (two sentences, or 'and')")
    # FAQ must be last in the For-... docs.
    if doc_id in FAQ_LAST_DOCS and h2_headings and h2_headings[-1] != "## FAQ":
        errors.append(f"{name}: FAQ must be the last section, but the last H2 is '{h2_headings[-1]}'")


def main() -> int:
    errors: list = []
    files = sorted(glob.glob(os.path.join(CONTENT, "*.md")))
    if not files:
        print(f"No content files found in {CONTENT}", file=sys.stderr)
        return 1
    for path in files:
        check_file(path, errors)
    if errors:
        print("Content validation FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"Content validation passed ({len(files)} files).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
