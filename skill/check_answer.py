"""Check the answer's encoding and basic structure, not scientific accuracy."""
from pathlib import Path
import sys

try:
    text = Path('answer.md').read_text(encoding='utf-8')
except (OSError, UnicodeDecodeError) as error:
    sys.exit(f'cannot read UTF-8 answer.md: {error}')

required = ('阅读问题', '方法链条', '证据与条件', '适用判断', '结论', '待查')
lines = text.splitlines()
headings = {line.lstrip('#').strip() for line in lines if line.lstrip().startswith('#')}
missing = [heading for heading in required if heading not in headings]
if missing:
    sys.exit('missing headings: ' + ', '.join(missing))
for index, line in enumerate(lines):
    if line.lstrip().startswith('#') and line.lstrip('#').strip() == '结论':
        verdict = next((line.strip().strip('*`') for line in lines[index + 1:] if line.strip()), '')
        break
if verdict not in ('可用', '部分可用', '不可用', '材料不足停止'):
    sys.exit('conclusion must be one of the four allowed values on its own line')
print('UTF-8 and required sections present; check scientific claims against the paper.')
