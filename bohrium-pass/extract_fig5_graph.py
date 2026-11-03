"""Extract Fig. 5 vector nodes and arrows from this particular paper's PDF."""
import argparse
import json
import math
from pathlib import Path

import fitz

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--pdf', type=Path, required=True)
parser.add_argument('--out', type=Path, required=True)
args = parser.parse_args()
args.out.mkdir(parents=True, exist_ok=True)
doc = fitz.open(args.pdf)
page = doc[5]
clip = fitz.Rect(100, 40, 480, 275)
drawings = [d for d in page.get_drawings() if d['rect'].intersects(clip)]
words = page.get_text('words', clip=clip)

def pt(p):
    return (round(p.x, 2), round(p.y, 2))

def arrow_tip(d):
    items = d['items']
    if len(items) < 3 or any(item[0] != 'l' for item in items[-3:]):
        return None
    edges = items[-3:]
    if not all(math.dist(pt(edges[i][2]), pt(edges[(i+1)%3][1])) < 0.1 for i in range(3)):
        return None
    vertices = [pt(item[1]) for item in edges]
    if max(math.dist(a,b) for a in vertices for b in vertices) > 4:
        return None
    for i, (x,y) in enumerate(vertices):
        a,b = [vertices[j] for j in range(3) if j != i]
        if abs(a[0]-b[0]) < 0.1 and abs(x-a[0]) > 0.5:
            return (x,y)
        if abs(a[1]-b[1]) < 0.1 and abs(y-a[1]) > 0.5:
            return (x,y)
    return None

def point_distance(point, rect):
    x,y = point
    return math.hypot(max(rect.x0-x,0,x-rect.x1),max(rect.y0-y,0,y-rect.y1))

def rect_distance(a,b):
    return math.hypot(max(a.x0-b.x1,b.x0-a.x1,0),max(a.y0-b.y1,b.y0-a.y1,0))

node_paths = [(i,d) for i,d in enumerate(drawings)
              if d['fill'] is not None and d['rect'].width >= 25 and d['rect'].height >= 15 and arrow_tip(d) is None]
nodes = []
for i,d in node_paths:
    r = d['rect']
    selected = [w for w in words if r.contains(fitz.Point((w[0]+w[2])/2,(w[1]+w[3])/2))]
    selected.sort(key=lambda w:(round(w[1],1),w[0]))
    label = ' '.join(w[4] for w in selected)
    if not label:
        raise ValueError(f'Node path {i} has no text')
    nodes.append({'id':f'N{len(nodes)+1}', 'text':label, 'rect':[round(x,2) for x in r], 'drawing_index':i})

arrows = []
for i,d in enumerate(drawings):
    tip = arrow_tip(d)
    if tip is None:
        continue
    ranked = sorted((point_distance(tip,fitz.Rect(n['rect'])),n['id']) for n in nodes)
    if not ranked or ranked[0][0] > 2 or (len(ranked)>1 and ranked[1][0]-ranked[0][0] < 0.1):
        raise ValueError(f'Ambiguous arrow target at drawing {i}: {ranked[:2]}')
    target = ranked[0][1]
    sources = [(rect_distance(d['rect'],fitz.Rect(n['rect'])),n['id']) for n in nodes if n['id'] != target]
    sources = sorted(x for x in sources if x[0] < 2)
    if len(sources) != 1:
        raise ValueError(f'Ambiguous arrow source at drawing {i}: {sources}')
    arrows.append({'from':sources[0][1], 'to':target, 'tip':tip, 'drawing_index':i,
                   'rect':[round(x,2) for x in d['rect']]})

# Branch words lie outside the node polygons. Assign them to the nearest
# outgoing arrow of the decision node, then check the assignment visually.
decision_nodes = {n['id'] for n in nodes if '?' in n['text']}
for w in words:
    if w[4] not in ('YES','NO'):
        continue
    center = fitz.Point((w[0]+w[2])/2,(w[1]+w[3])/2)
    options = sorted((point_distance((center.x,center.y),fitz.Rect(a['rect'])),index)
                     for index,a in enumerate(arrows) if a['from'] in decision_nodes)
    if not options or (len(options)>1 and options[1][0]-options[0][0] < 2):
        raise ValueError(f'Ambiguous branch label: {w[4]}')
    if 'branch' in arrows[options[0][1]]:
        raise ValueError(f'More than one branch label matched arrow {options[0][1]}')
    arrows[options[0][1]]['branch'] = w[4]

if len(nodes) != 9 or len(arrows) != 9:
    raise ValueError(f'Unexpected diagram structure: {len(nodes)} nodes, {len(arrows)} arrows')
if sorted(a['branch'] for a in arrows if 'branch' in a) != ['NO','YES']:
    raise ValueError('Expected one YES and one NO branch')
payload = {'page_index':5, 'clip_points':[100,40,480,275], 'pymupdf_version':fitz.VersionBind,
           'nodes':nodes, 'arrows':arrows}
(args.out/'graph.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for node in nodes:
    print(node['id'], node['text'])
for arrow in arrows:
    print(arrow['from'],'->',arrow['to'],arrow.get('branch',''),'tip',arrow['tip'])
