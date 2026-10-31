from pathlib import Path
import hashlib, json
root = Path(__file__).resolve().parents[1]
data = json.loads((root / 'source-manifest.json').read_text(encoding='utf-8'))
bad = []
for row in data['files']:
    p = root / row['path']
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != row['sha256']:
        bad.append(row['path'])
actual = {p.relative_to(root).as_posix() for p in (root / 'pgh_accounts').rglob('*') if p.is_file()}
expected = {x['path'] for x in data['files'] if x['path'].startswith('pgh_accounts/')}
bad.extend(sorted(actual ^ expected))
print(json.dumps({'files': len(data['files']), 'failures': bad}, ensure_ascii=False))
raise SystemExit(bool(bad))
