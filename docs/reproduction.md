# 复现说明

[正文](../README.md)给出使用已保存文本、提取图结构并向玻尔提问的主要命令。下面补充重新解析和 Skill 对照。

## 重新解析第 6 页

安装 `requests`，设置 `BOHR_ACCESS_KEY`，在仓库根目录使用新目录运行：

```powershell
python bohrium-pass/parse_zeng.py submit --page-index 5 --out ./parse-run
python bohrium-pass/parse_zeng.py poll --out ./parse-run
python bohrium-pass/build_figure_question.py --mode baseline --result-dir ./parse-run --out ./parse-run/baseline.txt
```

页索引从 0 开始，`5` 对应 PDF 第 6 页；若还在排队，稍后再运行 `poll`。最后一条命令检查请求页、完成状态、非空文本及任务 token，使用本次返回的内容生成提问。`--mode guarded` 会附加原来的核验要求。不带 `--result-dir` 时使用仓库里的[已保存文本](../bohrium-pass/zeng-parser-retest-page6.txt)。

[单页记录](../bohrium-pass/zeng-parser-retest-metadata.json)的状态为 `success`，费用 5 分。此前[全文解析](../bohrium-pass/zeng-parser-metadata.json)费用 45 分；启用图片模块的尝试返回 [HTTP 403](../bohrium-pass/zeng-figure-http403.txt)。

## 本地图结构检查

```powershell
python bohrium-pass/check_fig5.py --out ./fig5-check
python bohrium-pass/check_fig5.py --blank --out ./fig5-blank
```

两个输出目录须为新目录。第一条应得到九个节点、九条边：YES 回到 Dataset，NO 指向 Final dataset。第二条生成六页空白 PDF；提取器应以非零状态退出，且不产生 `graph.json`。检查只针对本论文 Fig. 5；结果应与[原图](../materials/excerpts/zeng2020-fig5.png)和[验收标准](../bohrium-pass/zeng-figure-vector-protocol.md)对照。

## Skill 对照预检

需要已登录的 Cursor agent CLI `2026.10.19-6bbf2c4` 和 `grok-4.7-high`。在 Windows 上用新的输出目录先预检：

```powershell
$PaperStamp = Get-Date -Format 'yyyyMMdd-HHmmss'
python examples/zeng-v5/reproduce_a.py --with-skill --out "$env:TEMP/paper-with-$PaperStamp" --dry-run
python examples/zeng-v5/reproduce_a.py --out "$env:TEMP/paper-without-$PaperStamp" --dry-run
python examples/zeng-v5/reproduce_a.py --compact --with-skill --out "$env:TEMP/paper-compact-with-$PaperStamp" --dry-run
python examples/zeng-v5/reproduce_a.py --compact --out "$env:TEMP/paper-compact-without-$PaperStamp" --dry-run
```

前两条使用[原任务](../examples/zeng-v5/cases/A/task.md)，后两条使用双方都加了篇幅要求的[简洁任务](../examples/zeng-v5/cases/A/task-compact.md)。每组的 PDF 和任务哈希应相同，只有有 Skill 的一侧有 Skill 哈希。去掉 `--dry-run` 会启动模型；Agent 使用 `--sandbox disabled`。

## 模型和费用

玻尔问答请求使用 `gpt-5-nano`，保存的返回模型为 `chenkun/gpt-5-nano`；见[方法问答](../bohrium-pass/zeng-pipeline-metadata.json)、[文本比较](../bohrium-pass/zeng-figure-comparison-metadata.json)和[矢量补充](../bohrium-pass/zeng-figure-vector-metadata.json)的记录。

Skill 对照请求使用 `grok-4.7-high`。前两组有 Skill 的初始化显示 `Grok 4.7 256K High`，无 Skill 显示 `Grok 4.7 High`；简洁任务两侧均显示 `Grok 4.7 256K High`。后台权重和单次费用无法取得。原始记录分别见[有 Skill](../examples/zeng-v5/A-with-1/run-init.json)、[无 Skill](../examples/zeng-v5/A-without-1/run-init.json)、[简洁版有 Skill](../examples/zeng-v5/A-compact-with/run-init.json)及[简洁版无 Skill](../examples/zeng-v5/A-compact-without/run-init.json)。
