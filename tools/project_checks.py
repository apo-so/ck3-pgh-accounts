"""Shared integrity checks for this repository; no game or private files needed."""
from pathlib import PurePosixPath
import hashlib
import json
import re

REQUIRED_EVIDENCE = {
    'docs/evidence/R72-audit.json',
    'docs/evidence/R74-creation.json',
    'docs/evidence/R74-restoration.json',
    'docs/evidence/R59-payment.json',
    'docs/evidence/R76-static.json',
    'docs/evidence/R76-deployment.json',
}


def checked_manifest(root, relative, required, allowed):
    failures, entries = [], {}
    try:
        data = json.loads((root / relative).read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        return {}, ['Invalid manifest ' + relative + ': ' + str(exc)]
    rows = data.get('files') if isinstance(data, dict) else None
    if not isinstance(rows, list) or not rows:
        return {}, ['Manifest files must be a non-empty list: ' + relative]
    for number, row in enumerate(rows):
        if not isinstance(row, dict):
            failures.append('Invalid manifest row: ' + relative + ':' + str(number))
            continue
        path, digest = row.get('path'), row.get('sha256')
        if not isinstance(path, str):
            failures.append('Manifest path must be a string: ' + relative)
            continue
        pure = PurePosixPath(path)
        if pure.is_absolute() or '..' in pure.parts or '\\' in path or pure.as_posix() != path or not allowed(path):
            failures.append('Invalid manifest path: ' + path)
            continue
        if path in entries:
            failures.append('Duplicate manifest path: ' + path)
            continue
        entries[path] = digest
        if not isinstance(digest, str) or not re.fullmatch(r'[0-9a-fA-F]{64}', digest):
            failures.append('Invalid SHA256: ' + path)
            continue
        target = (root / path).resolve()
        if root not in target.parents:
            failures.append('Manifest path leaves repository: ' + path)
        elif not target.is_file():
            failures.append('Missing manifest file: ' + path)
        elif hashlib.sha256(target.read_bytes()).hexdigest() != digest.lower():
            failures.append('Hash mismatch: ' + path)
    for path in sorted(required - entries.keys()):
        failures.append('Required manifest entry missing: ' + path)
    return entries, failures


def check_source(root):
    entries, failures = checked_manifest(
        root, 'source-manifest.json', {'pgh_accounts.mod', 'pgh_accounts/descriptor.mod'},
        lambda p: p == 'pgh_accounts.mod' or p.startswith('pgh_accounts/'),
    )
    actual = {p.relative_to(root).as_posix() for p in (root / 'pgh_accounts').rglob('*') if p.is_file()}
    expected = {p for p in entries if p.startswith('pgh_accounts/')}
    for path in sorted(actual ^ expected):
        failures.append('Unexpected or missing Mod file: ' + path)
    descriptor = root / 'pgh_accounts.mod'
    if descriptor.is_file():
        try:
            paths = re.findall(r'^\s*path\s*=\s*"([^"\r\n]*)"\s*(?:#.*)?$', descriptor.read_text(encoding='utf-8-sig'), re.MULTILINE)
            if paths != ['mod/pgh_accounts'] or not (root / 'pgh_accounts').is_dir():
                failures.append('External descriptor must contain exactly path="mod/pgh_accounts"')
            internal = root / 'pgh_accounts/descriptor.mod'
            if internal.is_file():
                inside = internal.read_text(encoding='utf-8-sig')
                outside = descriptor.read_text(encoding='utf-8-sig')
                for field in ['name', 'version', 'supported_version', 'remote_file_id']:
                    pattern = r'^\s*' + field + r'\s*=\s*"([^"\r\n]*)"\s*(?:#.*)?$'
                    original = re.findall(pattern, inside, re.MULTILINE)
                    launcher = re.findall(pattern, outside, re.MULTILINE)
                    valid_count = len(original) in (0, 1) if field == 'remote_file_id' else len(original) == 1
                    if launcher != original or not valid_count:
                        failures.append('Descriptor metadata missing, duplicated or inconsistent: ' + field)
        except (OSError, UnicodeError) as exc:
            failures.append('Invalid external descriptor: ' + str(exc))
    return entries, actual, failures


def check_evidence(root):
    entries, failures = checked_manifest(
        root, 'docs/evidence/manifest.json', REQUIRED_EVIDENCE,
        lambda p: p.startswith('docs/evidence/') and p.endswith('.json') and p != 'docs/evidence/manifest.json',
    )
    actual = {p.relative_to(root).as_posix() for p in (root / 'docs/evidence').rglob('*.json') if p.name != 'manifest.json'}
    for path in sorted(actual ^ entries.keys()):
        failures.append('Unlisted or missing historical evidence: ' + path)
    return entries, failures
