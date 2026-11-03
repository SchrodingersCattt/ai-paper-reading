"""Reproduce one of the paper-reading runs in a new Windows workspace."""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PDFS = {
    'A': 'materials/source/zeng2020-methane-nn-md.pdf',
    'B': 'materials/source/wen2020-dunn-carbon.pdf',
    'C': 'materials/source/zeng2020-constructed-pages1-2.pdf',
}

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--case', required=True, choices=PDFS)
parser.add_argument('--with-skill', action='store_true')
parser.add_argument('--out', type=Path, required=True, help='new output directory')
parser.add_argument('--dry-run', action='store_true', help='print input identities without launching the agent')
args = parser.parse_args()
pdf = ROOT / PDFS[args.case]
task = ROOT / 'examples/zeng-v5/cases' / args.case / 'task.md'
if not pdf.is_file():
    raise SystemExit(f'Full PDF required for case {args.case}: {pdf}')
agent_rel = Path('cursor-agent/versions/2026.10.19-6bbf2c4')
candidates = [Path(os.environ['LOCALAPPDATA']) / agent_rel, Path.home() / 'AppData/Local' / agent_rel]
agent_dir = next((p for p in candidates if (p/'node.exe').is_file() and (p/'index.js').is_file()), candidates[0])
details = {'case':args.case, 'with_skill':args.with_skill, 'model':'grok-4.7-high', 'harness':'Cursor agent CLI 2026.10.19-6bbf2c4', 'pdf_sha256':sha256(pdf), 'task_sha256':sha256(task), 'skill_sha256':sha256(ROOT/'skill/SKILL.md') if args.with_skill else None, 'agent_available':(agent_dir/'node.exe').is_file() and (agent_dir/'index.js').is_file()}
if args.dry_run:
    print(json.dumps(details,ensure_ascii=False,indent=2))
    raise SystemExit(0)
if not details['agent_available']:
    raise SystemExit('The documented Cursor agent CLI version is not installed.')
out = args.out.resolve()
out.mkdir(parents=True,exist_ok=False)
ws = out / 'workspace'
ws.mkdir()
shutil.copy2(pdf, ws/'paper.pdf')
if args.with_skill:
    shutil.copy2(ROOT/'skill/SKILL.md',ws/'SKILL.md')
    shutil.copy2(ROOT/'skill/check_answer.py',ws/'check_answer.py')
    shutil.copytree(ROOT/'skill/references',ws/'references')
prompt = task.read_text(encoding='utf-8')
cmd = [str(agent_dir/'node.exe'),str(agent_dir/'index.js'),'--print','--output-format','stream-json','--model','grok-4.7-high','--trust','--force','--sandbox','disabled','--workspace',str(ws),prompt]
env = os.environ.copy()
env['PYTHONUTF8'] = '1'
start = time.monotonic()
started_at = datetime.now(timezone.utc).isoformat()
timed_out = False
with (out/'stream.jsonl').open('wb') as stdout, (out/'stderr.txt').open('wb') as stderr:
    try:
        proc = subprocess.run(cmd,cwd=ws,env=env,stdout=stdout,stderr=stderr,timeout=900)
        exit_code = proc.returncode
    except subprocess.TimeoutExpired:
        timed_out, exit_code = True, None
answer = ws/'answer.md'
if answer.exists():
    shutil.copy2(answer,out/'answer.md')
details.update({'started_at':started_at,'exit':exit_code,'timeout':timed_out,'duration_seconds':round(time.monotonic()-start,1),'answer_present':answer.exists(),'cost':'无法取得'})
(out/'meta.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(details,ensure_ascii=False))
if timed_out or exit_code != 0 or not answer.exists():
    raise SystemExit(1)
