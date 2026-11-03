# 用 AI 读懂一篇机器学习势论文

读机器学习势论文时，最容易卡住的地方是：数据从哪里来，模型到底学了什么，论文中的误差又能说明什么？

这篇教程用 Zeng 等人的甲烷燃烧研究走一遍阅读过程。我们把论文中的方法和结果摘录交给玻尔，请它拆解研究流程，再回到原文核对数字和模拟条件。读完后，你可以用同一组问题去读自己的论文。

论文：[Complex reaction processes in combustion unraveled by neural network-based molecular dynamics simulation](https://doi.org/10.1038/s41467-020-19497-z)，*Nature Communications* **11**, 5713 (2020)。[仓库里的 PDF](materials/source/zeng2020-methane-nn-md.pdf) 与出版方论文相同，按 Creative Commons Attribution 4.0 分享。下面的页码都指 PDF 页码。

## 这篇论文里的势函数学了什么

这篇论文想用分子动力学观察甲烷燃烧中的反应过程。作者先构造参考数据，再训练一个神经网络势，用它计算模拟过程中的能量和原子受力。

把论文的 Fig. 5 和 Methods 连起来看，主要步骤是：

1. **采样构型。** 用 ReaxFF 反应性分子动力学生成初始结构，并对结构去冗余；随后通过多个神经网络模型的短时模拟补充数据（第 6—7 页）。
2. **计算参考值。** 用 Gaussian 16 在 MN15/6-31G\*\* 水平计算构型的能量和原子力，作为模型训练的参考（第 7 页）。
3. **训练势函数。** 使用 DeePMD-kit 训练 DeepPot-SE 模型，训练损失包含能量误差和力误差（第 7 页）。
4. **运行和检查模拟。** 作者比较了模型与参考计算的能量和力，并用势函数模拟甲烷与氧气的反应轨迹（第 2 页）。

因此，ReaxFF 和量化计算虽然都出现在数据制备流程里，分工不同：前者帮助找到构型，后者为选出的构型提供能量和力的参考值。这个区别也适用于阅读其他势函数论文。

## 用玻尔拆解论文的方法

我把 PDF 第 2、6、7 页中与方法和结果有关的摘录交给玻尔，依次问它：

- ReaxFF、量化计算和 DeepPot-SE 分别做什么？模型学到什么？
- 5 Å 和 6 Å 各属于哪一步？
- 训练集、测试集的能量误差和原子力误差各是多少？
- 论文展示的模拟，是否覆盖约 1 atm、低于 2000 K 的稀释甲烷—空气火焰？

完整输入在 [prompt](bohrium-pass/zeng-prompt.txt)，实际返回在 [response](bohrium-pass/zeng-response-public.json)。本次调用使用 Bohr CLI 2.9.17，请求模型 `gpt-5-nano`，返回模型名为 `chenkun/gpt-5-nano`。公开返回移除了包含账户信息的计费字段，回答正文保持原样。输入是人工选取的摘录，页码随摘录给出；这次调用不包含 PDF 上传或自动定位全文的步骤。

玻尔把 5 Å 与 6 Å 分别对应到局部簇构建和模型描述符，也列出了训练集、测试集的能量误差。它把量化计算结果称为“作为训练目标的真实值”。对照原文，更具体的说法是：这些量是 **MN15/6-31G\*\* 水平计算得到的参考能量和力**。知道参考值的来源，才能理解模型拟合的对象。

在干净目录中用同一提示复跑，返回保留了这些主要数字，却把 1 ns 的 NVT 轨迹称为“蒸发阶段”。论文第 2 页描述的是甲烷燃烧的反应性 MD，并未将这段轨迹称为蒸发。[第二次返回](bohrium-pass/zeng-retest-public.json)保留了原话。核对数字时，也要核对它所对应的过程。

## 回到原文核对关键解释

| 要核对的问题 | 原文中的信息 | 阅读时怎么用 |
| --- | --- | --- |
| 数据从哪里来？ | 第 6 页先用 ReaxFF 采样，第 7 页再用量化计算得到能量和力。 | 将采样方法与参考标签来源分别记下来。 |
| 两个截断半径是什么？ | 第 6 页的 **5 Å** 用于构建以原子为中心的局部簇；第 7 页的 **6 Å** 用于模型描述符。 | 即使单位相同，也要对应各自的步骤。 |
| 误差如何报告？ | 第 2 页的训练集与测试集能量 MAE 分别为 **0.04、0.14 eV/atom**；原子力 MAE 为 **0.12 eV/Å**。 | 先记指标、数据集和单位，再判断数字代表什么。 |
| 论文实际模拟了什么？ | 第 2 页使用 **100 CH₄ + 200 O₂、3000 K、0.25 g/cm³** 的体系，NVT 轨迹长 1 ns、时间步长 0.1 fs。 | 将论文条件与你的体系、温度和组成逐项比较。 |

例如，约 1 atm、低于 2000 K 的稀释甲烷—空气火焰与论文展示的条件不同；论文在这里展示的轨迹不能直接回答该工况下的反应路径。第 3 页也把使条件更接近实验的工作留给后续研究。模型能否用于新工况，还要核查目标体系相关的数据与验证。

这些项目的原文位置和来源摘录整理在 [核查记录](evidence/zeng-reading.md)。

## Skill 带来了哪些变化

之前用同一篇论文做过一个更窄的问题：判断论文方法能否用于实验室稀释甲烷—空气火焰。三次使用 `grok-4.7-high` 和 Cursor agent CLI 2026.10.19，使用相同任务与 PDF；其中一次加载了 `method-fit-check-v3`，另外两次没有加载 Skill。

| 运行 | 结论与记录 | 耗时 |
| --- | --- | ---: |
| [有 Skill](examples/zeng-v3/with/answer.md) | 判断目标条件不覆盖；给出页码、1 ns 和 0.1 fs。 | 375.5 s |
| [无 Skill 1](examples/zeng-v3/without-1/answer.md) | 也判断不覆盖，列出了 1 ns 和 0.1 fs；另用理想气体估算了压力。 | 133.2 s |
| [无 Skill 2](examples/zeng-v3/without-2/answer.md) | 也判断不覆盖；列出 3000 K 和 0.25 g/cm³，没有写 1 ns 和 0.1 fs。 | 104.8 s |

三次的核心覆盖结论一致。有 Skill 的结果给出了逐项页码，代价是这次耗时更长。无 Skill 第一次的压力是它自己按理想气体作的估算；论文正文给出密度并称压力高，没有报告这个压力数值。任务、运行摘要和使用的 v3 Skill 都保存在 [对照材料](examples/zeng-v3/) 中。

仓库中的 [Skill v4](skill/SKILL.md) 在此基础上增加了方法链条的解释和逐项核查步骤。上表是 v3 的既有运行，不作为 v4 的测试结果。

## 在自己的论文上复用

拿到一篇 PDF 后，可以先问：

```text
请根据这篇论文说明：
1. 构型如何采样，能量与力的参考值如何得到？
2. 模型学习了什么，用哪些数据和指标验证？
3. 最终模拟的体系、温度、密度或压力、组成和时间尺度是什么？
4. 如果我的目标是【写明体系和用途】，论文里的哪些证据可以支持它，还有哪些条件需要核查？
关键事实请给 PDF 页码；论文没有写明的内容标为“未说明”。
```

用玻尔复现本例时，先登录 Bohr CLI，再把仓库里保存的完整提示发送给 `bohr chat`。以下命令适用于 PowerShell；请在仓库根目录执行：

```powershell
bohr auth status
$BohrEntry = Join-Path ((npm root -g).Trim()) '@dptech-corp/bohr-cli/run.js'
$PaperQuestion = Get-Content -Raw -Encoding utf8 'bohrium-pass/zeng-prompt.txt'
node $BohrEntry chat $PaperQuestion --model gpt-5-nano --output json
```

检查回答是否区分采样、量化标注和训练，再逐项对照上表的 PDF 页码。模型输出会随调用变化；论文原文是核对数字和条件的依据。实际费用以自己的调用返回为准。

需要对一篇本地论文系统判断方法和后续用途时，可把 [Skill 目录](skill/) 加入支持 Skill 的 Agent，提供 PDF 与具体问题。Skill 会组织方法链条、证据和适用判断；[机器学习势阅读线索](skill/references/ml-potentials.md) 用于提醒区分采样、参考标签和模型训练。

## 论文与运行记录

| 内容 | 位置 |
| --- | --- |
| Zeng 2020 全文及许可 | [PDF](materials/source/zeng2020-methane-nn-md.pdf)、[许可说明](materials/LICENSE.md) |
| 玻尔实际提示与返回 | [提示](bohrium-pass/zeng-prompt.txt)、[第一次返回](bohrium-pass/zeng-response-public.json)、[复跑返回](bohrium-pass/zeng-retest-public.json) |
| 原文核查与页码 | [核查记录](evidence/zeng-reading.md) |
| v3 适用性对照 | [任务、Skill 和三次回答](examples/zeng-v3/) |
| 可复用 Skill | [SKILL.md](skill/SKILL.md) 和 [检查脚本](skill/check_answer.py) |
| 含能材料附加案例 | [原文证据](evidence/quotes.md) 和 [对照任务](cases/A/task.md) |

论文和已有软件分别归原作者所有；阅读问题、提示、核查记录、Skill 和所列运行由本项目整理。
