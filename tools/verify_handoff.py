"""Check a standalone project checkout using only Python's standard library."""
from pathlib import Path
import json
import re
import runpy
from urllib.parse import unquote

root = Path(__file__).resolve().parents[1]
failures = []
required = [
    'README.md', 'AGENTS.md', '接手入口.md', 'status.json',
    'docs/HANDOFF.md', 'docs/NEXT_STEPS.md', 'docs/SOURCE_MAP.md',
    'docs/DEVELOPMENT.md', 'docs/INSTALL.md', 'docs/KNOWN_ISSUES.md',
    'docs/VALIDATION.md', 'docs/evidence/README.md',
    'docs/evidence/manifest.json', 'source-manifest.json',
    'pgh_accounts.mod', 'pgh_accounts/descriptor.mod', 'tools/verify_manifest.py',
    'tools/project_checks.py',
]
for relative in required:
    if not (root / relative).is_file():
        failures.append('Missing file: ' + relative)

def load(relative):
    try:
        data = json.loads((root / relative).read_text(encoding='utf-8'))
        if not isinstance(data, dict):
            raise ValueError('Expected a JSON object')
        return data
    except (OSError, ValueError) as exc:
        failures.append('Invalid JSON: ' + relative + ': ' + str(exc))
        return {}

checks = runpy.run_path(str(root / 'tools/project_checks.py'))
expected, actual, source_failures = checks['check_source'](root)
failures.extend(source_failures)

status = load('status.json')
if status.get('mod_files') != len(actual):
    failures.append('status.json Mod file count differs from actual source')
for key in ['entry', 'handoff', 'next_steps', 'source_map', 'historical_evidence_manifest']:
    if not status.get(key) or not (root / status[key]).is_file():
        failures.append('Invalid status reference: ' + key)

evidence, evidence_failures = checks['check_evidence'](root)
failures.extend(evidence_failures)

links = 0
public_files = [p for p in root.rglob('*') if p.is_file() and '.git' not in p.relative_to(root).parts]
for p in public_files:
    if p.suffix not in {'.md', '.json', '.py', '.mod', '.txt', '.gui', '.yml'}:
        continue
    text = p.read_text(encoding='utf-8-sig')
    if re.search(r'(?i)[a-z]:[\\/](?:users|onedrive|ai总御)', text):
        failures.append('Machine-private absolute path: ' + p.relative_to(root).as_posix())
    if p.suffix != '.md':
        continue
    for match in re.finditer(r'\[[^\]\n]+\]\(([^)\n]+)\)', text):
        target = unquote(match.group(1).strip().strip('<>'))
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
            continue
        target = target.split('#', 1)[0]
        if not target:
            continue
        links += 1
        resolved = (p.parent / target).resolve()
        if root != resolved and root not in resolved.parents:
            failures.append('Link leaves repository: ' + target)
        elif not resolved.exists():
            failures.append('Broken link in ' + p.relative_to(root).as_posix() + ': ' + target)

result = {
    'status': 'PASS' if not failures else 'FAIL',
    'mod_files': len(actual), 'source_hash_entries': len(expected),
    'historical_evidence_files': len(evidence),
    'relative_links_checked': links, 'failures': failures,
    'scope': 'repository integrity and handoff references only',
    'game_runtime': 'NOT_RUN',
}
print(json.dumps(result, ensure_ascii=True, indent=2))
raise SystemExit(bool(failures))
