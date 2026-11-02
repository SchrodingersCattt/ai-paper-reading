# 核对用的原文短句

页码按 Wang et al., Nature Communications 9, 2444 (2018) 的 PDF。引号内是文本层里的句子，连字符以 PDF 抽出为准。

## 摘要把两类数写在一起

第 1 页把 measured density 1.95 g cm−3、decomposition temperature 284 °C、detonation velocity 9169 m s−1、impact sensitivity >60 J、friction sensitivity >360 N 放在同一段。紧接着是：the considered system is six-member aromatic and hetero-aromatic rings, and the approach “can also be applicable” to new energetic materials。这句没有给出五元环清单。

## 已执行的库

第 4 页：“14 kinds of six-member aromatic rings (including benzene rings and N-hetero-aromatic rings) are selected and coded as P1 to P14”。同一页写氧平衡边界 “−80 to −40%”，并把 5-amino-3-nitro-1,2,4-triazole (ANTA) 写成没有形成石墨状堆积的例子。ANTA 不在 P1–P14 里。

## 9169 是计算

第 8 页：detonation velocity and pressure “were evaluated using EXPLO5 (v6.02)”。算出的爆速是 9169 m s−1。输入包含 measured density 1.95 g cm−3。第 9 页表 1 里 HMX 的 CO2 氧平衡是 −21.69%，不在 −80% 到 −40% 的窗口内。表中 ICM-102 的撞击、摩擦感度来自 BAM 等实验。

因此：密度和感度可以标实测；9169 必须标计算；“can also be applicable” 不是已完成的五元环筛选。

## 1.95 与 1.92 不是同一样品

第 5 页：刚得到的中性样品是黄色。元素分析 N% 38.01、C% 21.65，接近 ICM-102·H2O 的计算值 N% 38.18、C% 21.82。单晶确认是一水合物。同一页把该样品加热到 150 °C、真空 5 torr、5 h，颜色从亮黄变为橙色，实测密度 1.92 g cm−3。

第 7 页：无水样品由一水合物在热 DMSO/EtOAc 中重结晶得到，颜色比 150 °C 加热后的样品更深，实测密度 1.95 g cm−3。

第 9 页表 1 的 ρ 是 1.95 g cm−3。注 b 写明气比重瓶、298 K。这是无水样品的密度，不是黄色一水合物的密度。

## 注 k 与表中 −55.45

第 9 页表 1 的 OBk 是 −55.45%。注 k 印出 OB (%) = 1600×(d−a−b/2)/Mw。a 前面是减号。第 10 页元素分析计算值写着 C4H6N6O4 (202.0451)。代入过程不在这两页上。演算在 `evidence/ob-formula.md`。
