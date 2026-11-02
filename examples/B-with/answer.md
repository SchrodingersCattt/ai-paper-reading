## 文献身份

- 题名：Complex reaction processes in combustion unraveled by neural network-based molecular dynamics simulation（第1页）
- 年份：2020（第1页刊头 “(2020) 11:5713”；第7页 “Received: 10 March 2020; Accepted: 6 October 2020”）
- DOI：10.1038/s41467-020-19497-z（第1页）
- 许可证（第9页原文）：“Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.”

目录中的章节：摘要性开篇（第1页）、Results（第2页；Accuracy of the NN PES；The initial stage of combustion；Production of formaldehyde and formyl radicals；Production of CO and CO2）、Discussion（第5页）、Methods（第6页；Reference dataset；QM calculation；Training of the NN PES）。结果与讨论均在本 PDF 中。

## 方法与条件

| 条目 | 原文短句 | 页码 | 标签 |
| --- | --- | --- | --- |
| 模型类别 | “the DeePMD model was used” | 2 | 原文事实 |
| 模型类别 | “The DeepPot-SE model was used to train the NN PES” | 2 | 原文事实 |
| 模型类别 | “The DeepPot-SE (Deep Potential-Smooth Edition) model was used to train the NN potential by the DeePMD-kit program.” | 7 | 原文事实 |
| 训练数据来源 | “calculated by Gaussian 16 software at the MN15/6-31G** level.” | 7 | 原文事实 |
| 初始构型采样力场 | “The ReaxFF parameter of Chenoweth et al. (CHO-2008 parameter set) was employed.” | 6 | 原文事实 |
| 采样体系 | “containing a lot of CH4 and H2 molecules” | 6 | 原文事实 |
| 反应性 | “The combustion of methane started with the abstraction of its hydrogen atom by O2” | 3 | 原文事实 |
| 反应性 | “We totally detected 505 molecular species and 798 reactions from the trajectory.” | 5 | 原文事实 |
| 粗粒化 | 由第7页原子能量分解 “E = Σ_i E_i” 与第2页 “a total of 900 atoms” 推出：模型按原子环境给能量。文中没有写粗粒化粒子。 | 2、7 | 推断 |
| 系综（能量守恒检验） | “we performed a reactive MD simulation under the NVE ensemble.” | 2 | 原文事实 |
| 系综（生产轨迹） | “under the NVT ensemble” ；“using the Berendsen thermostat” | 2 | 原文事实 |
| 温度 | “the temperature was kept at 3000 K” | 2 | 原文事实 |
| 采样温度 | “the temperature was set to 3000 K with the Berendsen thermostat.” | 6 | 原文事实 |
| 密度 | “with a density of 0.25 g/cm3” | 2 | 原文事实 |
| 压力 | “a relatively high density (and thus high pressure)” | 2 | 原文事实 |
| 时长 | “A 1 ns reactive MD simulation was performed” | 2 | 原文事实 |
| 时间步长 | “a time-step of 0.1 fs” | 2 | 原文事实 |
| 体系大小 | “a periodic box containing 100 CH4 molecules and 200 O2 molecules (a total of 900 atoms)” | 2 | 原文事实 |
| 描述符截断 | “The cutoff radius was set to 6.0 Å” | 7 | 原文事实 |
| 与实验室稀释条件的关系 | “mix the fuel into a relatively inert gas for safety.” | 3 | 原文事实 |
| 与实验室稀释条件的关系 | “bring simulated conditions more realistic.” | 3 | 原文事实 |

## 主张

| 主张 | 原文短句 | 页码 | 标签 |
| --- | --- | --- | --- |
| 该势能可给出反应物、产物和中间体的能量与原子力 | “This NN PES can accurately predict the energy and atomic forces of reactants, products and reaction intermediates.” | 2 | 原文事实 |
| 对 DFT 能量的数值误差 | “The mean absolute errors are only 0.04 and 0.14 eV/atom in the training set and the test set, respectively.” | 2 | 原文事实 |
| 原子力误差 | “the MAE is 0.12 eV/Å.” | 2 | 原文事实 |
| 列出的 32 个反应与实验主网络一致 | “the above-mentioned 32 reactions have all been found by experiments, and the reaction networks constructed by them are also highly consistent with the main reaction networks found experimentally” | 5 | 原文事实 |
| 与 GRI-Mech 的重合范围 | “130 of the 798 reactions extracted from the MD trajectory were included in the widely accepted GRI_Mech experimental mechanism library” | 5 | 原文事实 |
| 高温使一部分实验反应没有出现 | “mostly likely because the present simulation was performed at relatively high temperature.” | 5 | 原文事实 |
| 由单条轨迹抽出的速率不宜直接进入动力学模型 | “rates may not be accurate enough to be used directly in kinetic modeling” | 6 | 原文事实 |
| 甲醛、甲酰、CO、CO2 的路径是在该轨迹里抽出的 | “divided the combustion process into three stages, namely the initial stage of the combustion, the production of intermediate species of formaldehyde and formyl radical, and the production of CO and CO2.” | 3 | 原文事实 |
| 引言把减少污染物当作研究动机 | “minimize the production of pollutants” | 2 | 原文事实 |

## 覆盖判断

后续工作拆成：用本文势能预测实验室甲烷–空气火焰中的污染物路径；条件为约 1 atm、低于 2000 K、燃料用惰性气体稀释。

- 现象（实验室火焰）：不覆盖。生产模拟是 3000 K、0.25 g/cm3 的周期盒子，初始为 100 CH4 与 200 O2（第2页）。作者写模拟时间远短于实验，因而用高密度和高温提高碰撞采样，并把更真实的条件放到未来工作（第3页）。
- 污染物路径：部分覆盖。轨迹中抽出了甲醛、甲酰、CO 和 CO2 的反应步骤（第3–5页），物种统计含约 30 CO 与约 50 CO2（第3页）。这些路径属于上述甲烷–氧气盒子，不是实验室甲烷–空气火焰的污染物路径。
- 化学（甲烷氧化）：覆盖。反应从 CH4 被 O2 夺氢开始，并记录 505 个物种、798 个反应（第3、5页）。
- 化学（空气）：不覆盖。生产体系只有 CH4 与 O2（第2页）。参考集初始采样写的是 CH4 与 H2（第6页）。正文没有氮气或空气混合物上的轨迹。
- 温度低于 2000 K：不覆盖。NVT 生产轨迹与 ReaxFF 采样都设在 3000 K（第2、6页）。第5页把未观测到的实验反应主要归因于 “relatively high temperature”。
- 压力约 1 atm：不覆盖。原文给出的是密度 0.25 g/cm3，并写 “relatively high density (and thus high pressure)”（第2页）。没有约 1 atm 的数值；具体压强未写出，不能确定。
- 燃料用惰性气体稀释：不覆盖。第3页写实验通常把燃料混入相对惰性的气体，并写未来才把模拟条件做得更真实。生产体系是未稀释的 CH4/O2（第2页）。
- 时间尺度：部分覆盖。时间步长 0.1 fs、轨迹 1 ns，文中给出亚皮秒到皮秒量级的单步过程（第2–5页）。第3页同时写模拟时间远短于实验，所以才提高温度和密度。实验室火焰的停留时间没有对应轨迹。
- 直接把本文速率用于该条件下的动力学预测：不覆盖。第6页写这些速率 “may not be accurate enough to be used directly in kinetic modeling”，且速率来自 3000 K 的单条轨迹（第5–6页）。

## 结论

不可用

## 阻塞缺口

已报告的反应路径与速率来自 3000 K、0.25 g/cm3、未稀释的 CH4/O2 周期盒子，作者把惰性气体稀释和更真实的条件明确留到未来工作，因此本文方法与条件不能覆盖约 1 atm、低于 2000 K、惰性气体稀释的实验室甲烷–空气火焰污染物路径。

## 未核查

补充材料不在本 PDF 中，故 Supplementary Table 1–2 与 Supplementary Fig. 1–5 的数值和图未核对；第5页所说十个反应的速率常数只指向 Supplementary Table 2。正文第1–9页已读。图2–4中的键长标注未当作独立数据使用。正文没有给出以 atm 为单位的压强，该数字保持不能确定。
