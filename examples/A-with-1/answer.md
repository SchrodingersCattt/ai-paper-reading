# 文献身份

- 题名：Accelerating the discovery of insensitive high-energy-density materials by a materials genome approach（第 1 页）。
- 年份：2018（第 1 页页脚 “NATURE COMMUNICATIONS | (2018) 9:2444”；第 11 页 “© The Author(s) 2018”）。
- DOI：10.1038/s41467-018-04897-z（第 1 页）。
- 许可证原文（第 11 页）：“Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.”
- 篇幅与章节：全文 11 页均有文本层。第 1 页为题名与摘要段（无单独 Abstract 标题）。第 2 页起为 Results，其下有 Identification of key “genetic” features of IHE molecules、Rapid design and screening of new IHE molecules（第 4 页）、Synthesis and crystal structure（第 5 页）、Thermal properties、Solubility、Detonation properties（第 8 页）、Sensitivities（第 9 页）。第 9 页有 Discussion 与 Methods（General、Materials、Product characterization、Synthesis of ICM-102）。第 10 页有 Data availability 与 References。结果与讨论都在本文件中。

# 方法与条件

- 模型类别：材料基因组流程是识别 IHE 的结构“遗传”特征、用自编脚本枚举并按边界条件筛选、再实验合成目标分子。原文短句：“identification of “genetic” features, rapid molecular design, and screening, as well as experimental synthesis of a target molecule”。页码：第 1 页。标签：原文事实。
- 训练数据（实验）：晶体密度统计来自剑桥结构数据库中 1000 个以上中性 CHNO 有机物，并对照代表性炸药的撞击感度。原文短句：“crystal densities of more than 1000 neutral organic compounds ... from Cambridge Structural Database (CSD)”。页码：第 3 页。标签：原文事实。来源：实测（CSD 晶体密度；撞击感度按文中实验观察表述）。统计程序名：未说明。
- 训练数据（DFT）：本文没有该项。标签：推断。依据：第 2–11 页的方法、结果与讨论没有 DFT 训练集，也没有由 DFT 拟合的代理模型。
- 训练数据（经验力场）：本文没有该项。标签：推断。依据：第 2–11 页没有经验力场训练数据。
- 力场：本文没有该项。标签：推断。依据：第 8–10 页点名的程序是 Gaussian 09（Revision D.01）与 EXPLO5（v6.02），没有力场名称。
- 粗粒化：本文没有该项。标签：推断。依据：第 2–11 页没有粗粒化模型。
- 反应性：爆轰量由热化学程序根据密度和生成焓算出。原文短句：“evaluated using EXPLO5 (v6.02) program”。页码：第 8 页；程序再次出现于第 10 页。标签：原文事实。来源：计算。反应分子动力学：本文没有该项。标签：推断。依据：第 8–10 页只给出 EXPLO5 热化学计算，没有反应轨迹。
- 系综：本文没有该项。标签：推断。依据：全文没有分子动力学系综。
- 模拟时长：本文没有该项。标签：推断。依据：全文没有轨迹时长。
- 筛选库：只构造 14 种六元芳香环（苯环与氮杂芳香环，编码 P1–P14），取代基为硝基、氨基和氢。原文短句：“14 kinds of six-member aromatic rings (including benzene rings and N-hetero-aromatic rings) are selected and coded as P1 to P14”。页码：第 4 页。标签：原文事实。枚举程序：自编 Java scripts（第 4 页）。来源：计算。
- 筛选漏斗（个数）：176 个分子式，氧平衡边界后 45 个分子式、计入异构体 402 个分子，平面高对称 40 个，其中 7 个有可能形成类石墨堆积。原文短句：“176 suited molecular formulas were screened out ... decreased from 176 to 45 ... 402 molecules ... only 40 molecules ... only seven molecules”。页码：第 4 页。标签：原文事实。来源：计算（Java 枚举加遗传特征边界，第 4 页）。
- 氧平衡边界：CO2 氧平衡 −80% 到 −40% 作为第一条遗传特征。原文短句：“a relatively low CO2-based oxygen balance value in the range of −80 to −40%”。页码：第 3–4 页。标签：原文事实。氧平衡公式在第 9 页表注：“OB (%) = 1600×(d−a−b/2)/Mw”。来源：计算（公式在第 9 页；区间来自第 3 页对 CSD 密度的统计，统计程序未说明）。
- 第二、三条遗传特征：平面、高对称（文中举例 C1v 或更高）的芳香或杂芳香结构；类石墨晶体堆积，并用 15 个超分子合成子帮助判断。原文短句：“planar aromatic (or hetero-aromatic) structures with high symmetry” 以及 “the graphite-like crystal packing can be identified as the third “genetic” feature”。页码：第 3–4 页。标签：原文事实。
- 筛选阶段的终点：筛选止于结构边界和理论晶体密度，选出 P6NAAA。原文短句：“P6NAAA is finally screened as the target IHE molecule that is worthy of our synthetic effort”。页码：第 4 页。标签：原文事实。这一步没有对候选库给出相对 HMX 的爆速、爆压，也没有给出相对 TATB 的感度数值。
- 理论晶体密度：P6NAAA 的理论晶体密度为 1.91 g cm−3，为七个分子中最高。原文短句：“shows the highest theoretical crystal density (1.91 g cm−3) among seven molecules”。页码：第 4 页。标签：原文事实。来源：计算。计算程序所在页：正文指向 Supplementary Note 4，本 PDF 未给出程序或公式，程序名不能确定。
- 合成前要验证的预测：高密度和类石墨晶体结构。原文短句：“validate our predictions that the selected P6NAAA would be a high-density compound with graphite-like crystal structure”。页码：第 5 页。标签：原文事实。
- 温度（CSD 密度图）：图 2 密度轴写 “Density (g cm–3 at 295 K)”，正文写室温下密度 >1.90 g cm−3。页码：第 3 页。标签：原文事实。来源：实测（CSD 晶体密度）。295 K 是否为每条 CSD 记录的实测温度，正文未逐条说明，标未说明。
- 温度（样品密度）：表 1 注 “Measured density by a gas pycnometer at 298 K”。页码：第 9 页。标签：原文事实。来源：实测。无水 ICM-102 密度 1.95 g cm−3（第 5、8、9 页）。来源：实测。
- 温度（热分析与溶解）：DSC/TG 放热峰 284 °C（第 8 页）；真空 5 torr、150 °C、5 h 后密度 1.92 g cm−3（第 5 页）；水中溶解度对应 25 °C，DMSO 中另有 130 °C（第 8 页）。标签：原文事实。来源：实测。这些温度不是筛选变量。
- 压力：筛选没有压力边界。合成后处理写真空 5 torr（第 5 页）。标签：原文事实。来源：实测。分子动力学压力：本文没有该项。标签：推断。依据：全文没有动力学压力。爆压是 EXPLO5 输出，见下行。
- 密度（对照物，表 1）：TATB 1.94 g cm−3，HMX 1.90 g cm−3。页码：第 9 页表 1；TATB 1.94 g cm−3 亦见于第 4 页。标签：原文事实。表注 b 将 ρ 定义为气体比重瓶在 298 K 的测量值。来源：未说明（表注给出测量方式；TATB 与 HMX 是否在本实验重测，正文未说明）。
- 生成焓：ICM-102 用等键反应在 Gaussian 09（Revision D.01）中算得 −8.1 kJ mol−1。原文短句：“calculated by the isodesmic reaction approach using Gaussian 09 (Revision D.01) ... −8.1 kJ mol−1”。页码：第 8 页；第 9 页表注 c “Calculated heat of formation”；第 10 页再次写 Gaussian 09。标签：原文事实。来源：计算。表 1 中 TATB、HMX 的生成焓带表注 d “Measured heats of formation”。来源：实测（表注如此标注，数值来自文献，不是本文对五元环的计算）。
- 爆速与爆压（仅已合成的 ICM-102）：用实测室温密度 1.95 g cm−3 和上述生成焓，EXPLO5（v6.02）给出爆速 9169 m s−1、爆压 34.3 GPa。页码：第 8 页与第 9 页表 1、表注 e 和 f。标签：原文事实。来源：计算（程序第 8–10 页）。同一段另写爆压 34.2 GPa（第 8 页）。标签：原文事实。来源：计算。摘要把 1.95 g cm−3 与 9169 m s−1 写在同一句；密度按第 9 页表注为实测，爆速按第 8 页为计算。
- HMX 与 TATB 的爆轰对照：表 1 中 HMX 爆速 9221 m s−1、爆压 39.2 GPa 带表注 e/f，即 EXPLO5/6.02。页码：第 9 页。来源：计算。TATB 爆速 8114 m s−1、爆压 32.4 GPa 带表注 l “Ref. 9”。页码：第 9 页。来源：未说明（本文未写明该文献值是实测还是计算）。
- 感度测试：撞击感度用标准 BAM 落锤和特征落高 H50（2.5 kg 落锤），摩擦用 BAM 摩擦仪，另有静电感度。ICM-102 为撞击 >60 J、H50 = 320 cm、摩擦 >360 N、静电感度 1.85 J；TATB 为 >60 J、320 cm、>360 N、2.27 J；HMX 为 7.5 J、32 cm、120 N、0.099 J。页码：第 9 页正文与表 1、表注 g–j。标签：原文事实。来源：实测。
- 感度的分子模拟：图 7 给出 ICM-102、TATB、LLM-105、FOX-7 的静电势、硝基电荷和 ESP 平均偏差（ICM-102：硝基电荷 −0.564，最负电荷 −30.26，ESP 平均偏差 0.246）。页码：第 8–9 页。标签：原文事实。来源：计算。产生这些数的程序名在第 8–9 页未写出，不能确定。
- 体系大小：CSD 样本为 1000 个以上 CHNO 晶体（第 3 页）；枚举库为 14 个六元母环（第 4 页）；实验合成并完成能量与感度闭环的是一个六元嘧啶目标 ICM-102（2,4,6-triamino-5-nitropyrimidine-1,3-dioxide，第 1、5、9 页）。标签：原文事实。五元杂环在正文中作为堆积反例出现：5-amino-3-nitro-1,2,4-triazole（ANTA）有平面构型，但未能形成类石墨层状堆积（第 4 页）。标签：原文事实。ANTA 不在 P1–P14 枚举库中。

# 主张

- 目标是同时具有 HMX 的能量和 TATB 的感度。原文短句：“new IHE molecules are expected to have the TATB’s sensitivity and the HMX’s energy”；“the desired IHE molecule with HMX’s energy and TATB’s sensitivity”。页码：第 2 页、第 9 页。标签：原文事实。
- 六元环体系之外也可沿用该方法。原文短句：“Besides the considered system of six-member aromatic and hetero-aromatic rings, this materials genome approach can also be applicable”；“expanding this approach to multiple or fused hetero-aromatic ring systems”。页码：第 1 页、第 9 页。标签：原文事实。这是摘要和讨论中的可推广主张，对应的已执行库仍是六元环。
- ICM-102 的能量可与 HMX 相比、感度处于 TATB 一档。原文短句：“is comparable to HMX”；撞击与摩擦 “comparable to TATB”。页码：第 9 页。标签：原文事实。推断：表 1 中 ICM-102 的计算爆速 9169 m s−1 接近 HMX 的 9221 m s−1，计算爆压 34.3 GPa 低于 HMX 的 39.2 GPa（第 9 页）。该推断只描述这一个已合成的六元环分子。
- 预测与实验一致，因而该方法可以扩展。原文短句：“showing good agreement between prediction and experiment”。页码：第 9 页。标签：原文事实。推断：第 5 页写明合成前要验证的预测是高密度和类石墨堆积；爆速、爆压和感度是合成之后才给出的（第 8–9 页）。

# 覆盖判断

后续工作拆成下面几条。读者要在不再做新合成、不再做感度测试的前提下，只用这篇材料基因组筛选，判断一个五元杂环候选物能否同时达到 HMX 的能量和 TATB 的感度。

- 对象是五元杂环候选物：不覆盖。已执行的母环库是 14 种六元芳香环与氮杂芳香环（第 4 页）。五元环 ANTA 只用于说明平面分子仍可能得不到类石墨层（第 4 页），没有进入枚举和漏斗。第 1 页和第 9 页的 “can also be applicable” 与 “expanding” 是主张，没有对应的五元环样品或筛选清单。
- 只用筛选、不再做新的合成：不覆盖。流程第三步是合成筛出的目标（第 2、5、9–10 页）。筛选的终点是 “worthy of our synthetic effort”（第 4 页）。爆速和爆压使用的是合成样品的实测密度 1.95 g cm−3（第 8 页）。
- 不再做感度测试：不覆盖。与 TATB 比较的撞击、落高、摩擦和静电感度来自 BAM 等实验（第 9 页表 1）。图 7 的静电势和硝基电荷是对已合成 ICM-102 及已知分子的事后解释（第 8–9 页），没有成为筛选库的感度过滤器，也没有给出可与 TATB 实验感度互换的判据。
- 判断能否达到 HMX 的能量：不覆盖。HMX 对照是 EXPLO5 爆速 9221 m s−1、爆压 39.2 GPa（第 9 页，来源：计算）。同一套 EXPLO5 计算只用于已合成的六元环 ICM-102（第 8 页）。七个六元环候选只比较了理论晶体密度（第 4 页），筛选没有把 HMX 的爆速或爆压当作通过线。五元杂环候选没有这条计算。
- 判断能否达到 TATB 的感度：不覆盖。TATB 的低感度在表 1 中是实验值（第 9 页，来源：实测）。氧平衡、平面高对称和类石墨堆积被用作结构边界（第 3–4 页）。正文没有把这三条写成可单独代替感度测试、并判定达到 TATB 感度的定量条件。
- 把三条遗传特征当作结构边界再拿去看一个新分子：部分覆盖。这三条边界确实被用在六元环库上，并把库从 176 个分子式收到 1 个合成目标（第 3–4 页）。与后续工作不一致的是对象和终点：库内没有五元杂环（第 4 页）；通过边界也不等于已经达到 HMX 能量和 TATB 感度（能量与感度在第 8–9 页才对 ICM-102 给出）。

# 结论

不可用

# 阻塞缺口

全文实际枚举筛选的是 14 种六元芳香环（第 4 页），HMX 能量与 TATB 感度的数值结论建立在已合成 ICM-102 的实测密度、EXPLO5 计算和 BAM 等感度实验上（第 8–9 页），因此没有一条已执行的筛选条件能够在不做新合成、不做感度测试的情况下判断五元杂环候选物是否同时达到这两项指标。

# 未核查

补充信息（正文引用的 Supplementary Note 1–6、Supplementary Figs. 1–23、Supplementary Tables 1–5）不在本 PDF 内，第 10–11 页只给出 https://doi.org/10.1038/s41467-018-04897-z 的补充材料链接；其中第 4 页理论密度 1.91 g cm−3 的程序、第 4 页 15 个合成子的图，以及 ANTA 堆积的 Supplementary Fig. 3 都未打开。图 2–5 与图 7 的结构式绘图未逐原子读取，未写入正文的拟合斜率、误差棒和坐标细值未采用。本 PDF 第 1–11 页均已打开。
