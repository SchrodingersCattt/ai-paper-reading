# Zeng 2020：方法与结果核查

论文：J. Zeng et al., “Complex reaction processes in combustion unraveled by neural network-based molecular dynamics simulation,” *Nature Communications* 11, 5713 (2020), DOI 10.1038/s41467-020-19497-z。页码指 [出版方 PDF](../materials/source/zeng2020-methane-nn-md.pdf) 的页码。

| 核查项 | 原文位置 | 依据与解释 |
| --- | --- | --- |
| 初始采样 | 第 6 页，Methods / Reference dataset，Fig. 5 | ReaxFF 反应性 MD 产生初始采样；截断 5 Å 用于围绕原子构建局部簇。 |
| 减少冗余和补充数据 | 第 6—7 页，Methods / Reference dataset，Fig. 5 | 初始结构经分类、聚类和重采样；四个模型的预测用于主动学习补充构型。 |
| 参考值 | 第 7 页，Methods / QM calculation | Gaussian 16 在 MN15/6-31G\*\* 水平计算每个最终数据构型的能量和原子力。 |
| 模型 | 第 7 页，Methods / Training of the NN PES，Fig. 6 | DeepPot-SE 使用 DeePMD-kit 训练；6 Å 是模型描述符的截断半径。损失包含能量和力误差。 |
| 误差 | 第 2 页，Results / Accuracy of the NN PES | 训练集和测试集的能量 MAE 是 0.04 和 0.14 eV/atom；原子力 MAE 是 0.12 eV/Å。正文对应的细节另见 Supplementary Table 1 和 Supplementary Fig. 1，本仓库未包括补充材料。 |
| 生产模拟 | 第 2 页，Results / The initial stage of combustion | 100 CH4、200 O2、0.25 g/cm3、3000 K、NVT、1 ns、0.1 fs。作者将高温高密度用于提高碰撞和采样效率。 |
| 稀释和目标条件 | 第 2—3 页，Results | 文中提到实验通常以较惰性气体稀释燃料；更接近实验的条件属于未来工作。正文在相关轨迹处没有给出压力数值。 |

本次玻尔输入是人工选择并整理的摘录，见 [提示](../bohrium-pass/zeng-prompt.txt)；返回见 [实际响应](../bohrium-pass/zeng-response-public.json)。
