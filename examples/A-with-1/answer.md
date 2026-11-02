# 方法适用性核对

后续工作：不新合成、不做感度测试，只用本文的材料基因组筛选，判断一个五元杂环候选物能否同时达到 HMX 的能量和 TATB 的感度。

## 文献身份

- 题名：Accelerating the discovery of insensitive high-energy-density materials by a materials genome approach｜第 1 页｜原文事实
- 年份：2018。页眉为 “NATURE COMMUNICATIONS | (2018) 9:2444”；第 11 页有 “© The Author(s) 2018”｜第 1、11 页｜原文事实
- DOI：10.1038/s41467-018-04897-z｜第 1 页｜原文事实
- 许可证：第 11 页原文为 “Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.”｜第 11 页｜原文事实

正文有 Results（第 2 页起）和 Discussion（第 9 页）。文本层存在，未触发停止规则。

## 方法与条件

- 模型类别｜“identification of “genetic” features, rapid molecular design, and screening, as well as experimental synthesis of a target molecule”｜第 1 页｜原文事实
- 已执行的母环库｜“14 kinds of six-member aromatic rings (including benzene rings and N-hetero-aromatic rings) are selected and coded as P1 to P14”｜第 4 页｜原文事实
- 取代基｜“nitro group (–NO2), amino group (–NH2), and hydrogen atom (–H)”｜第 4 页｜原文事实
- 枚举工具｜“self-compiled Java scripts” 枚举母环与取代基的组合｜第 4 页｜原文事实
- 筛选漏斗｜176 个分子式，氧平衡边界后剩 45 个分子式、402 个含异构体的分子，平面高对称分子 40 个，其中 7 个有形成石墨状晶体的潜力｜第 4 页｜原文事实
- 边界条件｜“rapid screening is carried out using three identified key “genetic” features of IHE molecules as the boundary conditions”｜第 4 页｜原文事实
- 遗传特征 1，氧平衡｜“a relatively low CO2-based oxygen balance value in the range of −80 to −40% is desirable for the HEDMs’ insensitivity”｜第 3 页｜原文事实
- 遗传特征 2，分子几何｜“the planar aromatic (or hetero-aromatic) structures with high symmetry (e.g., C1v or better symmetries)”｜第 3–4 页｜原文事实
- 遗传特征 3，晶体堆积｜“the graphite-like crystal packing can be identified as the third “genetic” feature of IHE molecules”｜第 4 页｜原文事实
- 超分子合成子｜“15 main supramolecular synthons have been identified from the reported graphite-like high explosives”｜第 4 页｜原文事实
- 数据来源｜“crystal densities of more than 1000 neutral organic compounds … from Cambridge Structural Database (CSD)”；关系来自实验晶体密度、氧平衡和已报道炸药的感度｜第 3 页｜原文事实
- 训练数据属于 DFT 还是经验力场｜正文把筛选写成 CSD 统计、结构特征和 Java 枚举。没有写出以 DFT 或经验力场训练筛选模型｜第 3–4 页｜推断
- 力场名称｜晶体预测和筛选正文没有给出力场名称。理论密度写的是 “Supplementary Note 4”｜第 4 页｜不能确定
- 粗粒化｜枚举的是明确分子式和取代模式。正文没有粗粒化粒子模型｜第 4 页｜推断
- 反应性与断键｜筛选边界是氧平衡、平面性和石墨状堆积，没有写出键断裂或反应轨迹。爆轰量出现在合成之后，由 EXPLO5 计算｜第 4、8 页｜推断
- 系综｜正文没有系综｜全文｜不能确定
- 温度，CSD 图｜图 2 纵轴为 “Density (g cm–3 at 295 K)”｜第 3 页｜原文事实
- 温度，实测密度｜表 1 注 “Measured density by a gas pycnometer at 298 K”｜第 9 页｜原文事实
- 温度，热分解｜ICM-102 放热峰 284 °C｜第 8–9 页｜原文事实
- 模拟温度｜筛选没有给出模拟温度｜全文｜不能确定
- 筛选用密度｜P6NAAA “shows the highest theoretical crystal density (1.91 g cm−3) among seven molecules”｜第 4 页｜原文事实
- 实测密度｜无水 ICM-102 “measured density is high to 1.95 g cm−3”｜第 7 页｜原文事实
- 压力或爆压｜筛选没有给出模拟压力。ICM-102 爆压在合成并测密度之后计算，表 1 为 34.3 GPa，HMX 为 39.2 GPa｜第 8–9 页｜原文事实
- 模拟时长｜正文没有轨迹时长｜全文｜不能确定
- 体系大小｜CSD 化合物 “more than 1000”；母环 14 种；漏斗 176 → 45 → 402 → 40 → 7｜第 3–4 页｜原文事实
- 生成焓与爆轰程序的使用范围｜“heat of formation (ΔfH) of ICM-102 was first calculated by the isodesmic reaction approach using Gaussian 09”；“Using the measured ambient temperature density (1.95 g cm−3) … evaluated using EXPLO5 (v6.02)”｜第 8 页｜原文事实
- Gaussian 泛函、基组｜正文只写 “Gaussian 09 (Revision D.01)” 和 “isodesmic reaction approach”。泛函和基组不在现存正文｜第 8 页｜不能确定
- 感度如何被定量｜冲击用 “standard BAM” 和 “characteristic height (H50)”；摩擦 “>360 N”；静电感度另测。这些是合成后的实验｜第 9–10 页｜原文事实
- 筛选终点｜“P6NAAA is finally screened as the target IHE molecule that is worthy of our synthetic effort”｜第 4 页｜原文事实

## 主张

- 理想目标｜“new IHE molecules are expected to have the TATB’s sensitivity and the HMX’s energy”｜第 2 页｜原文事实
- 本文目标｜“The goal of our research is to obtain the desired IHE molecule with HMX’s energy and TATB’s sensitivity”｜第 9 页｜原文事实
- 筛选能否单独宣布达标｜筛选产出的是值得合成的目标分子；密度、晶体、爆轰和感度的达标陈述都在合成与测试之后｜第 4–9 页｜推断
- 对 ICM-102 能量的原文比较｜表 1：ICM-102 爆速 9169 m s−1、爆压 34.3 GPa；HMX 爆速 9221 m s−1、爆压 39.2 GPa。第 8 页另写爆压 34.2 GPa，并写 “lower than those of HMX (39.2 GPa)”。第 9 页写 “comparable to HMX”｜第 8–9 页｜原文事实
- 对 ICM-102 感度的原文比较｜冲击 “>60 J”、H50 “320 cm”、摩擦 “>360 N”，文中称为与 TATB 相当｜第 9 页｜原文事实
- 氧平衡窗口对应的感度统计｜氧平衡 −80% 到 −40%、密度高于 1.90 g cm−3 的化合物 “impact sensitivities of >30 J”。这是 >30 J，正文在这里没有写成 TATB 的 >60 J｜第 3 页｜原文事实
- 石墨状已知物｜“graphite-like HEDMs (e.g., DAAF and DAAzF) … detonation velocity > 8600 m/s and very low impact sensitivities (IS > 60 J)”｜第 4 页｜原文事实
- 五元环例子｜5-amino-3-nitro-1,2,4-triazole (ANTA) “fails to form a graphite-like layered packing”｜第 4 页｜原文事实
- 六元环之外的适用性｜摘要：“Besides the considered system of six-member aromatic and hetero-aromatic rings, this materials genome approach can also be applicable …”｜第 1 页｜原文事实
- 讨论中的扩展方向｜“expanding this approach to multiple or fused hetero-aromatic ring systems”｜第 9 页｜原文事实
- 上述两句是否已经覆盖五元杂环筛选｜两句没有给出五元母环清单、筛选漏斗或该候选物的爆轰与感度。它们是适用性或后续途径的陈述｜第 1、9 页｜推断
- HMX 的氧平衡是否落在筛选窗口内｜表 1：HMX 的 CO2 氧平衡为 −21.69%，TATB 为 −55.81%。窗口是 −80% 到 −40%｜第 3、9 页｜推断

## 覆盖判断

- 五元杂环进入本文已执行的筛选库｜不覆盖。已执行库是 14 种六元芳香环或氮杂六元环（第 4 页）。五元三唑 ANTA 只作为未形成石墨状堆积的例子（第 4 页）。第 1 页和第 9 页没有五元杂环的筛选结果。
- 氧平衡 −80% 到 −40% 这条边界本身可按分子式计算｜覆盖。该边界按组成计算，正文没有把它限制为六元环（第 3 页）。它判定的是文中所称的低感度有利区间，不是 HMX 能量。
- 平面杂芳环与石墨状堆积两条特征，文字上可向环系外讨论｜部分覆盖。特征在第 3–4 页写成 IHE 的一般边界；执行枚举仍是六元环（第 4 页）；五元 ANTA 被用于说明只满足部分氢键条件仍会失败（第 4 页）。
- 不新合成，只靠筛选判定性质已经达到｜不覆盖。筛选终点是 “worthy of our synthetic effort”（第 4 页）。晶体、实测密度、爆速、爆压和感度都在合成之后给出（第 5–9 页）。
- 能量达到 HMX｜不覆盖。三个遗传特征没有把 HMX 的爆速或爆压列为阈值（第 4 页）。EXPLO5 使用的是 ICM-102 的实测密度（第 8 页）。表中 ICM-102 爆压低于 HMX（第 9 页）。HMX 氧平衡 −21.69%，在 −80% 到 −40% 的窗口之外（第 3、9 页）。
- 不做感度测试，仍判定感度达到 TATB｜不覆盖。筛选给出的是低感度边界和 “potential” 堆积（第 4 页）。与该窗口直接相连的统计是冲击感度 >30 J（第 3 页）。与 TATB 并列的 >60 J、>360 N 和 H50 = 320 cm 来自合成后的 BAM 等测试（第 9 页）。
- 用遗传特征估计“可能较低感”｜部分覆盖。氧平衡、平面高对称和石墨状堆积被写成低感度的边界，TATB 氧平衡 −55.8% 落在窗口内（第 3–4 页）。正文没有把“可能”写成已达到 TATB 的测试结果。
- 同一五元杂环候选物同时达到 HMX 能量和 TATB 感度｜不覆盖。能量与 TATB 定量感度两条都未被筛选覆盖，化学对象也不在已执行库中（第 4、8–9 页）。

## 结论

不可用

## 阻塞缺口

已执行的筛选只枚举六元母环，并在合成前停在“值得合成”；HMX 能量和 TATB 感度的定量比较来自 ICM-102 合成后的实测密度、EXPLO5 和 BAM 等测试，现存正文没有五元杂环候选物的对应筛选输出。

## 未核查

补充信息全文不在本目录。正文指向 Supplementary Notes 1–6、Supplementary Figs. 1–23 和 Supplementary Tables 1–5，包括枚举明细、15 个合成子的结构、理论密度算法、晶体预测和 Gaussian 计算细节，这些页没有打开。图 2 的散点、图 4 的结构式和图 7 的静电势面中，正文或图注没有逐点写出的坐标没有重测。正文第 1–11 页的文本层已阅读。
