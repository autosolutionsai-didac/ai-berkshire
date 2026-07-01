#!/usr/bin/env python3
"""Report Audit Tool for AI Berkshire.

Data spot-check tool: extracts 15% of the financial data points from a research
report, compares them against reliable sources, releases the report if they pass,
or sends it back with reasons if they fail.

Zero external dependencies — uses only Python stdlib.
Requires Python >= 3.7.

Workflow (three steps):
  Step 1 — Extract data points, randomly sample 15%:
    python3 tools/report_audit.py extract --report reports/xxx.md

  Step 2 — For each data point in the audit checklist, Claude fetches values from
            reliable sources (macrotrends/stockanalysis/aastocks/eastmoney) and
            fills them into fetched_value

  Step 3 — Feed in the verification results and output the release/send-back verdict:
    python3 tools/report_audit.py verdict --results '[...]'

  One-step (extract + print the audit checklist only, no network verification):
    python3 tools/report_audit.py extract --report reports/xxx.md --dry-run
"""

import argparse
import json
import math
import os
import re
import sys
from decimal import Decimal, Context, ROUND_HALF_EVEN
from random import Random

_CTX = Context(prec=28, rounding=ROUND_HALF_EVEN)

# ---------------------------------------------------------------------------
# Data point extraction: identify financial numbers in a Markdown report
# ---------------------------------------------------------------------------

# Match pattern: number + unit, preceded by a context label
# e.g.: revenue 1,239 (100M), PE 18.8x, gross margin 56%, market cap ~$5,670 (100M)
# NOTE: CJK code points below are written as \uXXXX escapes so the source stays
# ASCII-only while the compiled patterns still match Chinese report content.
_PATTERNS = [
    # percentage
    (r'([\d,\uff0c\.]+)\s*%',                              '%',        'percent'),
    # 100M CNY / 100M USD / 100M HKD
    (r'([\d,\uff0c\.]+)\s*\u4ebf(\u5143|\u7f8e\u5143|\u6e2f\u5143|RMB|USD|HKD)?', '\u4ebf', 'hundred_million'),
    # multiples PE/PB/PS
    (r'([\d,\uff0c\.]+)\s*[xX\u500d]',                     'x',        'multiple'),
    # trillion
    (r'([\d,\uff0c\.]+)\s*\u4e07\u4ebf',                   '\u4e07\u4ebf', 'trillion'),
    # absolute USD value (B/T)
    (r'\$\s*([\d,\uff0c\.]+)\s*([BMT\u4ebf])',             '$',        'usd_abs'),
    # plain integers (e.g. market cap, revenue, user counts) appearing in tables between | |
    (r'\|\s*[~\u7ea6]?\$?([\d,\uff0c\.]+)\s*\|',           '',         'table_num'),
]

_LABEL_RE = re.compile(
    r'(?P<label>[^\|\n\uff1a:]{2,25})[\uff1a:\s]+[~\u7ea6]?\$?(?P<num>[\d,\uff0c\.]+)\s*(?P<unit>\u4ebf[\u5143\u7f8e\u6e2f]?\u5143?|\u4e07\u4ebf|[xX\u500d]|%|[BMT])?'
)

_TABLE_ROW_RE = re.compile(
    r'\|\s*(?P<label>[^|]{1,40})\s*\|\s*[~\u7ea6]?\$?(?P<num>[\d,\uff0c\.]+)\s*(?P<unit>\u4ebf[\u5143\u7f8e\u6e2f]?\u5143?|\u4e07\u4ebf|[xX\u500d]|%|[BMT])?\s*\|'
)


def _clean_num(s: str) -> float:
    """Convert a number string with commas or fullwidth commas to float."""
    s = s.replace(',', '').replace('\uff0c', '').strip()
    try:
        return float(s)
    except ValueError:
        return None


def _is_valid_label(label: str) -> bool:
    """Decide whether a label is a meaningful financial field name; filter out noise."""
    label = label.strip()
    # too short
    if len(label) < 2:
        return False
    # pure number or pure year/quarter
    if re.fullmatch(r'[\d\s\u5e74\u5b63\u5ea6Q]+', label):
        return False
    # starts with a symbol / markdown marker
    if re.match(r'^[+\-\*#\|~\$>_`]', label):
        return False
    # contains markdown bold / code markers
    if '**' in label or '`' in label or '__' in label:
        return False
    # label is a pure growth-rate token (e.g. +56%, -13% alone as a label)
    if re.fullmatch(r'[+\-]?\d+(\.\d+)?%', label):
        return False
    # common meaningless labels (Chinese entries kept as \uXXXX so they still match
    # report content): sources / source / note / caution / remark / data source /
    # subtotal / unit / trend
    _SKIP = {'\u6765\u6e90', 'sources', 'source', '\u8bf4\u660e', '\u6ce8\u610f',
             '\u5907\u6ce8', '\u6570\u636e\u6765\u6e90', 'n/a', '—', '-', '/',
             '\u5408\u8ba1', 'total', '\u5355\u4f4d', '\u8d8b\u52bf'}
    if label.lower() in _SKIP:
        return False
    return True


# Two-column table row: | label | value unit | (designed for KV tables in financial reports)
_KV_TABLE_RE = re.compile(
    r'^\|\s*(?P<label>[^|*\n]{2,40}?)\s*\|\s*[~\u7ea6]?\$?(?P<num>[\d,\uff0c\.]+)\s*'
    r'(?P<unit>\u4ebf[\u5143\u7f8e\u6e2f]?\u5143?|\u4e07\u4ebf|[xX\u500d]|%|[BMT\u4ebf])?\s*[\|\uff08\(]'
)

# Labeled KV line: label: value unit
_KV_LABEL_RE = re.compile(
    r'(?P<label>[\u4e00-\u9fa5A-Za-z][^\|\n\uff1a:*]{1,30})[\uff1a:]\s*[~\u7ea6]?\$?'
    r'(?P<num>[\d,\uff0c\.]+)\s*(?P<unit>\u4ebf[\u5143\u7f8e\u6e2f]?\u5143?|\u4e07\u4ebf|[xX\u500d]|%|[BMT])?'
)


def _parse_md_tables(lines: list) -> list:
    """Parse all tables in the Markdown; return a list of (row_label, col_header, value, unit, lineno, raw)."""
    results = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # detect header row (contains | and is not a separator row)
        if '|' in line and not re.match(r'^\|[\-\s\|:]+\|$', line):
            headers_raw = [h.strip().strip('*_').strip() for h in line.split('|')]
            headers_raw = [h for h in headers_raw if h]
            # the next line should be a separator row
            if i + 1 < len(lines) and re.match(r'^\|[\-\s\|:]+\|$', lines[i+1].strip()):
                i += 2  # skip the separator row
                # read data rows
                while i < len(lines):
                    dline = lines[i].strip()
                    if not dline or not dline.startswith('|'):
                        break
                    cells = [c.strip().strip('*_~').strip() for c in dline.split('|')]
                    cells = [c for c in cells if c != '']
                    if len(cells) < 2:
                        i += 1
                        continue
                    row_label = cells[0]
                    for col_idx, cell in enumerate(cells[1:], start=1):
                        col_header = headers_raw[col_idx] if col_idx < len(headers_raw) else f'col{col_idx}'
                        # extract number + unit from the cell
                        m = re.search(
                            r'[~\u7ea6]?\$?([\d,\uff0c\.]+)\s*(\u4ebf[\u5143\u7f8e\u6e2f]?\u5143?|\u4e07\u4ebf|[xX\u500d]|%|[BMT])?',
                            cell
                        )
                        if m:
                            val = _clean_num(m.group(1))
                            unit = (m.group(2) or '').strip()
                            if val and val != 0 and val < 1e15:
                                results.append((row_label, col_header, val, unit, i + 1, dline))
                    i += 1
                continue
        i += 1
    return results


def extract_data_points(md_text: str) -> list:
    """Extract all recognizable financial data points from a Markdown report.

    Covers three structures:
      1. Multi-column Markdown tables (the primary source): (row label + column header) -> value
      2. KV lines with a colon: label: value unit
      3. Bold number lines: **value** unit

    Returns a list of dict:
      {id, label, reported_value, unit, raw_text, line_number}
    """
    points = []
    seen = set()

    def _add(label, val, unit, lineno, raw):
        label = re.sub(r'[\*_`]+', '', label).strip()
        if not _is_valid_label(label):
            return
        if val is None or val == 0 or val > 1e15:
            return
        # filter out pure years / quarters
        if re.fullmatch(r'(20\d{2}|Q[1-4]|\d{4}\s*Q[1-4])', label.strip()):
            return
        key = f"{label}|{round(val,4)}|{unit}"
        if key in seen:
            return
        seen.add(key)
        points.append({
            'id': len(points) + 1,
            'label': label,
            'reported_value': val,
            'unit': unit,
            'raw_text': raw[:120],
            'line_number': lineno,
        })

    lines = md_text.split('\n')
    in_code = False

    # --- 1. Multi-column tables ---
    for row_label, col_header, val, unit, lineno, raw in _parse_md_tables(lines):
        # skip meaningless row labels
        if not _is_valid_label(row_label):
            continue
        # skip meaningless column headers (YoY growth columns are annotations, not data
        # to verify); Chinese values kept as \uXXXX so they still match report headers:
        # growth / YoY / change / trend / note / remark
        if col_header.upper() in ('YOY', 'YOY\u589e\u901f', '\u589e\u901f',
                                  '\u540c\u6bd4', '\u53d8\u5316', '\u8d8b\u52bf',
                                  '\u8bf4\u660e', '\u5907\u6ce8'):
            continue
        # label = "row_label · col_header" (if the column header supplements the row label)
        if col_header and col_header != row_label:
            label = f"{row_label} · {col_header}"
        else:
            label = row_label
        _add(label, val, unit, lineno, raw)

    # --- 2. KV colon lines ---
    for lineno, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith('```'):
            in_code = not in_code
            continue
        if in_code or stripped.startswith('> ') or re.match(r'^#{1,6}\s', stripped):
            continue
        if '|' in stripped:
            continue  # tables already handled above

        for m in _KV_LABEL_RE.finditer(stripped):
            label = m.group('label')
            val = _clean_num(m.group('num'))
            unit = (m.group('unit') or '').strip()
            _add(label, val, unit, lineno, stripped)

    return points


def sample_points(points: list, ratio: float = 0.15, seed: int = None) -> list:
    """Randomly sample a `ratio` fraction of data points, at least 3 and at most 30."""
    n = max(3, min(30, math.ceil(len(points) * ratio)))
    n = min(n, len(points))
    rng = Random(seed)
    sampled = rng.sample(points, n)
    # sort by line number for easier manual comparison
    return sorted(sampled, key=lambda p: p['line_number'])


# ---------------------------------------------------------------------------
# Release / send-back verdict
# ---------------------------------------------------------------------------

_TOLERANCE = 0.01   # 1% tolerance


def _pct_diff(reported: float, fetched: float) -> float:
    """Relative deviation (absolute value)."""
    if reported == 0:
        return 0.0 if fetched == 0 else float('inf')
    return abs(reported - fetched) / abs(reported)


def render_verdict(results: list, report_name: str = "") -> dict:
    """
    Output the release/send-back verdict based on verification results.

    results: list of dict, each item contains:
      - id, label, reported_value, unit, fetched_value, fetched_source
      - (optional) fetched_value2, fetched_source2   <- second source

    Returns:
      {
        'verdict': 'PASS' | 'FAIL',
        'pass_count': int,
        'fail_count': int,
        'total': int,
        'fail_items': [...],
        'summary': str,
      }
    """
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

    print('=' * 70)
    print(f'{BOLD}Report Data Audit — Release/Send-Back Verdict{RESET}')
    if report_name:
        print(f'Report: {report_name}')
    print('=' * 70)
    print()

    fail_items = []
    warn_items = []

    for item in results:
        label = item.get('label', '?')
        reported = float(item.get('reported_value', 0))
        unit = item.get('unit', '')
        fetched = item.get('fetched_value')
        source = item.get('fetched_source', '?')
        fetched2 = item.get('fetched_value2')
        source2 = item.get('fetched_source2', '')

        # --- Compare against primary source ---
        if fetched is None:
            # no verification value provided -> skip (not counted as pass/fail)
            print(f'  ⬜ [{item["id"]:>2}] {label[:35]:35s} {reported:>12.2f} {unit}  →  [no verification value provided, skipped]')
            continue

        fetched = float(fetched)
        diff1 = _pct_diff(reported, fetched)

        # --- Compare against second source (if any) ---
        diff2 = None
        if fetched2 is not None:
            fetched2 = float(fetched2)
            diff2 = _pct_diff(reported, fetched2)

        # decide
        pass1 = diff1 <= _TOLERANCE
        pass2 = (diff2 is None) or (diff2 <= _TOLERANCE)

        if pass1 and pass2:
            status = f'{GREEN}✅ PASS{RESET}'
            detail = f'{source}: {fetched:.2f} (deviation {diff1*100:.2f}%)'
            if diff2 is not None:
                detail += f'  |  {source2}: {fetched2:.2f} (deviation {diff2*100:.2f}%)'
        elif not pass1 and not pass2:
            status = f'{RED}❌ FAIL{RESET}'
            detail = f'{source}: {fetched:.2f} (deviation {diff1*100:.2f}%)'
            if diff2 is not None:
                detail += f'  |  {source2}: {fetched2:.2f} (deviation {diff2*100:.2f}%)'
            fail_items.append({
                'id': item['id'],
                'label': label,
                'reported': reported,
                'unit': unit,
                'fetched': fetched,
                'source': source,
                'fetched2': fetched2,
                'source2': source2,
                'diff1_pct': round(diff1 * 100, 2),
                'diff2_pct': round(diff2 * 100, 2) if diff2 is not None else None,
                'raw_text': item.get('raw_text', ''),
                'line_number': item.get('line_number', 0),
            })
        else:
            # one source passes and one fails -> warning, not counted as a failure
            status = f'{YELLOW}⚠️  WARN{RESET}'
            detail = f'{source}: {fetched:.2f} (deviation {diff1*100:.2f}%)'
            if diff2 is not None:
                detail += f'  |  {source2}: {fetched2:.2f} (deviation {diff2*100:.2f}%)'
            warn_items.append({
                'id': item['id'], 'label': label,
                'reported': reported, 'unit': unit,
                'diff1_pct': round(diff1 * 100, 2),
                'diff2_pct': round(diff2 * 100, 2) if diff2 is not None else None,
            })

        print(f'  {status} [{item["id"]:>2}] {label[:35]:35s}  Reported: {reported:>12.2f} {unit}')
        print(f'              {" " * 38}{detail}')

    print()
    print('-' * 70)

    total = len([r for r in results if r.get('fetched_value') is not None])
    fail_count = len(fail_items)
    warn_count = len(warn_items)
    pass_count = total - fail_count - warn_count

    print(f'  Audited total: {total}  |  Pass: {GREEN}{pass_count}{RESET}  |  Warn: {YELLOW}{warn_count}{RESET}  |  Fail: {RED}{fail_count}{RESET}')
    print()

    if fail_count == 0:
        print(f'{BOLD}{GREEN}[RELEASE] All audited data points passed; the report may be published.{RESET}')
        verdict = 'PASS'
    else:
        print(f'{BOLD}{RED}[SEND BACK] {fail_count} data point(s) failed verification; the report must be corrected and re-audited.{RESET}')
        print()
        print(f'{BOLD}Send-back reasons:{RESET}')
        for fi in fail_items:
            print(f'  ❌ Line {fi["line_number"]} | {fi["label"]}')
            print(f'     Reported value: {fi["reported"]} {fi["unit"]}')
            print(f'     {fi["source"]}: {fi["fetched"]}  (deviation {fi["diff1_pct"]}%)')
            if fi.get('fetched2') is not None:
                print(f'     {fi["source2"]}: {fi["fetched2"]}  (deviation {fi["diff2_pct"]}%)')
            print(f'     Source text: {fi["raw_text"][:80]}')
            print()
        verdict = 'FAIL'

    if warn_count > 0:
        print(f'{YELLOW}Note: {warn_count} data point(s) have inconsistent results across the two sources (over 1%); this may be a definition difference (GAAP/Non-GAAP or exchange rate). Please review manually.{RESET}')
        for wi in warn_items:
            print(f'  ⚠️  {wi["label"]}  Reported: {wi["reported"]} {wi["unit"]}  Deviation: {wi["diff1_pct"]}% / {wi["diff2_pct"]}%')

    print('=' * 70)

    return {
        'verdict': verdict,
        'pass_count': pass_count,
        'warn_count': warn_count,
        'fail_count': fail_count,
        'total': total,
        'fail_items': fail_items,
        'warn_items': warn_items,
    }


# ---------------------------------------------------------------------------
# CLI Entry Point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='Report Audit Tool — research report data audit tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Workflow:

  Step 1 — Extract data points, randomly sample 15%, and print the audit checklist:
    python3 tools/report_audit.py extract --report reports/tencent/tencent-research-20260408.md

  Step 2 — For each data point in the checklist, Claude fetches values from reliable
            sources and fills in fetched_value / fetched_source / fetched_value2 / fetched_source2

  Step 3 — Feed in the verification results and output the release/send-back verdict:
    python3 tools/report_audit.py verdict --results '[
      {"id":1,"label":"Revenue","reported_value":7518,"unit":"100M","fetched_value":7518,"fetched_source":"macrotrends","fetched_value2":7500,"fetched_source2":"stockanalysis"},
      ...
    ]'

  One-step preview (print the audit checklist only, no verification):
    python3 tools/report_audit.py extract --report reports/xxx.md --dry-run

  Specify the sampling ratio (default 0.15):
    python3 tools/report_audit.py extract --report reports/xxx.md --ratio 0.20

  Fix the random seed (reproduce the same sample batch):
    python3 tools/report_audit.py extract --report reports/xxx.md --seed 42
        """)

    sub = parser.add_subparsers(dest='command')

    # extract
    ext = sub.add_parser('extract', help='Extract data points from a report and randomly sample')
    ext.add_argument('--report', required=True, help='Path to the report file (Markdown)')
    ext.add_argument('--ratio', type=float, default=0.15, help='Sampling ratio, default 0.15')
    ext.add_argument('--seed', type=int, default=None, help='Random seed (optional, for reproducibility)')
    ext.add_argument('--dry-run', action='store_true', help='Only print; do not output JSON')

    # verdict
    vrd = sub.add_parser('verdict', help='Output the release/send-back verdict based on verification results')
    vrd.add_argument('--results', required=True, help='JSON array containing fields such as fetched_value')
    vrd.add_argument('--report', default='', help='Report name (optional, for display)')
    vrd.add_argument('--output-json', action='store_true', help='Output the verdict result as JSON to stdout')

    args = parser.parse_args()

    if args.command == 'extract':
        if not os.path.exists(args.report):
            print(f'❌ File does not exist: {args.report}', file=sys.stderr)
            sys.exit(1)

        with open(args.report, 'r', encoding='utf-8') as f:
            text = f.read()

        all_points = extract_data_points(text)
        sampled = sample_points(all_points, ratio=args.ratio, seed=args.seed)

        print('=' * 70)
        print(f'Report Data Audit Checklist')
        print(f'File: {args.report}')
        print(f'Total extracted data points: {len(all_points)}  |  Sampling ratio: {args.ratio:.0%}  |  Audit count: {len(sampled)}')
        if args.seed is not None:
            print(f'Random seed: {args.seed} (can be used to reproduce the same sample batch)')
        print('=' * 70)
        print()
        print(f'{"ID":>3}  {"Line":>5}  {"Label":<35}  {"Reported":>12}  {"Unit"}')
        print(f'{"─"*3}  {"─"*5}  {"─"*35}  {"─"*12}  {"─"*6}')
        for p in sampled:
            print(f'{p["id"]:>3}  {p["line_number"]:>5}  {p["label"][:35]:<35}  {p["reported_value"]:>12.2f}  {p["unit"]}')
        print()
        print('↑ For each data point above, fetch values from the sources below and fill in fetched_value:')
        print('  US stocks: macrotrends.net (primary) + stockanalysis.com (secondary)')
        print('  HK stocks: aastocks.com (primary) + macrotrends ADR (secondary)')
        print('  A-shares: eastmoney.com (primary) + cninfo.com.cn (secondary)')
        print()

        if not args.dry_run:
            # output a fillable JSON template
            template = []
            for p in sampled:
                template.append({
                    'id': p['id'],
                    'label': p['label'],
                    'reported_value': p['reported_value'],
                    'unit': p['unit'],
                    'line_number': p['line_number'],
                    'raw_text': p['raw_text'],
                    'fetched_value': None,       # <- fill in the primary-source verification value
                    'fetched_source': '',        # <- fill in the primary-source name
                    'fetched_value2': None,      # <- fill in the secondary-source verification value (optional)
                    'fetched_source2': '',       # <- fill in the secondary-source name (optional)
                })
            print('Audit checklist JSON (after filling in fetched_value, pass it to the verdict command):')
            print()
            print(json.dumps(template, ensure_ascii=False, indent=2))

    elif args.command == 'verdict':
        try:
            results = json.loads(args.results)
        except json.JSONDecodeError as e:
            print(f'❌ JSON parse failed: {e}', file=sys.stderr)
            sys.exit(1)

        report_name = args.report or ''
        outcome = render_verdict(results, report_name=report_name)

        if args.output_json:
            print(json.dumps(outcome, ensure_ascii=False, indent=2))

        # a non-zero exit code means send-back, convenient for CI/scripts to check
        sys.exit(0 if outcome['verdict'] == 'PASS' else 1)

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
