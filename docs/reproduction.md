# 复现检查、解析衔接与已记录的模型信息

[正文](../README.md)里的主路径，是用已经保存的第 6 页解析文本重建提问，从 PDF 抽出 Fig. 5 的节点和箭头，再交给玻尔。这里补充会打断阅读的衔接方式、本地检查、Skill 预检，以及仓库里已经记下的模型和费用。

下面凡是访问玻尔的命令，都是给持有密钥的读者重跑用的。成功状态、费用和 HTTP 403 来自原先保存的文件。整理这份说明时没有再提交解析，也没有再调用问答模型。

## 已保存的第 6 页文本

不带 `--result-dir` 时，[build_figure_question.py](../bohrium-pass/build_figure_question.py) 读取 [zeng-parser-retest-page6.txt](../bohrium-pass/zeng-parser-retest-page6.txt)。在仓库根目录运行：

```powershell
python bohrium-pass/build_figure_question.py --mode baseline --out ./figure-run/baseline.txt
```

`--mode guarded` 使用同一段文本，末尾加上 [zeng-figure-guarded-instruction.txt](../bohrium-pass/zeng-figure-guarded-instruction.txt) 里的那句核验要求。

这次单页解析的请求写在 [zeng-parser-retest-metadata.json](../bohrium-pass/zeng-parser-retest-metadata.json)：`textual`、`table`、`equation` 都是 2，`figure` 是 0，`pages` 是 `5`。页索引从 0 开始，所以 `5` 对应 PDF 第 6 页；`requested_page_count` 为 1。状态是 `success`，费用 5 分（`charged_amount` 为 `0.05`）。返回文本有 Fig. 5 图注和方法文字，没有图内方框标签和箭头。

更早的 9 页全文解析记在 [zeng-parser-metadata.json](../bohrium-pass/zeng-parser-metadata.json)：状态 `success`，费用 45 分，`figure_processed` 为 0。完整返回不在材料包内。同一份记录里，`figure` 设为 1、`pages` 为 `5` 的重试得到 HTTP 403，保存的错误是 [zeng-figure-http403.txt](../bohrium-pass/zeng-figure-http403.txt)。那次没有留下任务引用。

## 新解析结果经 --result-dir 进入提问

读者若要重新解析，先安装 `requests`，并设置环境变量 `BOHR_ACCESS_KEY`。[parse_zeng.py](../bohrium-pass/parse_zeng.py) 的 `--page-index` 也从 0 起。在仓库根目录、使用一个还不存在的目录：

```powershell
python bohrium-pass/parse_zeng.py submit --page-index 5 --out ./parse-run
python bohrium-pass/parse_zeng.py poll --out ./parse-run
python bohrium-pass/build_figure_question.py --mode baseline --result-dir ./parse-run --out ./parse-run/baseline.txt
```

`--page-index 5` 对应 PDF 第 6 页。省略 `--page-index` 会提交整个 PDF。`--figure` 只能是 0 或 1，默认 0。

`submit` 把这次请求写到 `parse-run/task-reference.json`。接口返回不成功时，脚本不保存任务引用。`poll` 把返回写到 `parse-run/result.json`。若状态还在排队，过一会儿再执行 `poll`。当次请求设置和费用以返回为准。

最后一条命令同时读这两份文件，通过后才把 `result.json` 里的 `content` 原文放进提问。它检查：

- 请求的 `pages` 只有一页，而且页索引是 5；
- 两份文件都有任务 token，并且相同；
- 结果状态是 `success`；
- `content` 是非空文本。

任一条件不满足时，命令以非零状态退出，不写问题文件，也不打印 token。`--mode guarded` 沿用通过检查的同一段 `content`，后面仍加上原来那句核验要求。

## 图结构检查与空白图

[check_fig5.py](../bohrium-pass/check_fig5.py) 调用 [extract_fig5_graph.py](../bohrium-pass/extract_fig5_graph.py)，读取论文第 6 页，再和 [zeng-figure-vector-protocol.md](../bohrium-pass/zeng-figure-vector-protocol.md) 里人工核对过的九个节点、九条边和 YES／NO 比较。它只检查这篇 Zeng 2020 PDF 的 Fig. 5，不联网。`--out` 必须是一个还不存在的目录；目录已经存在时，脚本退出，不写入文件。

```powershell
python bohrium-pass/check_fig5.py --out ./fig5-check
```

退出码应为 0。输出应包含 9 个节点、9 条边，以及：

```text
New data? → Dataset [YES]
New data? → Final dataset [NO]
```

退出码为 0 表示抽出的矢量与协议一致。[原图](../materials/excerpts/zeng2020-fig5.png)和 `graph.json` 仍要人工对照。

同一脚本可以在另一个新目录里生成一份六页空白 PDF，再交给同一个提取器：

```powershell
python bohrium-pass/check_fig5.py --blank --out ./fig5-blank
```

这条命令自己的退出码应为 0。它生成的空白 PDF 有 6 页。提取器的退出码为 1，报错是 `Unexpected diagram structure: 0 nodes, 0 arrows`，目录里没有 `graph.json`。

文字层那次补充可以用 [build_figure_layer.py](../bohrium-pass/build_figure_layer.py) 从同一页、同一裁剪区域重建词和坐标。它同样只读取本地 PDF，不连线。

## Skill 预检

案例 A 的四次正式运行已经保存在 `examples/zeng-v5/`。预检不启动模型。在 Windows 仓库根目录，用两个新目录：

```powershell
$PaperStamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$PaperWith = Join-Path $env:TEMP ("paper-with-$PaperStamp")
$PaperWithout = Join-Path $env:TEMP ("paper-without-$PaperStamp")
python examples/zeng-v5/reproduce_a.py --with-skill --out $PaperWith --dry-run
python examples/zeng-v5/reproduce_a.py --out $PaperWithout --dry-run
```

两次预检应给出相同的 `pdf_sha256` 和 `task_sha256`。只有有 Skill 的一侧有 `skill_sha256`。模型字段是 `grok-4.7-high`，程序字段是 `Cursor agent CLI 2026.10.19-6bbf2c4`。当前仓库里，这三项哈希分别为：

- PDF：`47987f623c3f5496bd699d905a11065078366abff6552e106e364a415ff0384e`
- 任务：`a9b010437d6a8b09791e374350609584be76128f96152bc122cf37075d02fc91`
- Skill：`54e99ecebb8c8c51f3c688cbd1fec4ddfaca5dd3225dd02e498bab8689d6c44d`

四次已保存运行的 [有 Skill 1](../examples/zeng-v5/A-with-1/meta.json)、[有 Skill 2](../examples/zeng-v5/A-with-2/meta.json)、[无 Skill 1](../examples/zeng-v5/A-without-1/meta.json)、[无 Skill 2](../examples/zeng-v5/A-without-2/meta.json) 与这些文件一致；验收标准哈希都是 `54bdd272c98162365cfee83882035f5e9dff1f6f5bcf62e0d721aefcd8107ec2`。去掉 `--dry-run` 会启动模型并创建新目录。Agent 使用 `--sandbox disabled`，按当前账号权限读取文件。整理这份说明时只做了预检，没有重跑四次回答。


补充的简洁任务在 [task-compact.md](../examples/zeng-v5/cases/A/task-compact.md)。两侧都增加同一篇幅要求，验收标准与原任务相同。加 `--compact` 选择这个任务：

```powershell
$CompactWith = Join-Path $env:TEMP ("paper-compact-with-$PaperStamp")
$CompactWithout = Join-Path $env:TEMP ("paper-compact-without-$PaperStamp")
python examples/zeng-v5/reproduce_a.py --compact --with-skill --out $CompactWith --dry-run
python examples/zeng-v5/reproduce_a.py --compact --out $CompactWithout --dry-run
```

两侧应给出相同的论文和任务哈希；只有有 Skill 的一侧有 Skill 哈希。去掉 `--dry-run` 会实际调用模型。

## 模型和费用

问答接口写成 `gpt-5-nano` 时，保存的返回模型都是 `chenkun/gpt-5-nano`。费用和 token 以各文件原记录为准。

| 已保存调用 | 模型 | 记录中的用量或费用 | 出处 |
| --- | --- | --- | --- |
| 方法四行问答 | `chenkun/gpt-5-nano` | `prompt_tokens` 267；返回里的 `completion_tokens` 1895，其中 `reasoning_tokens` 1728。这份返回没有费用分数字段 | [元数据](../bohrium-pass/zeng-pipeline-metadata.json)、[完整返回](../bohrium-pass/zeng-pipeline-response-public.json) |
| 只有第 6 页文本的基础问答 | `chenkun/gpt-5-nano` | `prompt_tokens` 1553 | [比较记录](../bohrium-pass/zeng-figure-comparison-metadata.json) |
| 加核验要求 | `chenkun/gpt-5-nano` | `prompt_tokens` 1587 | 同上 |
| 图内文字和坐标 | `chenkun/gpt-5-nano` | `prompt_tokens` 1962；文字层 31 个词，PyMuPDF 1.26.7 | [文字层记录](../bohrium-pass/zeng-figure-text-layer-metadata.json) |
| 矢量结构，运行 1 和运行 2 | `chenkun/gpt-5-nano` | 各次 `prompt_tokens` 1796 | [矢量记录](../bohrium-pass/zeng-figure-vector-metadata.json) |
| 第 6 页 Uni-Parser | 解析接口，无聊天模型名 | 状态 `success`，5 分 | [单页元数据](../bohrium-pass/zeng-parser-retest-metadata.json) |
| 9 页 Uni-Parser | 同上 | 状态 `success`，45 分；`figure=1` 的重试为 HTTP 403 | [全文元数据](../bohrium-pass/zeng-parser-metadata.json)、[403 记录](../bohrium-pass/zeng-figure-http403.txt) |
| Skill 对照四次 | 传入 `grok-4.7-high` | 费用字段均为“无法取得”。耗时 625.5 s、609.9 s、363.2 s、412.0 s | 上文四份 `meta.json` |

有 Skill 的两次初始化显示名是 `Grok 4.7 256K High`，无 Skill 的两次是 `Grok 4.7 High`。原始记录在：[有 Skill 1](../examples/zeng-v5/A-with-1/run-init.json)、[有 Skill 2](../examples/zeng-v5/A-with-2/run-init.json)、[无 Skill 1](../examples/zeng-v5/A-without-1/run-init.json)、[无 Skill 2](../examples/zeng-v5/A-without-2/run-init.json)。服务未公开权重版本。

Bohr CLI 的已保存版本是 2.9.21，见方法问答完整返回里的 `cli_version`。正文所记的 Node.js 24.11.1 和 Python 3.11.14 是当初核对图结构时的环境；PyMuPDF 1.26.7 也写在图结构 JSON 里。
