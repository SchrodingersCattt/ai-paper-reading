"""Rebuild either Fig. 5 question from the saved page-6 parser output."""
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--mode', required=True, choices=['baseline','guarded'])
parser.add_argument('--out', required=True, type=Path)
args = parser.parse_args()
here = Path(__file__).resolve().parent
source = (here/'zeng-parser-retest-page6.txt').read_text(encoding='utf-8')
question = '请列出这篇论文 Fig. 5 图中每个方框的名称及箭头顺序，并给出依据。用中文回答。'
text = '以下是玻尔解析 Zeng 2020 论文第 6 页返回的文本：\n\n' + source + '\n\n' + question + '\n'
if args.mode == 'guarded':
    text += '先检查文本中是否真的包含图内方框和箭头；缺少时直接说明，不能把正文中的推测当成图中的标注。\n'
args.out.parent.mkdir(parents=True,exist_ok=True)
args.out.write_bytes(text.encode('utf-8'))
print(f'Question saved to {args.out}')
