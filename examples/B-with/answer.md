# 文献身份

- 题名：Complex reaction processes in combustion unraveled by neural network-based molecular dynamics simulation（第 1 页）。
- 年份：2020。页脚写 “NATURE COMMUNICATIONS | (2020) 11:5713”（第 1 页）；收稿日期 10 March 2020，接受日期 6 October 2020（第 7 页）；“© The Author(s) 2020”（第 9 页）。
- DOI：10.1038/s41467-020-19497-z。第 1 页写有 https://doi.org/10.1038/s41467-020-19497-z。
- 许可证（第 9 页原文）：Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.
- 全文共 9 页，文本层可读。现存章节：开篇摘要（第 1 页，无 “Abstract” 小标题）；Results（第 2 页），其下有 Accuracy of the NN PES（第 2 页）、The initial stage of combustion（第 2 页）、Production of formaldehyde and formyl radicals（第 3 页）、Production of CO and CO2（第 3 页）；Discussion（第 5 页）；Methods（第 6 页），其下有 Reference dataset（第 6 页）、QM calculation（第 7 页）、Training of the NN PES（第 7 页）。结果与讨论都在本文件中。

# 方法与条件

| 条目 | 原文短句 | 页码 | 标签 |
| --- | --- | --- | --- |
| 模型类别 | “the DeePMD model was used”；“The DeepPot-SE model was used to train the NN PES”。程序名 DeePMD、DeepPot-SE，来源：计算（训练程序 DeePMD-kit，第 7 页）。 | 2，7 | 原文事实 |
| 训练数据来自什么 | “The potential energy and atomic forces for every structure in the final dataset were calculated by Gaussian 16 software at the MN15/6-31G** level.” 来源：计算（Gaussian 16，MN15/6-31G**，第 7 页）。实验能量不是这套参考数据。 | 7 | 原文事实 |
| 初始采样力场 | “reactive MD simulation with ReaxFF was used to sample an initial dataset”；“The ReaxFF parameter of Chenoweth et al. (CHO-2008 parameter set) was employed.” 程序 LAMMPS。来源：计算（第 6 页）。该力场只用于采样，生产轨迹用的是 NN PES。 | 6 | 原文事实 |
| 粗粒化 | 本文没有该项。 | 1–9 | 原文事实 |
| 反应性 | “a 1-ns reactive MD simulation was performed”；摘要写 “a total of 798 different chemical reactions were recorded”。来源：计算（由 NN PES 轨迹提取，第 1、2、5 页）。 | 1，2，5 | 原文事实 |
| 系综 | 能量守恒检验：“a reactive MD simulation under the NVE ensemble”。生产模拟：“under the NVT ensemble”，温度 “kept at 3000 K by using the Berendsen thermostat”。来源：计算。 | 2 | 原文事实 |
| 温度 | 生产模拟与 ReaxFF 采样均为 “3000 K”。来源：计算（Berendsen 恒温，第 2 页与第 6 页）。正文没有低于 2000 K 的设定温度。 | 2，6 | 原文事实 |
| 主动学习短程 MD 的温度 | 本文没有该项。只写 “several short MD simulations were performed based on these NN models”。温度来源：未说明。 | 6 | 不能确定 |
| 密度 | “with a density of 0.25 g/cm3”。NVE 检验与 NVT 生产都是这个密度。来源：计算（模拟设定，第 2 页）。 | 2 | 原文事实 |
| 压力 | “a relatively high density (and thus high pressure)”。以 atm 为单位的压力本文没有该项。压力数值来源：未说明。 | 2–3 | 原文事实 |
| 时长与步长 | “1-ns reactive MD simulation”；“time-step of 0.1 fs”。来源：计算（第 2 页；第 5 页重申 time-step 为 0.1 fs）。 | 2，5 | 原文事实 |
| 体系大小 | “100 CH4 molecules and 200 O2 molecules (a total of 900 atoms)”，周期箱。来源：计算（第 2 页）。 | 2 | 原文事实 |
| 体系组成 | 生产体系是 100 个甲烷与 200 个氧气。参考集采样句为 “containing a lot of CH4 and H2 molecules”。该采样句没有写出氮气或惰性气体。 | 2，6 | 原文事实 |
| ReaxFF 采样盒是否含氧气 | 本文没有该项。采样句只点名 CH4 与 H2。来源：未说明。 | 6 | 不能确定 |
| 参考集规模与团簇截断 | “578,731 structures in the reference set”；团簇截断 “the cutoff was set to 5 Å”。来源：计算（第 6 页）。 | 6 | 原文事实 |
| NN 截断与网络 | “cutoff radius was set to 6.0 Å”；嵌入网络 “(25, 50, 100)”，拟合网络 “(240, 240, 240)”。来源：计算（DeePMD-kit，第 7 页）。 | 7 | 原文事实 |
| NN 相对 DFT 的误差 | 能量 MAE “0.04 and 0.14 eV/atom” 分别对应训练集与测试集；力的相关系数 “0.999”，MAE “0.12 eV/Å”。来源：计算（NN 对 DFT，第 2 页）。 | 2 | 原文事实 |

# 主张

| 条目 | 原文短句 | 页码 | 标签 |
| --- | --- | --- | --- |
| 势能可描述反应物、产物和中间体 | “This NN PES can accurately predict the energy and atomic forces of reactants, products and reaction intermediates.” 数字误差见上表，来源：计算。 | 2 | 原文事实 |
| 轨迹给出甲烷燃烧反应网 | “A complete reaction network of the methane combustion can be constructed from the MD trajectory.” 1 ns 后大约消耗 90 个 CH4、150 个 O2，生成约 160 个 H2O、30 个 CO、50 个 CO2。这些分子数来源：计算（第 3 页）。 | 2，3 | 原文事实 |
| 与实验机理库的重合 | “130 of the 798 reactions extracted from the MD trajectory were included in the widely accepted GRI_Mech experimental mechanism library”；并检测到 “505 molecular species and 798 reactions”。计数来源：计算（第 5 页）。 | 5 | 原文事实 |
| 高温使部分实验反应未出现 | “Some experimentally observed reactions were not observed in our simulation, mostly likely because the present simulation was performed at relatively high temperature.” | 5 | 原文事实 |
| 污染物只作为研究动机 | “minimize the production of pollutants”。这句在结果之前，说明动机。来源：未说明具体污染物清单。 | 2 | 原文事实 |
| 真实实验条件留作以后 | “mix the fuel into a relatively inert gas for safety. In future work, we will try to combine the NN potential and enhanced sampling algorithms to bring simulated conditions more realistic.” | 3 | 原文事实 |
| 速率不宜直接进入动力学模型 | “these rates may not be accurate enough to be used directly in kinetic modeling”。速率来自这一条轨迹的统计，来源：计算（第 5–6 页）。 | 5–6 | 原文事实 |
| 目标实验室条件是否已由该势能预测 | 从第 3 页“future work”和第 2 页 3000 K、0.25 g/cm3 的轨迹不能推出约 1 atm、低于 2000 K、惰性气体稀释的甲烷–空气火焰已经被预测。 | 2，3 | 推断 |

# 覆盖判断

后续工作拆成下面几条。判断只认本文件里已经跑过的体系、轨迹和参考数据。

- 甲烷作为燃料：覆盖。生产体系含 100 个 CH4（第 2 页）。
- 空气：不覆盖。生产体系是 CH4 与 O2（第 2 页）。采样句写的是 CH4 与 H2（第 6 页）。正文没有氮气，也没有空气混合物。
- 实验室火焰这一现象：不覆盖。已做的是周期箱中的 NVT 反应分子动力学（第 2 页）。第 2 页把燃烧写成极端高压、高温过程，并说明这类条件使实时实验很难做。
- 用本文势能预测 C/H/O 反应路径：部分覆盖。DeepPot-SE / DeePMD 势能已用于 1 ns 轨迹，并抽出甲醛、甲酰、CO、CO2 的路径（第 2–5 页）。这条轨迹的温度、密度和组成与后续工作不一致（第 2–3 页）。
- 污染物路径：部分覆盖。轨迹里有甲醛、甲酰、CO、CO2 的生成路径（第 3–5 页）。第 2 页“pollutants”只是动机。空气火焰里需要氮的污染物路径，现存体系没有氮原子，做不到。第 6 页写这些速率不宜直接用于动力学模型。
- 约 1 atm：不覆盖。作者选择 “relatively high density (and thus high pressure)”，密度为 0.25 g/cm3（第 2–3 页）。正文没有 1 atm，也没有给出以 atm 计的压力。
- 低于 2000 K：不覆盖。生产和 ReaxFF 采样都是 3000 K（第 2、6 页）。第 5 页把一部分实验反应的缺失归因于这次模拟温度较高。
- 燃料用惰性气体稀释：不覆盖。第 3 页写实验通常把燃料混进相对惰性的气体，并把这种更接近真实的模拟列为 future work。已完成的生产体系是未稀释的 CH4 与 O2（第 2 页）。

# 结论

不可用

# 阻塞缺口

已完成的势能预测来自 3000 K、密度 0.25 g/cm3、未稀释的甲烷–氧气周期箱轨迹，正文没有约 1 atm、低于 2000 K、惰性气体稀释的甲烷–空气火焰轨迹。

# 未核查

补充材料不在本 PDF 中（正文指向 Supplementary Table 1、Supplementary Table 2、Supplementary Figs. 1–5，第 2、5、9 页）。图 1–4 里的键长标注没有逐一读成独立数据。主动学习短程 MD 的温度、压力和盒子组成，正文没有写出。参考文献页（第 7–8 页）里的他人温度或分子没有当成本文模拟条件。正文第 1–9 页已读。
