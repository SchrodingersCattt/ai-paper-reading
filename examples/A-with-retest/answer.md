# 文献身份

- 题名：Accelerating the discovery of insensitive high-energy-density materials by a materials genome approach。第1页。
- 年份：2018。页眉为 “NATURE COMMUNICATIONS | (2018) 9:2444”，第1页；收稿日期 2 February 2018，接受日期 29 May 2018，第10页；“© The Author(s) 2018”，第11页。
- DOI：10.1038/s41467-018-04897-z。第1页。
- 许可证原文（第11页）：“Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.”
- 页数与现存章节：PDF 共 11 页，文本层可读。第1页为题名与摘要（无单独 Abstract 标题）。第2页起为 Results，含子节 Identification of key “genetic” features of IHE molecules、Rapid design and screening of new IHE molecules、Synthesis and crystal structure、Thermal properties、Solubility、Detonation properties、Sensitivities。第9页有 Discussion 与 Methods。结果页和讨论页都在本文件中，故继续做覆盖判断。

# 方法与条件

后续工作要核对的是：不新做合成、不新做感度测试，只用本文的材料基因组筛选，判断一个五元杂环候选物能否同时达到 HMX 的能量和 TATB 的感度。下表只记现存页里的方法与条件。

| 条目 | 原文短句 | 页码 | 标签 | 数值来源 |
| --- | --- | --- | --- | --- |
| 模型类别 | “identification of “genetic” features, rapid molecular design, and screening, as well as experimental synthesis of a target molecule” | 第1页 | 原文事实 | 未说明（这句是流程，不是一个带单位的数值） |
| 已执行的母环库 | “14 kinds of six-member aromatic rings (including benzene rings and N-hetero-aromatic rings) are selected and coded as P1 to P14” | 第4页 | 原文事实 | 未说明（计数 14 来自作者选定的母环，不是实测物性） |
| 取代基 | “nitro group (–NO2), amino group (–NH2), and hydrogen atom (–H)” | 第4页 | 原文事实 | 未说明 |
| 枚举工具与规模 | “By means of self-compiled Java scripts, we enumerated all the combinatorial possibility ... 176 suited molecular formulas” | 第4页 | 原文事实 | 计算（自编 Java 脚本，第4页）。176 个分子式、氧平衡后 45 个分子式 / 402 个分子、平面高对称 40 个、可能石墨状堆积 7 个，均在第4页 |
| 氧平衡筛选窗 | “a relatively low CO2-based oxygen balance value in the range of −80 to −40%” | 第3页 | 原文事实 | 计算。公式在第9页表1注 k：OB (%) = 1600×(d−a−b/2)/Mw |
| 第二遗传特征 | “planar aromatic (or hetero-aromatic) structures with high symmetry (e.g., C1v or better symmetries)” | 第4页 | 原文事实 | 未说明 |
| 第三遗传特征 | “the graphite-like crystal packing can be identified as the third “genetic” feature”；“15 main supramolecular synthons have been identified from the reported graphite-like high explosives” | 第4页 | 原文事实 | 未说明（15 个合成子的几何在补充图，正文只有这一句） |
| 证据数据从哪来 | “crystal densities of more than 1000 neutral organic compounds based on C, H, N, and O elements from Cambridge Structural Database (CSD)”；图2纵轴 “Density (g cm–3 at 295 K)” | 第3页 | 原文事实 | 实测（CSD 晶体密度，295 K / 室温）。这不是 DFT 训练集，也不是经验力场训练集 |
| 低感度结构样本 | “we selected eight representative HEDMs ... (Supplementary Fig. 1)” | 第3页 | 原文事实 | 未说明（八个化合物的名称与原始感度不在现存正文） |
| 力场名称 | 本文没有该项 | 第1–11页 | 原文事实 | 未说明 |
| 粗粒化 | 本文没有该项 | 第1–11页 | 原文事实 | 未说明 |
| 反应性轨迹或系综 | 本文没有分子动力学、系综、轨迹时长或模拟盒子大小。爆轰写的是 “evaluated using EXPLO5 (v6.02) program” | 第8页；方法重述在第10页 | 原文事实 | 计算（EXPLO5 v6.02，第8页与第10页）。这是热化学爆轰计算，正文没有反应力场下的断键轨迹 |
| 筛选温度、筛选压力、筛选时长 | 本文没有该项。三条遗传特征筛选没有给出温度、压力或时长 | 第3–4页 | 原文事实 | 未说明 |
| 最终选中分子的理论晶体密度 | “P6NAAA ... shows the highest theoretical crystal density (1.91 g cm−3) among seven molecules” | 第4页 | 原文事实 | 计算。正文称为 calculated；程序或公式在 Supplementary Note 4，现存页没有程序名，程序本身标为未说明 |
| 被合成并测性能的分子 | 筛选终点是六元嘧啶环 P6NAAA，即 2,4,6-triamino-5-nitropyrimidine-1,3-dioxide，文中称 ICM-102 | 第1页、第4–5页 | 原文事实 | 未说明 |
| 五元杂环在正文中的位置 | “5-amino-3-nitro-1,2,4-triazole (ANTA) ... fails to form a graphite-like layered packing” | 第4页 | 原文事实 | 未说明。ANTA 是堆积反例，不在 P1–P14 的命中名单里 |
| ICM-102 密度 | “measured ambient temperature density (1.95 g cm−3)”；表1注 b “Measured density by a gas pycnometer at 298 K” | 第8–9页 | 原文事实 | 实测。摘要同一句里的 1.95 g cm−3 也按实测密度单列，不与爆速混标 |
| 加热脱水样品密度 | “heated to 150 °C under vacuum (5 torr) for 5 h ... measured density of 1.92 g cm−3” | 第5页 | 原文事实 | 实测（密度）；温度 150 °C、真空 5 torr、时长 5 h 为实验条件 |
| 生成焓 | “calculated by the isodesmic reaction approach using Gaussian 09 (Revision D.01) ... −8.1 kJ mol−1” | 第8页 | 原文事实 | 计算（Gaussian 09 Revision D.01，第8页；第10页方法句再次指定 Gaussian 09 用于生成焓）。基组不在现存页 |
| 爆速 | “the calculated detonation velocity and detonation pressure of ICM-102 are 9169 m s−1 and 34.3 GPa” | 第8页 | 原文事实 | 计算（EXPLO5 v6.02，第8页）。输入是实测密度 1.95 g cm−3 与计算生成焓 −8.1 kJ mol−1。摘要中的 9169 m s−1 按这一页标为计算，不标成实测 |
| 爆压的另一处写法 | 同页后文写 “the detonation pressure of ICM-102 (34.2 GPa)”；表1为 34.3 GPa | 第8–9页 | 不能确定 | 计算（EXPLO5 v6.02）。34.3 与 34.2 都出现在现存页，本文不另取一个数 |
| 热分解温度 | “exothermic peak at 284 °C” | 第7页；表1在第9页 | 原文事实 | 实测（DSC/TG）。Kissinger 与 Ozawa 表观活化能 448.7 kJ mol−1、435.5 kJ mol−1 是由不同升温速率 DSC 算出的，标计算（第7页） |
| 变温光谱温度 | “heated from room temperature to 200 °C” | 第7页 | 原文事实 | 实测（红外与拉曼） |
| 撞击、摩擦、特性落高、静电火花 | “IS > 60 J and H50 = 320 cm”；“friction sensitivity ... >360 N”；“electrostatic spark sensitivity ... Ea = 1.85 J” | 第9页 | 原文事实 | 实测。表1注：BAM fall-hammer、BAM friction tester、2.5 kg drop hammer。测试温度本文没有该项 |
| HMX 对照 | 表1：密度 1.90 g cm−3，分解温度 279 °C，爆压 39.2 GPa，爆速 9221 m s−1，撞击感度 7.5 J，摩擦感度 120 N，H50 32 cm | 第9页；爆速对照句在第8页 | 原文事实 | 爆压、爆速脚注 e、f 写明 EXPLO5/6.02，标计算。密度行脚注 b 写气比重瓶 298 K，但正文只把 ICM-102 的 1.95 g cm−3 称为本文 measured density；HMX 密度的测定者标未说明 |
| TATB 对照 | 表1：密度 1.94 g cm−3，爆速 8114 m s−1，爆压 32.4 GPa，撞击感度 >60 J，摩擦感度 >360 N，H50 320 cm，火花 2.27 J；正文另写 TATB 爆轰能量 “around 65% of” HMX | 第2页、第9页 | 原文事实 | TATB 的 8114 m s−1 与 32.4 GPa 脚注 l 指向文献 Ref. 9，标未说明。65% 这句没有程序或公式，标未说明。感度行的方法栏是 BAM，ICM-102 由本文测试；TATB 是否由本文重测，现存页未说明 |
| 分子静电势解释 | “low group charge (−0.564), very negative ESP (−30.26), and excellent average deviation of ESP (0.246)” | 第9页，图7 | 原文事实 | 计算。第10页只把 Gaussian 09 归于生成焓、把 EXPLO5 归于爆轰；ESP 的程序名在现存页未说明 |
| 从六元库推到任意五元杂环 | 第4页写明枚举对象是 14 种六元环；ANTA 只作为五元三唑未能形成石墨状层的例子 | 第4页 | 推断 | 推断依据就是这两句：已跑完的组合筛选库是六元母环；五元例子没有进入选出目标再算能量、再测感度的那一条 |

# 主张

后续工作会依赖下面这些句子。它们留在主张里，不直接当成已经覆盖。

| 条目 | 原文短句 | 页码 | 标签 | 数值来源 |
| --- | --- | --- | --- | --- |
| 理想指标 | “new IHE molecules are expected to have the TATB’s sensitivity and the HMX’s energy” | 第2页 | 原文事实 | 未说明（这句没有给出爆速、爆压或感度的数值门槛） |
| 六元体系之外也可适用 | “Besides the considered system of six-member aromatic and hetero-aromatic rings, this materials genome approach can also be applicable to the development of new high-performing energetic materials” | 第1页 | 原文事实 | 未说明。这是适用性主张，不是已完成的五元库 |
| 推广到稠杂环 | “expanding this approach to multiple or fused hetero-aromatic ring systems” | 第9页 | 原文事实 | 未说明。讨论中的展望；现存页没有相应的五元或稠环筛选库 |
| 筛选的终点 | “P6NAAA is finally screened as the target IHE molecule that is worthy of our synthetic effort” | 第4页 | 原文事实 | 未说明。筛选结论是值得合成，不是免合成的能量与感度判定 |
| 已合成样品同时接近两个指标 | “ICM-102 has excellent detonation properties (νD=9169 m s−1 and P = 34.3 GPa) and is comparable to HMX”；感度 “comparable to TATB” | 第8–9页 | 原文事实 | 爆速 9169 m s−1、爆压 34.3 GPa 为计算（EXPLO5 v6.02）；感度 >60 J、>360 N 为实测（BAM）。对象是已合成的 ICM-102 |
| 把上一句移到未合成的五元杂环 | 同页比较对象是 ICM-102、TATB、HMX、RDX、LLM-105、FOX-7 | 第8–9页 | 推断 | 从第8–9页的样品名单推出：HMX 能量与 TATB 感度的并列结论写在 ICM-102 名下，没有写在五元杂环候选物名下 |
| 石墨状堆积与低感度 | “facilitates to translate less heat from shear and slip ... reduced formation in hot spots”；DAAF 与 DAAzF “detonation velocity > 8600 m/s” 且 “IS > 60 J” | 第4页 | 原文事实 | DAAF、DAAzF 的爆速与撞击感度在正文给出，并指向文献 41，标未说明 |

# 覆盖判断

| 后续条件 | 判断 | 页码 | 依据 |
| --- | --- | --- | --- |
| 对象是一个五元杂环候选物 | 不覆盖 | 第4页；主张句在第1页、第9页 | 已枚举并筛完的库是 14 种六元芳环和氮杂芳环。五元三唑 ANTA 只作为不能形成石墨状层的例子。摘要和讨论里的“也可适用 / expanding”是主张，不是已做出的五元库、样品或轨迹 |
| 只靠三条遗传特征做定性核对（氧平衡 −80% 到 −40%、平面高对称、石墨状合成子），不要求它输出 HMX/TATB 数值 | 部分覆盖 | 第3–4页 | 氧平衡统计来自 1000 个以上 CHNO 晶体，叙述本身不限定六元环；平面芳杂环和石墨状堆积也按结构特征来写，并且用 ANTA 说明五元环可以平面仍铺不成石墨状层。本文没有把这三条算成一条五元候选物的筛选记录 |
| 不进行新的合成，就用筛选结果下结论 | 不覆盖 | 第2页、第4–5页、第9页 | 文中的材料基因组流程包含实验合成。筛选停在 “worthy of our synthetic effort”。密度 1.95 g cm−3、晶体结构和感度都来自合成之后的 ICM-102 |
| 不进行新的感度测试，就判定达到 TATB 的感度 | 不覆盖 | 第9–10页 | TATB 级感度的正文证据是 BAM 撞击 >60 J、摩擦 >360 N、H50 = 320 cm 和火花 1.85 J，测的是 ICM-102。遗传特征被用作合成前的边界，本文仍做了感度测试才写出与 TATB 相当 |
| 判定能量达到 HMX | 不覆盖 | 第4页、第8–9页 | 与 HMX 的爆速、爆压比较用的是合成后实测密度加 Gaussian 09 生成焓，再经 EXPLO5 v6.02 计算，对象是 ICM-102：9169 m s−1 对 HMX 9221 m s−1，34.3 GPa 对 HMX 39.2 GPa。筛选步骤给出的定量结果是 P6NAAA 的理论密度 1.91 g cm−3，不是五元候选物的爆速或爆压。表1里的 HMX、TATB 数值只覆盖表中那些化合物 |
| 能量和 TATB 感度同时成立 | 不覆盖 | 第2页、第9页 | “HMX’s energy and TATB’s sensitivity” 在第2页是目标陈述，在第9页讨论中落到已合成的 ICM-102。现存页没有五元杂环候选物的这一联合结果 |

关键条件里，五元杂环对象、免合成、免感度测试、以及同时达到 HMX 能量和 TATB 感度，都是不覆盖。氧平衡和堆积规则的文字比六元库宽，只构成部分覆盖，带不出上述判定。

# 结论

不可用

# 阻塞缺口

已完成的筛选只枚举 14 种六元母环，并用合成后的实测密度、EXPLO5 爆轰计算和 BAM 感度测试才讨论 HMX 能量与 TATB 感度；现存页没有一条五元杂环候选物在免合成、免感度测试下的筛选结果。

# 未核查

补充材料不在本目录的 paper.pdf 中，故 Supplementary Note 1–6、Supplementary Fig. 1–23 和 Supplementary Table 1–5 均未打开。因此未核查：八个低感度代表物的名单（Supplementary Fig. 1）、15 个超分子合成子的几何（Supplementary Fig. 2b）、等键反应的基组与反应式（Supplementary Note 3）、除正文 1.91 g cm−3 以外的理论晶体密度及所用程序（Supplementary Note 4、Supplementary Fig. 21）、晶体结构预测细节（Supplementary Note 5、Supplementary Fig. 22）、板痕试验照片（Supplementary Fig. 18）。图2各氧平衡区间的柱高、图4每个异构体的键连，只采用了正文已写出的计数和编号，没有从图中另读数值。正文第1–11页都已打开。
