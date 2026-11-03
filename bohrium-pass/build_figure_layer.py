"""Extract Fig. 5's PDF text layer and rebuild the recorded question."""
import argparse
import hashlib
from pathlib import Path
import fitz

here = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--out', type=Path, required=True)
parser.add_argument('--pdf', type=Path, default=here.parent/'materials/source/zeng2020-methane-nn-md.pdf')
args = parser.parse_args()
args.out.mkdir(parents=True, exist_ok=True)
page = fitz.open(args.pdf)[5]
words = page.get_text('words', clip=fitz.Rect(100, 40, 480, 275))
layer = '\n'.join(f'{x0:.1f}\t{y0:.1f}\t{word}' for x0,y0,x1,y1,word,block,line,index in words) + '\n'
addition = ('\n下方是从原 PDF 第 6 页 Fig. 5 区域的文字层提取的词，前两列是词左上角 x、y 坐标，单位为 PDF 点，原点在页面左上角。'
            '请利用这些文字核对图中英文标签；文字和位置不能直接证明箭头连接，无法从材料确定的箭头请标记为需要看原图。\n\n'
            'x\ty\tword\n' + layer)
source = (here/'zeng-parser-retest-page6.txt').read_text(encoding='utf-8')
question = '请列出这篇论文 Fig. 5 图中每个方框的名称及箭头顺序，并给出依据。用中文回答。'
baseline = ('以下是玻尔解析 Zeng 2020 论文第 6 页返回的文本：\n\n' + source + '\n\n' + question + '\n').encode('utf-8')
prompt = baseline + addition.encode('utf-8')
(args.out/'words.txt').write_bytes(layer.encode('utf-8'))
(args.out/'question.txt').write_bytes(prompt)
print('words:', len(words), 'prompt_sha256:', hashlib.sha256(prompt).hexdigest())
