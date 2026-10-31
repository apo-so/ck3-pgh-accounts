from pathlib import Path
import json
import runpy

root = Path(__file__).resolve().parents[1]
checks = runpy.run_path(str(root / 'tools/project_checks.py'))
entries, actual, failures = checks['check_source'](root)
print(json.dumps({'files': len(entries), 'mod_files': len(actual), 'failures': failures}, ensure_ascii=True))
raise SystemExit(bool(failures))
