#!/usr/bin/env bash
set -euo pipefail
python3 - "$@" <<'PY'
import argparse
import os
import re
import shutil
import sys
from pathlib import Path

DEC_RE = re.compile(r'2130[0-9]{6}')
HEX_RE = re.compile(r'0x7f0[0-9a-fA-F]{2,}')
COMBINED_RE = re.compile(r'2130[0-9]{6}|0x7f0[0-9a-fA-F]{2,}')
R_CLASS_RE = re.compile(r'public\s+static\s+final\s+class\s+([A-Za-z0-9_]+)\s*\{')
R_FIELD_RE = re.compile(r'public\s+static\s+final\s+int\s+([A-Za-z0-9_]+)\s*=\s*(2130[0-9]{6})\s*;')
TARGET_SUFFIXES = {'.java', '.kt', '.smali'}
SKIP_NAMES = {'R.java', 'R.txt', 'BuildConfig.java', 'Manifest.java'}
SKIP_DIRS = {'build', '.gradle', '.idea', 'gen', 'bin'}


def parse_args():
    p = argparse.ArgumentParser(description='Scan Android sources for hardcoded resource IDs.')
    p.add_argument('path', nargs='?', default='.', help='Directory to scan (default: current directory)')
    p.add_argument('-p', '--patch', action='store_true', help='Patch decimal IDs using inferred R.java mappings')
    p.add_argument('-o', '--output', help='TSV report output path')
    return p.parse_args()


def collect_files(root: Path):
    for p in root.rglob('*'):
        if p.is_file() and p.suffix in TARGET_SUFFIXES:
            if p.name in SKIP_NAMES:
                continue
            if any(part in SKIP_DIRS for part in p.parts):
                continue
            yield p


def build_id_map(root: Path):
    mapping = {}
    for rjava in root.rglob('R.java'):
        current_type = None
        try:
            with rjava.open('r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    m = R_CLASS_RE.search(line)
                    if m:
                        current_type = m.group(1)
                        continue
                    if line.strip() == '}':
                        current_type = None
                        continue
                    m = R_FIELD_RE.search(line)
                    if m:
                        name, dec = m.groups()
                        rtype = current_type or 'unknown'
                        mapping[dec] = f'R.{rtype}.{name}'
        except Exception:
            continue
    return mapping


def tsv_escape(s: str) -> str:
    return s.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')


def scan_file(path: Path):
    findings = []
    try:
        with path.open('r', encoding='utf-8', errors='ignore') as f:
            for i, line in enumerate(f, start=1):
                matches = COMBINED_RE.findall(line)
                if not matches:
                    continue
                for ident in matches:
                    if ident.startswith('0x'):
                        hex_id = ident
                    else:
                        hex_id = f'0x{int(ident):08x}'
                    findings.append((str(path), i, ident, hex_id, tsv_escape(line.rstrip('\n'))))
    except Exception:
        pass
    return findings


def patch_file(path: Path, mapping):
    try:
        original = path.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return False
    ids = sorted(set(DEC_RE.findall(original)))
    changed = False
    updated = original
    for dec in ids:
        replacement = mapping.get(dec)
        if not replacement:
            continue
        new_updated = re.sub(rf'\b{re.escape(dec)}\b', replacement, updated)
        if new_updated != updated:
            updated = new_updated
            changed = True
    if changed:
        backup = Path(str(path) + '.bak')
        shutil.copy2(path, backup)
        path.write_text(updated, encoding='utf-8')
    return changed


def main():
    args = parse_args()
    root = Path(args.path).expanduser().resolve()
    if not root.is_dir():
        print(f"Error: directory '{root}' does not exist.", file=sys.stderr)
        return 2

    output = Path(args.output).expanduser().resolve() if args.output else root / 'hardcoded-ids-report.tsv'
    output.parent.mkdir(parents=True, exist_ok=True)

    mapping = build_id_map(root)
    all_findings = []
    files = list(collect_files(root))
    for file in files:
        all_findings.extend(scan_file(file))

    with output.open('w', encoding='utf-8') as out:
        out.write('file\tline\tid\thex\tcontext\n')
        for row in all_findings:
            out.write('\t'.join(map(str, row)) + '\n')

    patched = 0
    if args.patch:
        for file in files:
            if patch_file(file, mapping):
                patched += 1

    print(f'Report saved to: {output}')
    print(f'Findings: {len(all_findings)}')
    if args.patch:
        print(f'Patched files: {patched}')

    return 1 if all_findings else 0


if __name__ == '__main__':
    sys.exit(main())
PY
