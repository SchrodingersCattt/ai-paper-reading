"""Attach the extracted figure graph to the saved page-6 reading question."""
import argparse
import hashlib
import json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--baseline', required=True, type=Path)
parser.add_argument('--graph', required=True, type=Path)
parser.add_argument('--out', required=True, type=Path)
args = parser.parse_args()
data = json.loads(args.graph.read_text(encoding='utf-8'))
nodes = [f"{n['id']}: {n['text']}" for n in data['nodes']]
arrows = [f"{e['from']} -> {e['to']}" + (f" ({e['branch']})" if e.get('branch') else '') for e in data['arrows']]
supplement = ('\n\n补充材料：下列节点文字及有向箭头由同一 PDF 第 6 页 Fig. 5 的矢量形状、文字和箭头提取，'
              '分支文字用邻近关系标注。请按材料列出各节点和箭头，并解释 YES/NO 的循环或退出；'
              '区分节点、区域名称和分支标记，原文没有给出的内容不要猜。图中结论标注 PDF 页码和图号。\n\n'
              '节点：\n' + '\n'.join(nodes) + '\n箭头：\n' + '\n'.join(arrows) + '\n')
args.out.mkdir(parents=True,exist_ok=True)
(args.out/'vector-supplement.txt').write_bytes(supplement.encode('utf-8'))
prompt = args.baseline.read_bytes() + supplement.encode('utf-8')
(args.out/'vector-prompt.txt').write_bytes(prompt)
print('prompt_sha256:',hashlib.sha256(prompt).hexdigest())
