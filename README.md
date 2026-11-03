# 用 AI 读懂一篇机器学习势论文

读一篇机器学习势论文，先要弄清三个问题：构型从哪里来，模型学了什么，结果能不能用于自己的体系？这篇教程拿一篇甲烷燃烧论文做例子，用玻尔解析全文、辅助解释方法，再回到原文核对关键细节。

案例是 Zeng 等人的 [Complex reaction processes in combustion unraveled by neural network-based molecular dynamics simulation](https://doi.org/10.1038/s41467-020-19497-z)，*Nature Communications* **11**, 5713 (2020)。[论文 PDF](materials/source/zeng2020-methane-nn-md.pdf) 按 CC BY 4.0 分享；文中的页码均指该 PDF。

## 先看懂论文的方法链条

作者希望用分子动力学观察甲烷燃烧中的反应。论文的方法可以分成四步：

1. **采样构型。** 用 ReaxFF 反应性分子动力学生成初始结构，按局部成键分类并用聚类去冗余；随后用多个模型的短轨迹补充构型（第 6—7 页）。
2. **计算参考值。** 用 Gaussian 16 在 MN15/6-31G\*\* 水平计算构型的能量和原子力，得到训练参考（第 7 页）。
3. **训练势函数。** 用 DeePMD-kit 训练 DeepPot-SE；模型学习构型与势能的关系，训练损失包含能量和力（第 7 页）。
4. **运行与检查模拟。** 作者比较预测值与参考计算的误差，并用训练好的势模拟甲烷—氧气体系（第 2 页）。

ReaxFF 用于初始采样，量化计算提供参考能量和力。模型给出体系势能；原子力是势能对坐标的负梯度。MD 用力推进轨迹，论文再从轨迹中识别反应路径。

第 6 页的初始集约有 2250 万个结构。作者先分类和聚类，再用四个神经网络比较原子力预测；力差落在 0.5—1.0 eV/Å 区间的构型进入补充数据集。这是**选取新构型的判据**。第 2 页的 0.12 eV/Å 则是模型与参考计算的力 MAE，回答的是另一件事。

![Zeng 等人论文 Fig. 5：参考数据集的构建流程](materials/excerpts/zeng2020-fig5.png)

*图为 Zeng 等人论文第 6 页 Fig. 5 的裁图，按 CC BY 4.0 分享。*

## 用玻尔解析论文全文

我用 Bohrium Uni-Parser 的文件接口解析了这篇 9 页 PDF：`textual=2`、`table=2`、`equation=2`、`figure=0`。任务返回 `success`，本次费用为 45 分。[请求设置与结果摘要](bohrium-pass/zeng-parser-metadata.json) 和 [第 6、7 页相关解析块](bohrium-pass/zeng-parser-key-blocks.json)保留了实际返回的文字及公式；后者按原始顺序选出与下文讨论有关的块，保留类型、文本或 LaTeX，省去坐标与任务标识。

两处容易混淆的参数都被提取出来了：第 6 页的 **5 Å** 用于构造采样局部簇，第 7 页的 **6 Å** 用于模型描述符。第 7 页的能量—力损失函数也被识别为公式，可直接对照原文查看。

```math
\mathcal{L}=\frac{p_e}{N}\Delta E^2+\frac{p_f}{3N}\sum_i\lVert\Delta\mathbf{F}_i\rVert^2
```

其中 $\Delta E$ 和 $\Delta\mathbf{F}_i$ 对应能量与力的误差，$p_e$、$p_f$ 是两项权重。论文将能量项权重设为 0.2 eV⁻²，力项权重从 1000 降至 1 Å² eV⁻²；这两个权重用于训练，不是第 2 页报告的 MAE。

这次有一个实际需要回看原文的地方：解析结果包含第 6 页 Fig. 5 的图注，却没有图内的 “Sampling with ReaxFF” 等流程标签。本次请求将图像模块设为 `figure=0`，因此我打开 PDF 第 6 页核对了流程图。随后只对第 6 页请求 `figure=1`，接口返回 [HTTP 403](bohrium-pass/zeng-figure-http403.txt)。这说明本次账号和设置下，应继续用原 PDF 检查图内内容。

用下方脚本在新目录只解析第 6 页，任务再次成功，费用为 5 分；[实际返回文本](bohrium-pass/zeng-parser-retest-page6.txt)仍包含图注而没有图内流程标签，[请求与状态](bohrium-pass/zeng-parser-retest-metadata.json)单独保存。

复现时，准备 Python 和 `requests`，并配置玻尔开放平台的 `BOHR_ACCESS_KEY` 环境变量。本例的预检环境是 Python 3.11.14、`requests` 2.34.2；在仓库根目录执行：

```powershell
python bohrium-pass/parse_zeng.py submit --out ./parse-run
python bohrium-pass/parse_zeng.py poll --out ./parse-run
```

首次返回排队时，间隔几秒再次执行 `poll`。输出目录保存任务引用与原始响应；费用按实际请求返回。若要尝试第 6 页的图像模块，使用新的输出目录并加 `--figure 1 --page-index 5`；页码参数从 0 开始。

原始响应可能包含任务标识和计费字段；公开分享时可保留需要核查的文本、请求设置和页码，移除账户信息。

## 让 AI 解释方法，再回原文核对

我先从已保存的解析结果中选出第 6、7 页的五段原文，按页码和块号编号后交给玻尔。[实际提示](bohrium-pass/zeng-pipeline-prompt.txt)和[完整回答](bohrium-pass/zeng-pipeline-answer.txt)都已保存：这次回答正确区分了 ReaxFF 的初始采样、量化计算的参考能量与力，以及 5 Å、6 Å 的不同用途。返回模型为 `chenkun/gpt-5-nano`。

[构造提问的脚本](bohrium-pass/build_question.py)从仓库中保存的解析块提取同一组原句。先安装并登录 Bohr CLI；本例的参考环境为 Node.js 24.11.1、`@dptech-corp/bohr-cli` 2.9.21：

```powershell
npm install -g @dptech-corp/bohr-cli@2.9.21
bohr auth login
```

然后在仓库根目录用 PowerShell 重做这次提问：

```powershell
python bohrium-pass/build_question.py --out ./parse-run/question.txt
$BohrEntry = Join-Path ((npm root -g).Trim()) '@dptech-corp/bohr-cli/run.js'
$PaperQuestion = Get-Content -Raw -Encoding utf8 './parse-run/question.txt'
node $BohrEntry chat $PaperQuestion --model gpt-5-nano --output json
```

脚本重建的是本案例的提问；阅读另一篇论文时，需要按新问题选择对应的解析块。

再用同一份第 6 页解析文本提问：“请列出这篇论文 Fig. 5 图中每个方框的名称及箭头顺序，并给出依据。用中文回答。”第二次[增加核验要求](bohrium-pass/zeng-figure-guarded-instruction.txt)，要求模型先检查图内标签是否真的出现在文本里。两次请求都使用 `gpt-5-nano`，实际返回模型为 `chenkun/gpt-5-nano`。

两次回答都说明没有看到原图标签，但随后分别根据正文给出 16 步和 8 步的推测：[直接提问的回答](bohrium-pass/zeng-figure-baseline-answer.txt)、[增加核验后的回答](bohrium-pass/zeng-figure-guarded-answer.txt)。对照上面的原图，这些是对正文方法的拆解，不能当作图内方框的逐字转录。读取图示时，把模型推断与图里的实际标注分开即可。

两次输入共用前面保存的第 6 页文本；[脚本](bohrium-pass/build_figure_question.py)可分别重建完整提问，[记录](bohrium-pass/zeng-figure-comparison-metadata.json)保存了模型名称和提示哈希。

原 PDF 的文字层还保留了图中的词。我用 PyMuPDF 提取 Fig. 5 区域的 31 个词及坐标，补到同一个问题里再次提问。[这次回答](bohrium-pass/zeng-figure-text-layer-answer.txt)找到了 “Sampling with ReaxFF”“QM calculation” 等标签，但把区域名称 “Active learning” 排进线性流程，还遗漏了图中的 Redundancy removal → Dataset 连接。文字层能补回标签，箭头仍需看原图。

安装 `PyMuPDF==1.26.7` 后，可以从论文生成[同一组词和位置](bohrium-pass/zeng-figure-text-layer-words.txt)及完整问题；接着沿用上面的 `$BohrEntry` 提问：

```powershell
python -m pip install PyMuPDF==1.26.7
python bohrium-pass/build_figure_layer.py --out ./figure-run
$FigureQuestion = Get-Content -Raw -Encoding utf8 './figure-run/question.txt'
node $BohrEntry chat $FigureQuestion --model gpt-5-nano --output json
```

## 把论文条件和自己的问题对上

假设我要研究约 1 atm、低于 2000 K 的稀释甲烷—空气火焰，论文的结果能直接回答吗？先把目标与已完成模拟放在一起：

| 条件 | 论文展示的生产模拟 | 我的目标 |
| --- | --- | --- |
| 组成 | 100 CH₄ + 200 O₂，无额外稀释气体 | 甲烷—空气，另有惰性气体稀释 |
| 温度 | 3000 K | 低于 2000 K |
| 密度／压力 | 0.25 g/cm³；正文称高密度、因而高压力，未报告压力数值 | 约 1 atm |
| 轨迹 | 一条 1 ns 的 NVT 轨迹，时间步长 0.1 fs | 目标火焰中的反应路径 |

论文第 2—3 页展示的是高温、高密度的 CH₄/O₂ 周期盒；更接近实验的稀释条件被列为后续工作。因此，这条已发表轨迹回答的是论文自己的模拟条件。想用于目标火焰，还需要核查相关构型、元素和验证数据。

方法描述中还有一处可以顺着数据继续查：第 6 页的初始采样盒被写成含大量 CH₄ 和 H₂，第 2 页的生产模拟则为 CH₄ 和 O₂。两处是不同步骤；仅凭这两段，不能确定初始盒是否另含氧气，或含氧构型如何进入参考集。论文第 7 页提供了数据集和代码地址。

## 用 Skill 检查证据边界

我把上面的阅读方法整理成 [method-fit-check](skill/SKILL.md)：先解释方法链条，再逐项对照读者的用途、论文条件和来源页码。它以本地 PDF 和具体问题为输入，输出一份可核查的 `answer.md`。

使用同一份 Zeng PDF 和同一任务，分别运行两次有 Skill、两次无 Skill。四次均传入 `grok-4.7-high`，使用 Cursor agent CLI 2026.10.19 和独立目录；验收标准在运行前写好。

| 运行 | 对训练集范围和压力的处理 | 耗时 |
| --- | --- | ---: |
| [有 Skill 1](examples/zeng-v5/A-with-1/answer.md) | 训练集元素范围和压力数值标为未说明。 | 625.5 s |
| [无 Skill 1](examples/zeng-v5/A-without-1/answer.md) | 将训练集写成确定的 C/H/O，并另做压力估算。 | 363.2 s |
| [有 Skill 2](examples/zeng-v5/A-with-2/answer.md) | 将惰性气体适用性留待验证，压力数值标为未说明。 | 609.9 s |
| [无 Skill 2](examples/zeng-v5/A-without-2/answer.md) | 将参考集写成确定没有惰性气体；另估算密度和比例。 | 412.0 s |

四份回答都解释了主要方法并判断目标条件未被展示。两份有 Skill 的回答保留了训练集元素范围未明确报告的边界，耗时也高于两份无 Skill 回答。虽然四次传入的模型 ID 相同，两份有 Skill 的初始化显示名带 `256K`，两份无 Skill 的显示名没有；服务未公开权重版本，无法完全排除后端配置差异对结果的影响。

换用 Wen 和 Tadmor 的 DUNN 论文后，[另一次运行](examples/zeng-v5/B-with/answer.md)分清了包含金刚石的 DFT 数据集、未用金刚石训练的检测势，以及加入金刚石后的重拟合势。它额外写了一句过强的反事实：如果检测势已训练金刚石，原先的差异就不会出现。论文直接展示的是一次重拟合后的下降。[原文第 5、6 页](materials/excerpts/wen2020-original-pages5-6.pdf)和[第 8 页数据集说明](materials/excerpts/wen2020-page8-dataset.md)可用于核查。

从 Zeng 论文构造的[前两页 PDF](materials/source/zeng2020-constructed-pages1-2.pdf)上，[两次运行](examples/zeng-v5/)都停在“材料不足”，列出需要补读的 Methods 和结果内容。现有两页不足以确定缺失章节的页码，两份回答均没有猜测。

## 在自己的论文上复用

先准备 PDF 和你真正想回答的问题，例如：

```text
请根据这篇论文说明：
1. 构型如何采样，能量与力的参考值如何得到？
2. 模型学习了什么，用哪些数据和指标验证？
3. 最终模拟的体系、温度、密度或压力、组成和时间尺度是什么？
4. 我的目标是【写明体系和用途】。哪些证据可以支持它，还需要查什么？
关键事实请给 PDF 页码；论文未说明的内容请标出。
```

在支持 Skill 的 Agent 中加载 [skill/](skill/)，将 PDF 与问题交给它。核对时优先检查参考标签来源、指标及单位、模拟条件和图表上下文。要复查本例，可以打开[任务、标准和七份答案](examples/zeng-v5/)，也可以按其中的 Windows 步骤重跑 A 案例；预检先比较两侧输入的哈希，再决定是否调用模型。

## 论文与证据

| 内容 | 位置 |
| --- | --- |
| Zeng 2020 全文及许可 | [PDF](materials/source/zeng2020-methane-nn-md.pdf)、[许可说明](materials/LICENSE.md) |
| 玻尔全文解析 | [请求与状态](bohrium-pass/zeng-parser-metadata.json)、[关键块输出](bohrium-pass/zeng-parser-key-blocks.json)、[第 6 页复跑](bohrium-pass/zeng-parser-retest-page6.txt)、[复现脚本](bohrium-pass/parse_zeng.py) |
| 解析后提问 | [构造脚本](bohrium-pass/build_question.py)、[实际提示](bohrium-pass/zeng-pipeline-prompt.txt)、[实际回答](bohrium-pass/zeng-pipeline-answer.txt)、[模型信息](bohrium-pass/zeng-pipeline-metadata.json) |
| 流程图对照 | [提问重建脚本](bohrium-pass/build_figure_question.py)、[增加的核验要求](bohrium-pass/zeng-figure-guarded-instruction.txt)、[两次完整回答](bohrium-pass/zeng-figure-baseline-answer.txt)与[复跑回答](bohrium-pass/zeng-figure-guarded-answer.txt) |
| PDF 文字层补充 | [词与坐标](bohrium-pass/zeng-figure-text-layer-words.txt)、[完整回答](bohrium-pass/zeng-figure-text-layer-answer.txt)、[提取脚本](bohrium-pass/build_figure_layer.py)、[模型与哈希](bohrium-pass/zeng-figure-text-layer-metadata.json) |
| Skill v5 对照 | [任务、标准与七份答案](examples/zeng-v5/) |
| Wen 2020 核查材料 | [第 5、6 页](materials/excerpts/wen2020-original-pages5-6.pdf)、[第 8 页数据集说明](materials/excerpts/wen2020-page8-dataset.md) |
| 其他文献案例 | [含能材料案例与原文证据](https://github.com/SchrodingersCattt/ai-paper-reading/blob/14371bcd1077ffaab6aca1b4f7869d0fbeaeec0b/evidence/quotes.md) |

论文和既有软件归原作者所有；提示、核查记录、Skill 和所列运行由本项目整理。
