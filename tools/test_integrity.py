"""Regressions for omissions found during the independent GitHub-only review."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

root = Path(__file__).resolve().parents[1]
results = []
cases = [
    ('baseline', (0, 0)),
    ('changed_source', (1, 1)),
    ('omitted_external_descriptor', (1, 1)),
    ('wrong_descriptor_path_with_new_hash', (1, 1)),
    ('descriptor_metadata_mismatch_with_new_hash', (1, 1)),
    ('empty_evidence', (0, 1)),
    ('removed_required_evidence', (0, 1)),
    ('duplicate_source_entry', (1, 1)),
    ('invalid_source_schema', (1, 1)),
]
with tempfile.TemporaryDirectory(prefix='ck3-pgh-integrity-') as temporary:
    for name, expected in cases:
        target = Path(temporary) / name
        shutil.copytree(root, target, ignore=shutil.ignore_patterns('.git', '__pycache__'))
        manifest_path = target / 'source-manifest.json'
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        evidence_path = target / 'docs/evidence/manifest.json'
        evidence = json.loads(evidence_path.read_text(encoding='utf-8'))
        descriptor = target / 'pgh_accounts.mod'
        if name == 'changed_source':
            path = target / 'pgh_accounts/descriptor.mod'
            path.write_bytes(path.read_bytes() + b'\n# test mutation\n')
        elif name == 'omitted_external_descriptor':
            manifest['files'] = [r for r in manifest['files'] if r['path'] != 'pgh_accounts.mod']
            descriptor.write_text('path="mod/missing-folder"\n', encoding='utf-8')
        elif name in {'wrong_descriptor_path_with_new_hash', 'descriptor_metadata_mismatch_with_new_hash'}:
            text = descriptor.read_text(encoding='utf-8')
            if name == 'wrong_descriptor_path_with_new_hash':
                text = text.replace('path="mod/pgh_accounts"', 'path="mod/missing-folder"')
            else:
                text = text.replace('supported_version="1.20.*"', 'supported_version="0.0.*"')
            descriptor.write_text(text, encoding='utf-8')
            for row in manifest['files']:
                if row['path'] == 'pgh_accounts.mod':
                    row['sha256'] = hashlib.sha256(descriptor.read_bytes()).hexdigest()
        elif name == 'empty_evidence':
            evidence['files'] = []
        elif name == 'removed_required_evidence':
            removed = evidence['files'].pop()
            (target / removed['path']).unlink()
        elif name == 'duplicate_source_entry':
            manifest['files'].append(manifest['files'][0].copy())
        elif name == 'invalid_source_schema':
            manifest = []
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=True), encoding='utf-8')
        evidence_path.write_text(json.dumps(evidence, ensure_ascii=True), encoding='utf-8')
        checks = []
        for tool in ['verify_manifest.py', 'verify_handoff.py']:
            result = subprocess.run([sys.executable, '-I', str(target / 'tools' / tool)], cwd=target, capture_output=True, text=True, encoding='utf-8')
            checks.append({'tool': tool, 'exit_code': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr})
        passed = tuple(c['exit_code'] for c in checks) == expected and all(not c['stderr'] for c in checks)
        results.append({'case': name, 'passed': passed, 'expected_exit_codes': expected, 'checks': checks})
report = {'status': 'PASS' if all(r['passed'] for r in results) else 'FAIL', 'cases': len(results), 'results': results, 'game_runtime': 'NOT_RUN'}
print(json.dumps(report, ensure_ascii=True, indent=2))
raise SystemExit(report['status'] != 'PASS')
