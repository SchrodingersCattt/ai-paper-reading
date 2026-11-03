# 用 AI 读懂一篇机器学习势论文

第一次读机器学习势论文，我想弄清楚：**训练用的结构从哪里来，能量和力由谁计算，神经网络又学到了什么？**

Zeng 等人把甲烷燃烧的参考数据集画在第 6 页 Fig. 5。只把第 6 页解析文本交给玻尔时，它写明看不到方框标签，并按方法文字列出 16 步。补入已经与原图核对过的节点和箭头后，两次回答都写出 9 条箭头，YES 回到 Dataset，NO 指向 Final dataset。

图结构对齐后，方法含义仍要回原文核对：一次回答把本征谱与特征向量混同，另一次把去冗余后的数据集称为初始数据集；两次都没有明确说出量化计算的参考值是能量和力。

论文：Zeng et al., [*Complex reaction processes in combustion unraveled by neural network-based molecular dynamics simulation*](https://doi.org/10.1038/s41467-020-19497-z), *Nature Communications* **11**, 5713 (2020)。[论文全文](materials/source/zeng2020-methane-nn-md.pdf)按 CC BY 4.0 分享；本文页码均为 PDF 页码。

## 这篇论文里的势函数学了什么

论文想用分子动力学观察甲烷燃烧中的反应。作者先用 ReaxFF 反应性 MD 采样，为每个原子构建 5 Å 分子簇，去除冗余后，再用四个神经网络势的短轨迹寻找要补充的构型。第 7 页的加入条件是四个模型对同一原子力的预测彼此不一致，且 `0.5 eV/Å < error < 1.0 eV/Å`；更新持续到四个模型的预测始终一致。最终数据集中每个结构的参考能量和原子力，由 Gaussian 16 在 MN15/6-31G\*\* 水平计算。这些数据训练 DeepPot-SE，描述符截断为 6.0 Å，并从 1.0 Å 平滑衰减到 6.0 Å（第 6—7 页）。

势函数把原子构型映射到势能，原子力是势能对坐标的负梯度。训练完成后，MD 用预测的力推进原子，作者再从轨迹中分析反应路径。论文展示的生产模拟是 **100 个 CH₄、200 个 O₂，3000 K、0.25 g/cm³**，运行 1 ns，步长 0.1 fs（第 2 页）。这条轨迹没有展示约 1 atm、低于 2000 K 的稀释甲烷—空气火焰；换到该条件，还要检查目标体系的数据覆盖和验证结果。

## 用玻尔拆解论文的方法

采样、能量和力、5 Å、6.0 Å 这四件事，有一次真实问答。输入是人工选出的第 6、7 页原文：[提示](bohrium-pass/zeng-pipeline-prompt.txt) 中的 P6-13a、P6-13b 是 [原块](bohrium-pass/zeng-parser-key-blocks.json) 第 6 页 order 13 的两处选段，P7-10a、P7-10b 是第 7 页 order 10 的两处选段。调用的是 Bohr CLI 2.9.21 的 `bohr chat`，[接口返回](bohrium-pass/zeng-pipeline-response-public.json)和[模型记录](bohrium-pass/zeng-pipeline-metadata.json)里的模型都是 `chenkun/gpt-5-nano`。[回答](bohrium-pass/zeng-pipeline-answer.txt) 按块号写了四句：

- P6-13a：`使用基于 ReaxFF 的反应性分子动力学模拟来采样初始数据集。`
- P7-8：`最终数据集中每个结构的势能和原子力通过 Gaussian 16 软件在 MN15/6-31G** 水平计算。`
- P6-13b：`截断半径设为 5 Å，用于构建以该原子为中心、包含其周围物种的分子簇。`
- P7-10b：`截断半径设为 6.0 Å，描述子在 1.0 到 6.0 Å 间平滑衰减。`

回答里的两个“截断半径”分别用于构建采样分子簇和确定 DeepPot-SE 的描述符范围，不能当作同一个参数。

图的顺序要另看。我用 Bohrium Uni-Parser 解析 9 页 PDF，设置 `textual=2`、`table=2`、`equation=2`、`figure=0`。任务返回 `success`，本次费用 45 分。第 6 页[实际返回](bohrium-pass/zeng-parser-retest-page6.txt)包含 Fig. 5 图注和方法文字，没有图里的方框标签与箭头；单独复跑第 6 页，缺口仍在，费用 5 分。之后尝试 `figure=1`，本次请求返回 [HTTP 403](bohrium-pass/zeng-figure-http403.txt)。[请求和状态](bohrium-pass/zeng-parser-metadata.json)均已保存。

同一个问题使用三种输入，四次返回的模型都是 `chenkun/gpt-5-nano`。问题是：“请列出这篇论文 Fig. 5 图中每个方框的名称及箭头顺序，并给出依据。用中文回答。”

| 给玻尔的材料 | 实际回答 | 对照原图 |
| --- | --- | --- |
| 第 6 页解析文本，没有箭头 | 写明看不到方框标签，按方法文字推断 16 步 | 原图有 9 个流程节点，推测不能当作逐框转录。[基础回答](bohrium-pass/zeng-figure-baseline-answer.txt) |
| 解析文本加图中文字坐标，没有箭头 | 把 Active learning 排成流程节点，漏掉 Redundancy removal → Dataset | Active learning 是区域名称，原图有被漏掉的箭头。[文字坐标回答](bohrium-pass/zeng-figure-text-layer-answer.txt) |
| 解析文本加已核对的节点和箭头 | 两次都列对 9 条箭头和 YES／NO 分支 | 箭头已经写在[输入](bohrium-pass/zeng-figure-vector-supplement.txt)里；方法解释仍有错误。[运行 1](bohrium-pass/zeng-figure-vector-answer-1.txt)、[运行 2](bohrium-pass/zeng-figure-vector-answer-2.txt) |

后两次的方法解释与原文的差异见下节和[核查记录](bohrium-pass/zeng-figure-vector-review.md)。

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

在这个 PDF 中，方框、文字和箭头都保留为可读取的对象。[提取脚本](bohrium-pass/extract_fig5_graph.py)先按图的页面坐标找到填充形状，再用文字位置识别节点；它识别箭头端部的小三角形，根据尖端所在节点和箭头范围附近的节点确定方向，最后按邻近位置关联 YES／NO。节点或分支存在歧义时，脚本报错并要求回看原图。[节点、坐标和九条边](bohrium-pass/zeng-figure-vector-graph.json)与原图逐条核对过。脚本使用的区域和尺寸阈值是按这张 Fig. 5 写的。

箭头对上之后，方法用语还要再对原文。[运行 1](bohrium-pass/zeng-figure-vector-answer-1.txt)把“特征谱”和“特征向量”并列为近义表述，原文第 6 页写的是用于聚类的 eigen-spectrum。[运行 2](bohrium-pass/zeng-figure-vector-answer-2.txt)把去冗余后的数据集称为初始数据集，而原文先把采样得到的约 2250 万个结构称为初始数据集，再去除冗余。两次都没有在 QM 环节明确写出参考值是能量和力，需补看第 7 页。[逐项核对记录](bohrium-pass/zeng-figure-vector-review.md)保留了全部结果。

读方法段时，下面几组数也要分开：

| 数值 | 在论文中的作用 | 位置 |
| --- | --- | --- |
| 5 Å | 为采样构型中的每个原子构建局部分子簇 | 第 6 页 |
| 6.0 Å | DeepPot-SE 描述符的截断半径，描述符从 1.0 Å 平滑衰减到 6.0 Å | 第 7 页 |
| `0.5 eV/Å < error < 1.0 eV/Å` | 四个模型的力预测彼此不一致时，按这个开区间把分子簇加入数据集 | 第 7 页 |
| 0.12 eV/Å | 模型预测与参考计算之间的原子力 MAE | 第 2 页 |

开区间两端都不取等号。误差达到 1.0 eV/Å 时，正文没有写出这些结构如何处理。

## Skill 带来了哪些变化

我把“解释方法、对照原文、再判断用途”的步骤整理成 [method-fit-check](skill/SKILL.md)。用同一篇 Zeng 论文和同一任务，各运行两次有 Skill、两次无 Skill，调用参数均为 `grok-4.7-high`；[任务](examples/zeng-v5/cases/A/task.md)和[验收标准](examples/zeng-v5/cases/A/acceptance.md)在运行前写好。

| 运行 | 对论文未明确说明的信息如何处理 | 耗时 |
| --- | --- | ---: |
| [有 Skill 1](examples/zeng-v5/A-with-1/answer.md) | 训练集元素范围和压力数值标为未说明 | 625.5 s |
| [无 Skill 1](examples/zeng-v5/A-without-1/answer.md) | 将训练集写成确定的 C/H/O，并另做压力估算 | 363.2 s |
| [有 Skill 2](examples/zeng-v5/A-with-2/answer.md) | 将惰性气体适用性留待验证，压力数值标为未说明 | 609.9 s |
| [无 Skill 2](examples/zeng-v5/A-without-2/answer.md) | 将参考集写成确定没有惰性气体，并估算密度和比例 | 412.0 s |

四份回答都解释了主要方法，并判断论文没有展示目标火焰条件。有 Skill 的两次没有把元素范围或惰性气体适用性写成定论，无 Skill 的两次写成了确定结论；有 Skill 的两次也更慢。四次传入的模型 ID 相同。有 Skill 的初始化显示名是 `Grok 4.7 256K High`（[1](examples/zeng-v5/A-with-1/run-init.json)、[2](examples/zeng-v5/A-with-2/run-init.json)），无 Skill 的显示名是 `Grok 4.7  High`，4.7 与 High 之间有两个空格（[1](examples/zeng-v5/A-without-1/run-init.json)、[2](examples/zeng-v5/A-without-2/run-init.json)）。服务未公开权重版本，显示名又不同，耗时和措辞差里还可能有后端配置差异。

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

`graph.json` 应列出 9 个节点和 9 条箭头，YES 返回 Dataset，NO 指向 Final dataset。对照原图和[事先写好的验收标准](bohrium-pass/zeng-figure-vector-protocol.md)检查箭头与分支；表述可以和仓库里已有的两次回答不同。

要重新调用 Uni-Parser，安装 `requests` 并配置 `BOHR_ACCESS_KEY`，再运行 `python bohrium-pass/parse_zeng.py submit --out ./parse-run` 和 `python bohrium-pass/parse_zeng.py poll --out ./parse-run`。首次仍在排队时，稍后再次执行 `poll`。请求设置与费用以实际返回为准。

## 论文与运行记录

| 内容 | 位置 |
| --- | --- |
| 论文全文与授权 | [Zeng 2020 PDF](materials/source/zeng2020-methane-nn-md.pdf)、[许可说明](materials/LICENSE.md) |
| 方法四问 | [提示](bohrium-pass/zeng-pipeline-prompt.txt)、[选出的原块](bohrium-pass/zeng-parser-key-blocks.json)、[回答](bohrium-pass/zeng-pipeline-answer.txt)、[模型记录](bohrium-pass/zeng-pipeline-metadata.json)、[接口返回](bohrium-pass/zeng-pipeline-response-public.json) |
| 玻尔解析与基础问答 | [设置和状态](bohrium-pass/zeng-parser-metadata.json)、[第 6 页结果](bohrium-pass/zeng-parser-retest-page6.txt)、[基础回答](bohrium-pass/zeng-figure-baseline-answer.txt) |
| 图中文字与矢量结构 | [文字层回答](bohrium-pass/zeng-figure-text-layer-answer.txt)、[节点和箭头](bohrium-pass/zeng-figure-vector-graph.json)、[提取脚本](bohrium-pass/extract_fig5_graph.py) |
| 两次补充问答与核查 | [运行 1](bohrium-pass/zeng-figure-vector-answer-1.txt)、[运行 2](bohrium-pass/zeng-figure-vector-answer-2.txt)、[运行前标准](bohrium-pass/zeng-figure-vector-protocol.md)、[核查](bohrium-pass/zeng-figure-vector-review.md)、[模型和哈希](bohrium-pass/zeng-figure-vector-metadata.json) |
| Skill A 对照 | [任务](examples/zeng-v5/cases/A/task.md)、[验收标准](examples/zeng-v5/cases/A/acceptance.md)、[复现脚本](examples/zeng-v5/reproduce.py) |

论文和已有软件归原作者所有；本项目整理了阅读问题、图结构提取、提示、核查记录及 Skill 对照。
