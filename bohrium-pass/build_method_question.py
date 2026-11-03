"""Rebuild the two recorded method questions from the saved parser block."""
import argparse
import hashlib
from pathlib import Path

here = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--vector-prompt',required=True,type=Path)
parser.add_argument('--out',required=True,type=Path)
parser.add_argument('--mode',required=True,choices=['ambiguous','explicit'])
args = parser.parse_args()
block = (here/'zeng-figure-method-page7-block.txt').read_text(encoding='utf-8')
if args.mode == 'ambiguous':
    introduction = '\n\n补充材料：以下为玻尔解析结果中 PDF 第 7 页 QM calculation 的原文块。\n[P7-8] '
    reference = '第 6 页原文和 [P7-8]'
else:
    introduction = '\n\n补充材料：以下为玻尔解析结果中 PDF 第 7 页 QM calculation 的原文块，BLOCK 8 是块编号而非页码。\n[PDF_PAGE_7_BLOCK_8] '
    reference = '第 6 页原文和 [PDF_PAGE_7_BLOCK_8]'
addition=(introduction+block+'\n\n请保留前述全部节点、箭头和分支，并对照'+reference+' 回答：'
          '初始数据集是在去冗余之前还是之后？Coulomb 矩阵用什么表示后进行聚类？'
          '量子化学计算为每个最终结构提供哪两类参考量，具体使用什么方法？'
          '每项注明 PDF 页码和原文位置；材料没有说明时直接写未说明。\n')
args.out.mkdir(parents=True,exist_ok=True)
prompt=args.vector_prompt.read_bytes()+addition.encode('utf-8')
(args.out/('method-'+args.mode+'-prompt.txt')).write_bytes(prompt)
print('prompt_sha256:',hashlib.sha256(prompt).hexdigest())
