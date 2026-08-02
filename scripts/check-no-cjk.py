#!/usr/bin/env python3
"""Fail if any literal CJK character appears in the toolkit's source surface.

The toolkit is English-only. Functional Chinese values (API parameters,
scraper markers) are kept as ASCII \\uXXXX escapes in source, so any literal
CJK glyph in the paths below is a regression. Historical research output
under reports/ and data/ is exempt.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TARGETS = [
    'skills',
    'codex-skills',
    'codex-prompts',
    'tools',
    'scripts',
    'docs',
    'CLAUDE.md',
    'AGENTS.md',
    'README.md',
    'ai_CLAUDE.md',
]

EXTS = ('.md', '.py', '.sh', '.yaml', '.yml', '.json', '.txt', '.toml')

# Han ideographs, CJK punctuation, and full-width forms
CJK_RANGES = (
    (0x4E00, 0x9FFF),   # CJK Unified Ideographs
    (0x3400, 0x4DBF),   # Extension A
    (0xF900, 0xFAFF),   # Compatibility Ideographs
    (0x3000, 0x303F),   # CJK punctuation
    (0xFF01, 0xFF5E),   # Full-width forms
)


def is_cjk(ch: str) -> bool:
    cp = ord(ch)
    return any(lo <= cp <= hi for lo, hi in CJK_RANGES)


def iter_files():
    for target in TARGETS:
        path = ROOT / target
        if path.is_file():
            yield path
        elif path.is_dir():
            for f in sorted(path.rglob('*')):
                if f.is_file() and f.suffix in EXTS:
                    yield f


def main() -> int:
    total = 0
    for f in iter_files():
        try:
            text = f.read_text(encoding='utf-8')
        except (UnicodeDecodeError, OSError):
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            hits = [ch for ch in line if is_cjk(ch)]
            if hits:
                total += len(hits)
                rel = f.relative_to(ROOT)
                sample = ''.join(hits[:10])
                print(f'{rel}:{lineno}: {len(hits)} CJK char(s): {sample}')
    if total:
        print(f'\nFAIL: {total} CJK character(s) found in the toolkit surface.')
        return 1
    print('OK: toolkit surface is CJK-free.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
