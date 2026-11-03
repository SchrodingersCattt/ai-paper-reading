# 用 AI 读懂一篇机器学习势论文

第一次读机器学习势论文，我想弄清楚：**训练用的结构从哪里来，能量和力由谁计算，神经网络又学到了什么？**

这里用 Zeng 等人的甲烷燃烧论文做例子。论文第 6 页 Fig. 5 画出了数据集构建过程；我先让玻尔解释，再用原图核对。遇到图内箭头没有进入解析文本的问题后，我从 PDF 的矢量路径提取节点和连线，补充给玻尔，重新检查它的回答。

你可以跟着复现这个案例，得到一条从**采样、量化标注、势函数训练到分子动力学**的方法链，也能看到哪些结论需要回到原图和方法段确认。

论文：Zeng et al., [*Complex reaction processes in combustion unraveled by neural network-based molecular dynamics simulation*](https://doi.org/10.1038/s41467-020-19497-z), *Nature Communications* **11**, 5713 (2020)。[论文全文](materials/source/zeng2020-methane-nn-md.pdf)按 CC BY 4.0 分享；本文页码均为 PDF 页码。

## 这篇论文里的势函数学了什么

论文想用分子动力学观察甲烷燃烧中的反应。作者先用 ReaxFF 反应性 MD 生成原子构型，去除冗余后，再用多个神经网络和短轨迹寻找需要补充的构型。最终数据集中每个结构的参考能量和原子力，由 Gaussian 16 在 MN15/6-31G\*\* 水平计算（第 6—7 页）。

这些构型、能量和力被用来训练 DeepPot-SE 势。势函数把原子构型映射到势能；原子力是势能对坐标的负梯度。训练完成后，MD 用预测的力推进原子运动，作者再从轨迹中分析反应路径。

论文展示的生产模拟是 **100 个 CH₄、200 个 O₂，3000 K、0.25 g/cm³** 的周期性体系，运行 1 ns，步长 0.1 fs（第 2 页）。如果我的目标是约 1 atm、低于 2000 K 的稀释甲烷—空气火焰，这条轨迹没有展示目标条件；还需要检查目标体系的数据覆盖和验证结果。

## 用玻尔拆解论文的方法

我用 Bohrium Uni-Parser 解析 9 页 PDF，设置 `textual=2`、`table=2`、`equation=2`、`figure=0`。任务返回 `success`，本次费用 45 分。第 6 页[实际返回](bohrium-pass/zeng-parser-retest-page6.txt)包含 Fig. 5 图注和方法文字，却没有图里的方框标签与箭头；单独复跑第 6 页得到同样的缺口，费用 5 分。之后尝试 `figure=1`，本次请求返回 [HTTP 403](bohrium-pass/zeng-figure-http403.txt)。[请求和状态](bohrium-pass/zeng-parser-metadata.json)均已保存。

我把第 6 页返回文本交给玻尔，问：“请列出这篇论文 Fig. 5 图中每个方框的名称及箭头顺序，并给出依据。用中文回答。”[基础回答](bohrium-pass/zeng-figure-baseline-answer.txt)说明看不到原图标签，随后依据方法文字推测了 16 个步骤。它讲到了采样和聚类，却不能用于逐框转录图示。

我继续做了两种补充，使用同一个 `gpt-5-nano` 接口，实际返回模型均为 `chenkun/gpt-5-nano`：

| 给玻尔的补充材料 | 实际结果 |
| --- | --- |
| 原 PDF 图内的文字及坐标 | [回答](bohrium-pass/zeng-figure-text-layer-answer.txt)找到了多个标签，但将区域名称 Active learning 排进线性流程，也漏掉 Redundancy removal → Dataset。 |
| 从同一 PDF 提取的节点、箭头和 YES／NO 分支 | [运行 1](bohrium-pass/zeng-figure-vector-answer-1.txt)和[运行 2](bohrium-pass/zeng-figure-vector-answer-2.txt)均列对 9 条箭头及两个分支。 |

后两种输入增加了原图信息，是对材料获取方式的比较。节点和箭头已经写在补充材料中，模型据此组织解释；这两次结果不能说明模型仅凭图注就读出了图形。

## 回到原文核对关键解释

![Zeng 等人论文第 6 页 Fig. 5，参考数据集构建流程](materials/excerpts/zeng2020-fig5.png)

*Zeng 等人 Fig. 5 裁图，CC BY 4.0。*

对照原图，主线是：

```text
Molecular system → Sampling with ReaxFF → Redundancy removal → Dataset
Dataset → QM calculation → NN training → Re-sampling → New data?
New data? ──YES──→ Dataset        继续循环
New data? ──NO───→ Final dataset  结束
```

在这个 PDF 中，方框、文字和箭头都保留为可读取的对象。[提取脚本](bohrium-pass/extract_fig5_graph.py)先按图的页面坐标找到填充形状，再用文字位置识别节点；它识别箭头端部的小三角形，根据尖端所在节点和箭头范围附近的节点确定方向，最后按邻近位置关联 YES／NO。节点或分支存在歧义时，脚本报错并要求回看原图。[节点、坐标和九条边](bohrium-pass/zeng-figure-vector-graph.json)与原图逐条核对过。

脚本使用的是本图的区域和尺寸阈值，适用于这份带文字层和矢量路径的 PDF。扫描页或把整张图存成图片的论文，需要先通过其他方式读取图形。

图结构对了，还要检查模型对方法的解释：[运行 1](bohrium-pass/zeng-figure-vector-answer-1.txt)把“特征谱”和“特征向量”并列为近义表述，原文第 6 页写的是用于聚类的 eigen-spectrum；[运行 2](bohrium-pass/zeng-figure-vector-answer-2.txt)把去冗余后的数据集称为初始数据集，而原文先把采样得到的约 2250 万个结构称为初始数据集，再去除冗余。两次都没有在 QM 环节明确写出参考值是能量和力，需补看第 7 页。[逐项核对记录](bohrium-pass/zeng-figure-vector-review.md)保留了全部结果。

读方法段时，下面几组数也要分开：

| 数值 | 在论文中的作用 | 位置 |
| --- | --- | --- |
| 5 Å | 为采样构型中的每个原子构建局部分子簇 | 第 6 页 |
| 6 Å | DeepPot-SE 描述符的截断半径 | 第 7 页 |
| 0.5—1.0 eV/Å | 四个模型的力预测出现该范围差异时，用于选择补充构型 | 第 7 页 |
| 0.12 eV/Å | 模型预测与参考计算之间的原子力 MAE | 第 2 页 |

前两项属于不同步骤；后两项分别用于选取构型和报告预测误差，不能互换。

## Skill 带来了哪些变化

我把“解释方法、对照原文、再判断用途”的步骤整理成 [method-fit-check](skill/SKILL.md)。用同一篇 Zeng 论文和同一任务，各运行两次有 Skill、两次无 Skill，调用参数均为 `grok-4.7-high`；[任务](examples/zeng-v5/cases/A/task.md)和[验收标准](examples/zeng-v5/cases/A/acceptance.md)在运行前写好。

| 运行 | 对论文未明确说明的信息如何处理 | 耗时 |
| --- | --- | ---: |
| [有 Skill 1](examples/zeng-v5/A-with-1/answer.md) | 训练集元素范围和压力数值标为未说明 | 625.5 s |
| [无 Skill 1](examples/zeng-v5/A-without-1/answer.md) | 将训练集写成确定的 C/H/O，并另做压力估算 | 363.2 s |
| [有 Skill 2](examples/zeng-v5/A-with-2/answer.md) | 将惰性气体适用性留待验证，压力数值标为未说明 | 609.9 s |
| [无 Skill 2](examples/zeng-v5/A-without-2/answer.md) | 将参考集写成确定没有惰性气体，并估算密度和比例 | 412.0 s |

四份回答都解释了主要方法，并判断论文没有展示目标火焰条件。有 Skill 的两次更谨慎地处理了训练集元素范围，也都更慢。四次传入的模型 ID 相同，但有 Skill 的初始化显示名带 `256K`，无 Skill 的显示名没有；服务未公开权重版本，因此不能排除后端配置差异的影响。

重跑对照需要已登录的 Cursor agent CLI `2026.10.19-6bbf2c4` 和 `grok-4.7-high`。在 Windows 仓库根目录先预检两个独立目录：

```powershell
$PaperStamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$PaperWith = Join-Path $env:TEMP ("paper-with-$PaperStamp")
$PaperWithout = Join-Path $env:TEMP ("paper-without-$PaperStamp")
python examples/zeng-v5/reproduce.py --case A --with-skill --out $PaperWith --dry-run
python examples/zeng-v5/reproduce.py --case A --out $PaperWithout --dry-run
```

两次预检应给出相同的 PDF 和任务哈希，只有有 Skill 的一侧有 Skill 哈希。去掉 `--dry-run` 会启动模型并创建新目录；Agent 使用 `--sandbox disabled`，按当前账号权限读取文件。

## 在自己的论文上复用

先选一个具体问题，再检查 AI 实际拿到了什么。遇到流程图时，可按这个顺序读：

1. 让玻尔解释正文，要求标出页码；同时检查解析结果是否含有图注、图内文字和连线。
2. 如果 PDF 保留矢量图形，提取节点和箭头，和原图核对；如果只有文字，先核对文字，连线直接看原图。
3. 让模型根据核对过的材料解释步骤，再用方法段检查数据来源、参数用途和适用条件。

复跑本例需要 Windows、Python、Node.js、已登录的 Bohr CLI 和能调用 `gpt-5-nano` 的玻尔账号。下面的问答使用仓库中保存的第 6 页解析文本；图结构从论文 PDF 重新提取。本次图形提取使用 Python 3.12.8、PyMuPDF 1.26.7，也在 Python 3.11.14 下核对了同样的结果；Bohr CLI 为 2.9.21，Node.js 为 24.11.1。

在仓库根目录运行：

```powershell
python -m pip install PyMuPDF==1.26.7
npm install -g @dptech-corp/bohr-cli@2.9.21
bohr auth login

python bohrium-pass/extract_fig5_graph.py --pdf materials/source/zeng2020-methane-nn-md.pdf --out ./figure-run
python bohrium-pass/build_figure_question.py --mode baseline --out ./figure-run/baseline.txt
python bohrium-pass/build_vector_prompt.py --baseline ./figure-run/baseline.txt --graph ./figure-run/graph.json --out ./figure-run

$BohrEntry = Join-Path ((npm root -g).Trim()) '@dptech-corp/bohr-cli/run.js'
$FigureQuestion = Get-Content -Raw -Encoding utf8 './figure-run/vector-prompt.txt'
node $BohrEntry chat $FigureQuestion --model gpt-5-nano --output json
```

`graph.json` 应列出 9 个节点和 9 条箭头，YES 返回 Dataset，NO 指向 Final dataset；然后对照原图和[事先写好的验收标准](bohrium-pass/zeng-figure-vector-protocol.md)检查回答。重跑模型可能得到不同表述。

要重新调用 Uni-Parser，安装 `requests` 并配置 `BOHR_ACCESS_KEY`，再运行 `python bohrium-pass/parse_zeng.py submit --out ./parse-run` 和 `python bohrium-pass/parse_zeng.py poll --out ./parse-run`。首次仍在排队时，稍后再次执行 `poll`。请求设置与费用以实际返回为准。

## 论文与运行记录

| 内容 | 位置 |
| --- | --- |
| 论文全文与授权 | [Zeng 2020 PDF](materials/source/zeng2020-methane-nn-md.pdf)、[许可说明](materials/LICENSE.md) |
| 玻尔解析与基础问答 | [设置和状态](bohrium-pass/zeng-parser-metadata.json)、[第 6 页结果](bohrium-pass/zeng-parser-retest-page6.txt)、[基础回答](bohrium-pass/zeng-figure-baseline-answer.txt) |
| 图中文字与矢量结构 | [文字层回答](bohrium-pass/zeng-figure-text-layer-answer.txt)、[节点和箭头](bohrium-pass/zeng-figure-vector-graph.json)、[提取脚本](bohrium-pass/extract_fig5_graph.py) |
| 两次补充问答与核查 | [运行 1](bohrium-pass/zeng-figure-vector-answer-1.txt)、[运行 2](bohrium-pass/zeng-figure-vector-answer-2.txt)、[运行前标准](bohrium-pass/zeng-figure-vector-protocol.md)、[核查](bohrium-pass/zeng-figure-vector-review.md)、[模型和哈希](bohrium-pass/zeng-figure-vector-metadata.json) |
| Skill A 对照 | [任务](examples/zeng-v5/cases/A/task.md)、[验收标准](examples/zeng-v5/cases/A/acceptance.md)、[复现脚本](examples/zeng-v5/reproduce.py) |

论文和已有软件归原作者所有；本项目整理了阅读问题、图结构提取、提示、核查记录及 Skill 对照。
