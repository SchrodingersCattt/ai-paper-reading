"""用仓库里已保存的第 6 页文本构造测试，核对 Fig. 5 提问的新旧两条路径。不联网。"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / 'bohrium-pass' / 'zeng-parser-retest-page6.txt'
METADATA = ROOT / 'bohrium-pass' / 'zeng-parser-retest-metadata.json'
COMPARISON = ROOT / 'bohrium-pass' / 'zeng-figure-comparison-metadata.json'
BUILD = ROOT / 'bohrium-pass' / 'build_figure_question.py'
TOKEN = 'constructed-test-token'
TOKEN_OTHER = 'constructed-test-token-mismatch'
SENTINEL = '\nparser-bridge-sentinel\n'


def fail(message):
    print(message, file=sys.stderr)
    raise SystemExit(1)


def fresh_out(path):
    out = path.expanduser().resolve()
    if not out.parent.is_dir():
        fail(f'上级目录不存在，未写入：{out.parent}')
    if out.exists():
        fail(f'输出路径已存在，未写入：{out}')
    return out


def redact(text):
    return (text or '').replace(TOKEN_OTHER, '[token]').replace(TOKEN, '[token]')


def leaked(text):
    raw = text or ''
    return TOKEN in raw or TOKEN_OTHER in raw


def write_json(path, document):
    path.write_text(json.dumps(document, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def base_documents(page_text, request, status):
    reference = {
        'constructed_test': True,
        'notice': '构造测试，不是玻尔返回。request 复制自仓库已保存的单页元数据，token 是测试占位符。',
        'token': TOKEN,
        'request': request,
    }
    result = {
        'constructed_test': True,
        'notice': '构造测试，不是玻尔返回。content 复制自仓库已保存的第 6 页文本，token 是测试占位符。',
        'token': TOKEN,
        'status': status,
        'content': page_text,
    }
    return reference, result


def write_pair(directory, reference, result):
    directory.mkdir()
    write_json(directory / 'task-reference.json', reference)
    write_json(directory / 'result.json', result)


def run_builder(mode, dest, result_dir=None):
    command = [sys.executable, str(BUILD), '--mode', mode, '--out', str(dest)]
    if result_dir is not None:
        command.extend(['--result-dir', str(result_dir)])
    return subprocess.run(
        command,
        cwd=str(ROOT),
        env=os.environ.copy(),
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='strict',
        timeout=60,
        check=False,
    )


def expected_hashes():
    rows = json.loads(COMPARISON.read_text(encoding='utf-8'))
    found = {}
    for row in rows:
        found[row['mode']] = row['prompt_sha256']
    if set(found) != {'baseline', 'guarded'}:
        fail(f'对照记录里的提问模式不完整：{sorted(found)}')
    return found


def load_saved():
    if not PAGE.is_file() or not METADATA.is_file() or not COMPARISON.is_file() or not BUILD.is_file():
        fail('缺少已保存的单页文本、元数据、对照记录或提问脚本')
    page_text = PAGE.read_text(encoding='utf-8')
    metadata = json.loads(METADATA.read_text(encoding='utf-8'))
    request = metadata.get('request')
    if not isinstance(request, dict) or request.get('pages') != '5':
        fail('已保存元数据的请求页索引不是 5')
    if metadata.get('requested_page_count') != 1:
        fail('已保存元数据不是单页请求')
    if metadata.get('status') != 'success':
        fail('已保存元数据的状态不是 success')
    if not isinstance(page_text, str) or page_text.strip() == '':
        fail('已保存的单页文本为空')
    if TOKEN in page_text or TOKEN_OTHER in page_text:
        fail('测试占位符与已保存文本冲突')
    return page_text, request, metadata['status']


def check_rebuild(out, page_text, request, status, expected, lines):
    constructed = out / 'constructed'
    reference, result = base_documents(page_text, request, status)
    write_pair(constructed, reference, result)
    for name in ('task-reference.json', 'result.json'):
        document = json.loads((constructed / name).read_text(encoding='utf-8'))
        if document.get('constructed_test') is not True:
            fail(f'{name} 没有标明构造测试')
        if document.get('token') != TOKEN:
            fail(f'{name} 没有使用测试占位符')
    loaded = json.loads((constructed / 'result.json').read_text(encoding='utf-8'))
    if loaded.get('content') != page_text:
        fail('构造结果的 content 与已保存单页文本不一致')
    for mode in ('baseline', 'guarded'):
        default_path = out / f'{mode}-default.txt'
        bridged_path = out / f'{mode}-result-dir.txt'
        default_proc = run_builder(mode, default_path)
        bridged_proc = run_builder(mode, bridged_path, constructed)
        combined = (default_proc.stdout or '') + (default_proc.stderr or '') + (bridged_proc.stdout or '') + (bridged_proc.stderr or '')
        if leaked(combined):
            fail(f'{mode} 提问脚本的输出包含任务 token')
        if default_proc.returncode != 0 or not default_path.is_file():
            fail(f'{mode} 默认路径没有写出提问\n{redact(default_proc.stderr)}')
        if bridged_proc.returncode != 0 or not bridged_path.is_file():
            fail(f'{mode} 的 --result-dir 路径没有写出提问\n{redact(bridged_proc.stderr)}')
        default_bytes = default_path.read_bytes()
        bridged_bytes = bridged_path.read_bytes()
        if TOKEN.encode() in default_bytes or TOKEN.encode() in bridged_bytes:
            fail(f'{mode} 提问文件写入了测试 token')
        if default_bytes != bridged_bytes:
            fail(f'{mode} 的默认路径和 --result-dir 路径不一致')
        digest = hashlib.sha256(default_bytes).hexdigest()
        if digest != expected[mode]:
            fail(f'{mode} 与已记录提问哈希不一致：{digest}')
        lines.append(f'{mode}：默认路径与 --result-dir 逐字节一致，sha256 {digest}，{len(default_bytes)} 字节')


def check_result_content_is_used(out, page_text, request, status, lines):
    if SENTINEL in page_text:
        fail('测试标记与已保存文本冲突')
    directory = out / 'sentinel-content'
    reference, result = base_documents(page_text + SENTINEL, json.loads(json.dumps(request)), status)
    write_pair(directory, reference, result)
    dest = directory / 'question.txt'
    proc = run_builder('baseline', dest, directory)
    combined = (proc.stdout or '') + (proc.stderr or '')
    if leaked(combined):
        fail('content 标记测试的输出包含任务 token')
    if proc.returncode != 0 or not dest.is_file():
        fail(f'content 标记测试没有写出提问\n{redact(proc.stderr)}')
    default_bytes = (out / 'baseline-default.txt').read_bytes()
    needle = page_text.encode('utf-8')
    if default_bytes.count(needle) != 1:
        fail('默认 baseline 里的单页文本不是恰好一份')
    expected = default_bytes.replace(needle, (page_text + SENTINEL).encode('utf-8'), 1)
    if dest.read_bytes() != expected:
        fail('--result-dir 没有把 result.json 的 content 原样写入提问')
    if SENTINEL.encode('utf-8') in default_bytes:
        fail('默认路径带上了只放在构造结果里的标记')
    lines.append('--result-dir 使用 result.json 的 content；默认路径仍是仓库里的历史文本')


def check_rejections(out, page_text, request, status, lines):
    cases = [
        ('incomplete', '未完成', '结果状态不是 success', 'status', 'processing'),
        ('wrong-page', '错误页码', '请求页索引不是 5', 'pages', '6'),
        ('token-mismatch', 'token 不一致', 'token 缺失或不一致', 'token', TOKEN_OTHER),
        ('empty-text', '空文本', '不是非空文本', 'content', ''),
    ]
    for dirname, label, phrase, field, value in cases:
        directory = out / dirname
        reference, result = base_documents(page_text, json.loads(json.dumps(request)), status)
        if field == 'pages':
            reference['request']['pages'] = value
        elif field == 'token':
            result['token'] = value
        elif field == 'status':
            result['status'] = value
        elif field == 'content':
            result['content'] = value
        write_pair(directory, reference, result)
        dest = directory / 'question.txt'
        proc = run_builder('baseline', dest, directory)
        combined = (proc.stdout or '') + (proc.stderr or '')
        if leaked(combined):
            fail(f'{label} 的输出包含任务 token')
        if proc.returncode == 0 or dest.exists():
            fail(f'{label} 未被拒绝，或已经生成问题文件')
        if phrase not in redact(proc.stderr):
            fail(f'{label} 的报错不符合预期\n{redact(proc.stderr)}')
        names = sorted(path.name for path in directory.iterdir())
        if names != ['result.json', 'task-reference.json']:
            fail(f'{label} 的目录里出现了其他文件：{names}')
        lines.append(f'{label}：退出码 {proc.returncode}，未生成问题文件')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True, help='必须是还不存在的新目录')
    args = parser.parse_args()
    out = fresh_out(args.out)
    page_text, request, status = load_saved()
    expected = expected_hashes()
    out.mkdir()
    lines = [
        '构造测试使用 bohrium-pass/zeng-parser-retest-page6.txt 和 zeng-parser-retest-metadata.json。',
        'JSON 标明 constructed_test，任务 token 只使用测试占位符。',
        '本脚本不联网。',
    ]
    check_rebuild(out, page_text, request, status, expected, lines)
    check_result_content_is_used(out, page_text, request, status, lines)
    check_rejections(out, page_text, request, status, lines)
    report = '\n'.join(lines)
    if leaked(report):
        fail('检查报告包含任务 token')
    (out / 'report.txt').write_text(report + '\n', encoding='utf-8')
    print(report)


if __name__ == '__main__':
    main()
