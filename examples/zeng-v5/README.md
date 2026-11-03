# v5 实际运行记录

核心案例 A 使用 [Zeng 2020 PDF](../../materials/source/zeng2020-methane-nn-md.pdf)、同一份[任务](cases/A/task.md)和运行前写好的[验收标准](cases/A/acceptance.md)。四次均传入 `grok-4.7-high`，使用 Cursor agent CLI 2026.10.19-6bbf2c4 和相同工具权限；每次使用独立目录。

| 运行 | 结果 | 时间 |
| --- | --- | ---: |
| [A-with-1](A-with-1/answer.md) | 方法、误差和条件符合标准；压力及未报告的训练集范围标为未说明。 | 625.5 s |
| [A-without-1](A-without-1/answer.md) | 核心方法正确；另估算压力，并把训练集写成确定的 C/H/O。 | 363.2 s |
| [A-with-2](A-with-2/answer.md) | 方法、误差和条件符合标准；压力未补算，目标用途待验证。 | 609.9 s |
| [A-without-2](A-without-2/answer.md) | 核心方法正确；未补压力数值，另外估算密度，并将参考集中的惰性气体写成确定不存在。 | 412.0 s |

四份都判断目标工况未被论文展示。两份有 Skill 回答都保留训练集元素范围未明确报告这一边界；两份无 Skill 回答把它说得更确定。两次有 Skill 的耗时均高于对应无 Skill 运行。

启动参数相同，但两份有 Skill 的初始化显示 `Grok 4.7 256K High`，两份无 Skill 显示 `Grok 4.7 High`。事后查到的模型列表没有单列 256K ID；服务未公布权重版本，无法确认这些历史调用的后端配置是否完全一致。每个运行目录保留实际初始化事件 `run-init.json` 和元数据；仓库中另有包含用户任务及结束事件的 `trace-summary.jsonl`。这些记录已去掉个人路径和会话标识。

变更论文后，[B-with](B-with/answer.md) 区分了 Wen 2020 论文中的 DFT 数据集、不含金刚石的检测势以及加入金刚石后的重拟合势，耗时 344.6 s。它另外推测“如果检测势已用金刚石训练，图 5a 就不会出现约四倍差异”；原文直接展示的是具体一次重拟合后的下降，这句反事实比观察更强。核查用 [Wen 2020 原文第 5、6 页](../../materials/excerpts/wen2020-original-pages5-6.pdf)和[第 8 页数据集说明](../../materials/excerpts/wen2020-page8-dataset.md)。

[C-with-1](C-with-1/answer.md) 和 [C-with-2](C-with-2/answer.md) 使用从 Zeng PDF 构造的[前两页](../../materials/source/zeng2020-constructed-pages1-2.pdf)，分别耗时 450.5 和 373.9 s，均以“材料不足停止”结束。两份都指出缺少 Methods，列出待查内容，并说明不能从现有两页确定后文章节页码。事先标准写了完整论文的第 6—7 页；模型只拿到前两页，没有猜这个页码。

各案例的任务和事先标准在 [cases/](cases/)；完整模型答案均保持原样。更完整的七次工具事件和证据索引随 Skill 比赛提交包保存。

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

两侧会分别创建新工作目录和 `answer.md`，同时保存原始流、错误输出、耗时及退出状态。对照时使用 [A 的验收标准](cases/A/acceptance.md)。Agent 会调用 Cursor 模型服务，并以 `--sandbox disabled` 在当前账号权限下运行。
