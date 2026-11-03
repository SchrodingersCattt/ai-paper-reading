# 文献身份

- 题名：Complex reaction processes in combustion unraveled by neural network-based molecular dynamics simulation（第1页）。
- 年份：2020。第1页刊头为 Nature Communications (2020) 11:5713；第7页写 Received: 10 March 2020; Accepted: 6 October 2020。
- DOI：10.1038/s41467-020-19497-z（第1页）。
- 许可证（第9页原文）：Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.
- 全文 9 页。目录中的章节：Results（第2页；下含 Accuracy of the NN PES、The initial stage of combustion、Production of formaldehyde and formyl radicals、Production of CO and CO2）、Discussion（第5页）、Methods（第6页；下含 Reference dataset、QM calculation、Training of the NN PES）。第1页有一段未单独标题的摘要。结果和讨论都在本文件中。

# 方法与条件

| 条目 | 原文短句 | 页码 | 标签 |
| --- | --- | --- | --- |
| 模型类别 | “the DeePMD model was used.” 生产势能为 DeepPot-SE，由 DeePMD-kit 训练：“The DeepPot-SE (Deep Potential-Smooth Edition) model was used to train the NN potential by the DeePMD-kit program.” | 第2、7页 | 原文事实 |
| 生产势能 | 高维神经网络势能，由从头算能量训练：“an NN potential derived by training a high-dimensional NN model from ab initio computed energies.” | 第2页 | 原文事实 |
| 训练数据（能量与力） | “The potential energy and atomic forces for every structure in the final dataset were calculated by Gaussian 16 software at the MN15/6-31G** level.” 来源：计算（Gaussian 16，第7页）。 | 第7页 | 原文事实 |
| 经验力场（只用于采样） | “The ReaxFF parameter of Chenoweth et al. (CHO-2008 parameter set) was employed.” 该力场用于构建参考数据集的初始采样，不是 1 ns 生产轨迹的势能。采样程序为 LAMMPS。来源：计算（LAMMPS，第6页）。 | 第6页 | 原文事实 |
| 筛选库 / 参考集 | 作者写明 QM9、ANI-1 等不适用于甲烷燃烧。自建参考集：“there are still 578,731 structures in the reference set.” 初始 ReaxFF 轨迹约 22.5 million structures。来源：未说明（第6页给出数目，未写出计数程序）。 | 第2、6页 | 原文事实 |
| 粗粒化 | 本文没有该项。 | 第2–7页 | 原文事实 |
| 反应性 | “a 1-ns reactive MD simulation was performed.” 轨迹中写出断键，例如甲烷被 O2 抽氢生成 ·CH3 与 HOO·。 | 第2、3页 | 原文事实 |
| 系综（能量守恒检验） | “we performed a reactive MD simulation under the NVE ensemble.” 同一组成，密度 0.25 g/cm3。本文没有给出这次 NVE 的温度和时长。 | 第2页 | 原文事实 |
| 系综（生产轨迹） | “A 1 ns reactive MD simulation was performed for methane combustion with the NN PES under the NVT ensemble.” 恒温：“the temperature was kept at 3000 K by using the Berendsen thermostat.” | 第2页 | 原文事实 |
| 温度 | 生产轨迹与 ReaxFF 采样均为 3000 K。第6页：“the temperature was set to 3000 K with the Berendsen thermostat.” 来源：计算。ReaxFF 这段的程序是 LAMMPS（第6页）。第2页生产轨迹写明 Berendsen，产生该轨迹的程序名未说明。 | 第2、6页 | 原文事实 |
| 压力 | 本文没有该项。正文没有 atm 或 Pa。相邻原句只说 “a relatively high density (and thus high pressure) and high temperature”。 | 第2–3页 | 原文事实 |
| 密度 | “with a density of 0.25 g/cm3.” NVE 与 NVT 两个盒子都是这个密度。来源：计算（第2页的模拟设定；该生产轨迹的程序名未说明）。 | 第2页 | 原文事实 |
| 时长与步长 | “a 1-ns reactive MD simulation”；“a time-step of 0.1 fs”。来源：计算（第2页的模拟设定；程序名未说明）。 | 第2页 | 原文事实 |
| 体系大小与组成 | “a periodic box containing 100 CH4 molecules and 200 O2 molecules (a total of 900 atoms)”。来源：计算（第2页）。参考集初始采样是另一体系：“a model combustion system containing a lot of CH4 and H2 molecules.” 分子数未给出，不能确定。 | 第2、6页 | 原文事实；H2 体系的分子数为不能确定 |
| 惰性气体或空气 | 生产体系原文只有 CH4 与 O2。采样体系原文只有 CH4 与 H2。惰性气体出现在今后工作的句子里：“In future work, we will try to combine the NN potential and enhanced sampling algorithms to bring simulated conditions more realistic.” | 第2、3、6页 | 原文事实 |
| 截断 | 数据集团簇截断 “the cutoff was set to 5 Å.” 神经网络 “The cutoff radius was set to 6.0 Å”。来源：计算（第6页数据集流程；第7页 DeePMD-kit 训练设定）。 | 第6、7页 | 原文事实 |

# 主张

| 条目 | 原文短句 | 页码 | 标签 |
| --- | --- | --- | --- |
| 势能可描述燃烧中的反应物、产物和中间体 | “This NN PES can accurately predict the energy and atomic forces of reactants, products and reaction intermediates.” | 第2页 | 原文事实 |
| 一条轨迹可以抽出甲烷燃烧反应网络 | “A complete reaction network of the methane combustion can be constructed from the MD trajectory.” | 第2页 | 原文事实 |
| 主要路径与实验机理一致 | “the above-mentioned 32 reactions have all been found by experiments, and the reaction networks constructed by them are also highly consistent with the main reaction networks found experimentally.” 同页：“130 of the 798 reactions extracted from the MD trajectory were included in the widely accepted GRI_Mech experimental mechanism library.” 798 与 130 的来源：计算（从轨迹计数，第5页；该句未写检测程序）。 | 第5页 | 原文事实 |
| 现有轨迹故意用了高温高密度，更接近实验的稀释条件尚未做 | “We chose a relatively high density (and thus high pressure) and high temperature to enhance the collision probability and sampling efficiency.” 随后：“experiments usually do not use pure fuel for combustion, but rather mix the fuel into a relatively inert gas for safety. In future work, we will try…” | 第2–3页 | 原文事实 |
| 高温使一部分实验反应没有出现 | “Some experimentally observed reactions were not observed in our simulation, mostly likely because the present simulation was performed at relatively high temperature.” | 第5页 | 原文事实 |
| 污染物物种在该轨迹中的数量 | “about 160 H2O, 30 CO, and 50 CO2 are produced.” 来源：计算（第3页的 NVT 轨迹计数；程序名未说明）。 | 第3页 | 原文事实 |
| 上述轨迹已经覆盖约 1 atm、低于 2000 K、惰性气体稀释的甲烷–空气火焰 | 正文没有这一句。第2页的轨迹是 3000 K、0.25 g/cm3 的 100 CH4 + 200 O2；第3页把惰性气体稀释和更真实条件写成 future work。由此推出：作者没有把现有轨迹当作该实验室火焰。 | 第2–3页 | 推断 |

# 覆盖判断

后续工作拆成七项。覆盖与否只按已经做过的体系、轨迹和数据集，不按摘要或讨论里的展望。

1. 使用本文神经网络势能做反应路径预测：部分覆盖。DeepPot-SE 势能和 1 ns 反应轨迹都写在第2页，训练程序 DeePMD-kit 在第7页，甲醛、甲酰、CO、CO2 的路径在第3–5页。这些轨迹的温度、密度和组成不是读者给出的实验室条件。第3页的 future work 只是主张，不能当成已经覆盖。
2. 对象是甲烷–空气火焰：不覆盖。生产盒子是 100 个 CH4 与 200 个 O2，共 900 个原子（第2页）。现存页没有把空气或氮气写成体系组分。
3. 现象是污染物路径：部分覆盖。轨迹给出甲醛、甲酰自由基、CO 和 CO2 的生成路径（第3–5页），1 ns 时约有 30 个 CO 和 50 个 CO2（第3页，来源：计算，程序名未说明），并检测到 505 个物种和 798 个反应（第5页，来源：计算）。第5页同时写明，因为温度高，一部分实验里有的反应没有出现。实验室火焰中的污染物路径没有对应轨迹。
4. 温度低于 2000 K：不覆盖。读者条件是低于 2000 K。论文生产 NVT 与 ReaxFF 采样都是 3000 K（第2、6页，来源：计算；第6页程序为 LAMMPS，第2页生产轨迹的程序名未说明）。3000 K 不低于 2000 K。
5. 压力约 1 atm：不覆盖。读者条件是约 1 atm。本文没有压力数值。写出的密度是 0.25 g/cm3（第2页，来源：计算，程序名未说明），并称为 relatively high density and thus high pressure（第2–3页）。high 不能代替与 1 atm 的数值比较。没有约 1 atm 的轨迹。
6. 燃料用惰性气体稀释：不覆盖。第3页写实验通常把燃料混入相对惰性的气体，并把这件事放在 future work。第2页的生产体系只有 CH4 和 O2，第6页的采样体系是大量 CH4 和 H2。
7. 实验室火焰的时间尺度与热状态：不覆盖。第2–3页写高温高密度是为了在短于实验的模拟时间内增加碰撞。第5页写模拟可以在比实验室实验更极端的条件下进行。极端温度和密度下的轨迹不能当成实验室条件。

# 结论

不可用

# 阻塞缺口

本文没有在约 1 atm、低于 2000 K、惰性气体稀释的甲烷–空气体系中用该神经网络势能做出的反应轨迹，现有路径来自 3000 K、0.25 g/cm3 的纯 CH4/O2 盒子。

# 未核查

补充材料不在本目录，Supplementary Table 1、Supplementary Table 2 和 Supplementary Fig. 1–5 中的误差、能量守恒和速率常数没有核验。正文第1–9页已读。图2–4中的键长标注没有用于覆盖判断。
