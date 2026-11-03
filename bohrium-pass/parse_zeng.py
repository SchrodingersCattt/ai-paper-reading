"""Submit the local paper to Bohrium Uni-Parser and retrieve the actual result."""
import argparse
import json
import os
import sys
import uuid
from pathlib import Path

import requests

BASE = 'https://open.bohrium.com/openapi/v2/parse'
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('action', choices=['submit', 'poll'])
parser.add_argument('--out', required=True, type=Path, help='local directory for the task reference and response')
parser.add_argument('--pdf', type=Path, default=Path('materials/source/zeng2020-methane-nn-md.pdf'))
parser.add_argument('--figure', type=int, choices=[0, 1], default=0)
parser.add_argument('--page-index', type=int, help='zero-based single page; omit for the whole PDF')
args = parser.parse_args()
api_key = os.environ.get('BOHR_ACCESS_KEY')
if not api_key:
    sys.exit('Set BOHR_ACCESS_KEY in the environment before calling the API.')
headers = {'Authorization': f'Bearer {api_key}'}
args.out.mkdir(parents=True, exist_ok=True)
ref_path = args.out / 'task-reference.json'

if args.action == 'submit':
    if ref_path.exists():
        sys.exit('Task reference already exists. Use a new output directory or poll the existing task.')
    task_token = str(uuid.uuid4())
    form = {'token': task_token, 'sync': 'false', 'textual': '2', 'table': '2', 'equation': '2', 'molecule': '0', 'chart': '0', 'figure': str(args.figure), 'expression': '0', 'timeout': '1800'}
    if args.page_index is not None:
        if args.page_index < 0:
            sys.exit('--page-index must be non-negative')
        form['pages'] = str(args.page_index)
    with args.pdf.open('rb') as pdf:
        response = requests.post(BASE + '/trigger-file-async', headers=headers, files={'file': (args.pdf.name, pdf, 'application/pdf')}, data=form, timeout=60)
    if not response.ok:
        print(f'Parser request returned HTTP {response.status_code}; no task reference saved.', file=sys.stderr)
        sys.exit(1)
    body = response.json()
    if body.get('code') not in (None, 0):
        sys.exit(f"Parser request failed: {body.get('message', body.get('code'))}")
    task_token = body.get('token') or task_token
    ref_path.write_text(json.dumps({'token':task_token, 'request':{k:v for k,v in form.items() if k != 'token'}}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"Submitted: {body.get('status', 'unknown')}; task reference saved to {ref_path}")
else:
    if not ref_path.is_file():
        sys.exit(f'No task reference: {ref_path}')
    task_token = json.loads(ref_path.read_text(encoding='utf-8'))['token']
    response = requests.post(BASE + '/get-result', headers=headers, json={'token':task_token, 'content':True, 'objects':False, 'pages_dict':True}, timeout=60)
    response.raise_for_status()
    body = response.json()
    if body.get('code') not in (None, 0):
        sys.exit(f"Parser result failed: {body.get('message', body.get('code'))}")
    result_path = args.out / 'result.json'
    result_path.write_text(json.dumps(body, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"Status: {body.get('status', 'unknown')}; result saved to {result_path}")
