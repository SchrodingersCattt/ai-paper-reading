"""Rebuild the question from the saved Uni-Parser page blocks."""
import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--out', required=True, type=Path)
args = parser.parse_args()
source = Path(__file__).resolve().parent / 'zeng-parser-key-blocks.json'
data = json.loads(source.read_text(encoding='utf-8'))
blocks = {(b['pdf_page'],b['order']):b.get('text','') for b in data['blocks']}

def span(text, start, end):
    a = text.index(start)
    b = text.index(end,a) + len(end)
    return text[a:b]

p6, qm, model = blocks[(6,13)], blocks[(7,8)], blocks[(7,10)]
items = [
    ('P6-13a', span(p6,'To increase the efficiency','initial dataset.')),
    ('P6-13b', span(p6,'Then, for each atom','cutoff was set to 5 Å.')),
    ('P7-8', span(qm,'The potential energy','MN15/6-31G** level.')),
    ('P7-10a', span(model,'The DeepPot-SE','DeePMD-kit program')),
    ('P7-10b', span(model,'The cutoff radius','from 1.0 to 6.0 Å.')),
]
prompt = '以下是玻尔解析 Zeng 2020 论文后保留的原文块。只依据这些块，用中文分四行解释：ReaxFF 的作用、能量和力参考值的来源、5 Å 的用途、6 Å 的用途。每行标对应块号；不要补充块外事实。\n\n'
prompt += '\n'.join(f'[{label}] {value}' for label,value in items) + '\n'
args.out.parent.mkdir(parents=True,exist_ok=True)
args.out.write_bytes(prompt.encode('utf-8'))
print(f'Question saved to {args.out}')
