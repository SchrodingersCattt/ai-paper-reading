"""Rebuild either Fig. 5 question from the saved page-6 parser output."""
import argparse
import json
import sys
from pathlib import Path


def fail(message):
    print(message, file=sys.stderr)
    raise SystemExit(1)


def one_index(value):
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str) and exact_decimal(value):
        return int(value)
    return None


def exact_decimal(text):
    if text.startswith('-'):
        sign, body = '-', text[1:]
    else:
        sign, body = '', text
    if not body.isdigit():
        return False
    canonical = '0' if int(body) == 0 and not sign else f'{sign}{int(body)}'
    return text == canonical


def parse_pages(pages):
    if isinstance(pages, list):
        indexes = []
        for item in pages:
            index = one_index(item)
            if index is None:
                return None
            indexes.append(index)
        return indexes
    index = one_index(pages)
    if index is None:
        return None
    return [index]


def task_token(document):
    token = document.get('token')
    if not isinstance(token, str) or token.strip() == '':
        return None
    return token


def load_parsed_page(result_dir):
    directory = result_dir.expanduser()
    ref_path = directory / 'task-reference.json'
    result_path = directory / 'result.json'
    if not ref_path.is_file() or not result_path.is_file():
        fail(f'结果目录缺少 task-reference.json 或 result.json：{directory}')
    try:
        reference = json.loads(ref_path.read_text(encoding='utf-8'))
        result = json.loads(result_path.read_text(encoding='utf-8'))
    except (OSError, UnicodeError, json.JSONDecodeError):
        fail('task-reference.json 或 result.json 无法按 UTF-8 JSON 读取')
    if not isinstance(reference, dict) or not isinstance(result, dict):
        fail('task-reference.json 或 result.json 不是 JSON 对象')
    ref_token = task_token(reference)
    result_token = task_token(result)
    if ref_token is None or result_token is None or ref_token != result_token:
        fail('两份文件的任务 token 缺失或不一致')
    request = reference.get('request')
    pages = request.get('pages') if isinstance(request, dict) else None
    indexes = parse_pages(pages)
    if not indexes or len(indexes) != 1:
        fail('请求不是单页')
    if indexes[0] != 5:
        fail('请求页索引不是 5')
    if result.get('status') != 'success':
        fail('结果状态不是 success')
    content = result.get('content')
    if not isinstance(content, str) or content.strip() == '':
        fail('结果 content 不是非空文本')
    return content


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', required=True, choices=['baseline', 'guarded'])
    parser.add_argument('--out', required=True, type=Path)
    parser.add_argument(
        '--result-dir',
        type=Path,
        help='directory where parse_zeng.py saved task-reference.json and result.json',
    )
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    if args.result_dir is None:
        source = (here / 'zeng-parser-retest-page6.txt').read_text(encoding='utf-8')
    else:
        source = load_parsed_page(args.result_dir)
    question = '请列出这篇论文 Fig. 5 图中每个方框的名称及箭头顺序，并给出依据。用中文回答。'
    text = '以下是玻尔解析 Zeng 2020 论文第 6 页返回的文本：\n\n' + source + '\n\n' + question + '\n'
    if args.mode == 'guarded':
        text += '先检查文本中是否真的包含图内方框和箭头；缺少时直接说明，不能把正文中的推测当成图中的标注。\n'
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_bytes(text.encode('utf-8'))
    print(f'Question saved to {args.out}')


if __name__ == '__main__':
    main()
