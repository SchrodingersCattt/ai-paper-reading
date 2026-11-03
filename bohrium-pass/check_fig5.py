"""核对 Zeng 2020 这篇 PDF 的 Fig. 5；只适用于这一张图。"""
import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "materials" / "source" / "zeng2020-methane-nn-md.pdf"
PROTOCOL = ROOT / "bohrium-pass" / "zeng-figure-vector-protocol.md"
EXTRACT = ROOT / "bohrium-pass" / "extract_fig5_graph.py"


def fail(message):
    print(message, file=sys.stderr)
    raise SystemExit(1)


def fresh_out(path):
    out = path.expanduser().resolve()
    if not out.parent.is_dir():
        fail(f"上级目录不存在，未写入：{out.parent}")
    if out.exists():
        fail(f"输出路径已存在，未写入：{out}")
    return out


def load_protocol(path):
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    # The later acceptance section also mentions arrows. Only the manually
    # checked list under this heading is the nine-node, nine-edge record.
    heading = "## 运行前人工核对的原图"
    if heading not in text:
        fail(f"协议缺少人工核对原图一节：{path}")
    section = text.split(heading, 1)[1].split("\n## ", 1)[0]
    marker = "Fig. 5 的节点按原图为："
    node_lines = [line for line in section.splitlines() if marker in line]
    if len(node_lines) != 1:
        fail(f"协议里没有唯一定义节点的那一句：{path}")
    body = node_lines[0].split(marker, 1)[1].split("。", 1)[0]
    nodes = [part.strip() for part in body.split("；") if part.strip()]
    edges = []
    for raw in section.splitlines():
        line = raw.strip()
        branched = re.fullmatch(r"\d+\.\s+(.+)\s+→\s+(.+)，分支\s+(YES|NO)。", line)
        plain = re.fullmatch(r"\d+\.\s+(.+)\s+→\s+(.+)。", line)
        if branched:
            edges.append((branched.group(1), branched.group(2), branched.group(3)))
        elif plain:
            edges.append((plain.group(1), plain.group(2), None))
    if len(nodes) != 9 or len(edges) != 9:
        fail(f"协议应有九个节点和九条边，实际读到 {len(nodes)} 个节点、{len(edges)} 条边：{path}")
    node_set = set(nodes)
    if len(node_set) != 9:
        fail(f"协议节点有重复：{nodes}")
    for src, dst, _branch in edges:
        if src not in node_set or dst not in node_set:
            fail(f"协议中的边无法对应节点：{src} → {dst}")
    return nodes, edges


def bind_label(text, labels):
    # Longest label wins, so "Final dataset" stays distinct from "Dataset".
    for label in sorted(labels, key=len, reverse=True):
        if text == label or text.startswith(label + " ") or text.startswith(label + "("):
            return label
    return None


def run_extract(pdf, out):
    return subprocess.run(
        [sys.executable, str(EXTRACT), "--pdf", str(pdf), "--out", str(out)],
        cwd=str(ROOT),
        env=os.environ.copy(),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=120,
        check=False,
    )


def check_real(out):
    nodes, edges = load_protocol(PROTOCOL)
    if not PDF.is_file():
        fail(f"找不到论文 PDF：{PDF}")
    if not EXTRACT.is_file():
        fail(f"找不到提取脚本：{EXTRACT}")
    proc = run_extract(PDF, out)
    graph_path = out / "graph.json"
    if proc.returncode != 0 or not graph_path.is_file():
        detail = (proc.stderr or proc.stdout or "").strip()
        fail(
            "提取原 PDF 第 6 页失败，未得到可核对的 graph.json。\n"
            f"退出码：{proc.returncode}\n{detail}"
        )
    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    if graph.get("page_index") != 5:
        fail(f"graph.json 的 page_index 不是 5：{graph.get('page_index')}")
    id_to_label = {}
    for node in graph.get("nodes", []):
        label = bind_label(node.get("text", ""), nodes)
        if label is None:
            fail(f"节点无法对应协议：{node.get('text')!r}")
        if label in id_to_label.values():
            fail(f"协议节点被重复对应：{label}")
        id_to_label[node["id"]] = label
    if set(id_to_label.values()) != set(nodes):
        fail("抽出的节点与协议的九个节点不一致。")
    got = []
    for arrow in graph.get("arrows", []):
        src = id_to_label.get(arrow.get("from"))
        dst = id_to_label.get(arrow.get("to"))
        if src is None or dst is None:
            fail(f"箭头端点无法对应节点：{arrow}")
        branch = arrow.get("branch")
        if branch is not None and branch not in ("YES", "NO"):
            fail(f"无法识别的分支标记：{branch}")
        got.append((src, dst, branch))
    if Counter(got) != Counter(edges):
        fail("方向或 YES/NO 与协议不一致。\n" f"协议：{edges}\n抽出：{got}")
    lines = [
        "核对 Zeng 2020 PDF 第 6 页 Fig. 5（页索引 5）。",
        "9 个节点、9 条边与 bohrium-pass/zeng-figure-vector-protocol.md 中人工核对过的方向一致。",
    ]
    for src, dst, branch in edges:
        lines.append(f"{src} → {dst} [{branch}]" if branch else f"{src} → {dst}")
    lines.append(f"结果文件：{graph_path}")
    lines.append("完整原图和这次抽出的结果仍要人工对照 materials/excerpts/zeng2020-fig5.png。")
    lines.append("本脚本只检查这篇论文的 Fig. 5。")
    print("\n".join(lines))


def check_blank(out):
    import fitz

    out.mkdir()
    pdf_path = out / "blank-6pages.pdf"
    doc = fitz.open()
    try:
        for _ in range(6):
            doc.new_page(width=595.276, height=841.890)
        doc.save(pdf_path)
    finally:
        doc.close()
    opened = fitz.open(pdf_path)
    try:
        page_count = opened.page_count
    finally:
        opened.close()
    if page_count != 6:
        fail(f"空白 PDF 页数不是 6：{page_count}")
    extract_dir = out / "extract"
    proc = run_extract(pdf_path, extract_dir)
    (out / "extractor-stderr.txt").write_text(proc.stderr or "", encoding="utf-8")
    (out / "extractor-stdout.txt").write_text(proc.stdout or "", encoding="utf-8")
    graphs = list(out.rglob("graph.json"))
    expected = "Unexpected diagram structure: 0 nodes, 0 arrows"
    if proc.returncode == 0 or graphs or expected not in (proc.stderr or ""):
        fail(
            "空白图测试未按预期失败。\n"
            f"提取器退出码：{proc.returncode}\n"
            f"graph.json：{graphs}\n"
            f"{proc.stderr}"
        )
    print(f"空白 PDF：{pdf_path}（{page_count} 页）")
    print(f"提取器退出码：{proc.returncode}")
    print(f"提取器报错：ValueError: {expected}")
    print("未生成 graph.json。")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True, help="必须是还不存在的新目录")
    parser.add_argument(
        "--blank",
        action="store_true",
        help="生成六页空白 PDF，确认提取器报错且不写出 graph.json",
    )
    args = parser.parse_args()
    out = fresh_out(args.out)
    if args.blank:
        check_blank(out)
    else:
        check_real(out)


if __name__ == "__main__":
    main()
