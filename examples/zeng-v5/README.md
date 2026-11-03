# v5 实际运行记录

案例 A 使用 [Zeng 2020 PDF](../../materials/source/zeng2020-methane-nn-md.pdf)、同一份[任务](cases/A/task.md)和运行前写好的[验收标准](cases/A/acceptance.md)。四份原始答案分别为[有 Skill 1](A-with-1/answer.md)、[无 Skill 1](A-without-1/answer.md)、[有 Skill 2](A-with-2/answer.md)和[无 Skill 2](A-without-2/answer.md)。

本教程展示 A 案例；公开仓库还收录另一篇论文和缺页材料的运行，分别保存在 `B-with`、`C-with-1` 和 `C-with-2` 目录。

运行目录保留原始答案、元数据和初始化事件；仓库另有包含任务及结束事件的 `trace-summary.jsonl`。记录已移除个人路径及会话标识。模型显示名称的差异和各次耗时见主文的对照表。

## 在原环境复跑案例 A

需要 Windows、已登录的 Cursor agent CLI `2026.10.19-6bbf2c4`，以及可调用的 `grok-4.7-high`。实验驱动使用 Python 3.11；Agent 读取 PDF 时使用 Python 3.12.8、pypdf 6.19.0 和 PyMuPDF 1.26.7。

在仓库根目录执行：

```powershell
$env:PYTHONUTF8 = '1'
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$withDir = Join-Path $env:TEMP ("paper-with-$stamp")
$withoutDir = Join-Path $env:TEMP ("paper-without-$stamp")
python examples/zeng-v5/reproduce.py --case A --with-skill --out $withDir --dry-run
python examples/zeng-v5/reproduce.py --case A --out $withoutDir --dry-run
```

两次预检应显示相同的论文和任务 SHA-256；只有有 Skill 的一侧显示 Skill SHA-256。预检不启动模型，也不创建输出目录。确认环境后，去掉两条命令末尾的 `--dry-run` 即可开始运行。

两侧分别创建新工作目录和 `answer.md`，同时保存原始流、错误输出、耗时及退出状态。对照时使用 [A 的验收标准](cases/A/acceptance.md)。Agent 会调用 Cursor 模型服务，并以 `--sandbox disabled` 在当前账号权限下运行。
