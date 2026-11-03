# 方法段补充问答核对

在图结构问答后，我把玻尔解析出的 PDF 第 7 页 QM calculation 原文块和三个核查问题补进同一提问：初始数据集在去冗余前还是后、聚类用什么表示、QM 提供哪些参考量。标准分别在两轮请求前写入[原始标记标准](zeng-figure-method-ambiguous-protocol.md)和[明确标记标准](zeng-figure-method-explicit-protocol.md)。

第一次使用 `[P7-8]` 表示“第 7 页第 8 块”。两次请求返回同一个 completion ID、相同回答，按一份结果记录。[这份回答](zeng-figure-method-ambiguous-answer.txt)答对了三个方法问题，但一处把 QM 原文块称为第 6 页，另一处将 `P7-8` 说成第 7 页到第 8 页之间，定位互相冲突。

随后将同一原文标为 `[PDF_PAGE_7_BLOCK_8]`，明确 BLOCK 是块号，用不同请求标识再次调用两次。两个 completion ID 不同，完整回答见[运行 1](zeng-figure-method-explicit-answer-1.txt)和[运行 2](zeng-figure-method-explicit-answer-2.txt)。

| 核查项 | 明确标记运行 1 | 明确标记运行 2 |
| --- | --- | --- |
| 9 条箭头与 YES／NO | 与输入图结构及原图一致 | 与输入图结构及原图一致 |
| 初始数据集和去冗余的先后 | 正确 | 正确 |
| Coulomb 矩阵的特征谱用于聚类 | 正确 | 正确 |
| QM 参考势能和力，Gaussian 16、MN15/6-31G** | 正确 | 正确 |
| QM 原文位置 | 第 7 页 BLOCK 8 | 第 7 页 BLOCK 8 |

两次回答都拿到了由原图提取的节点和箭头，因此图结构正确反映的是它们按补充材料组织了结果。运行 1 对部分箭头的依据主要引用正文中的方法顺序；图中具体连线还应对照矢量结果和原图。运行 2 把原图题首的 “Fig. 5” 写成了 “Figura 5”，引用图题时应按原图核对。

明确块号后，两份回答都没有重现先前的页码冲突；这两次观察不足以判断该写法的稳定性。全部输入可重建，[哈希与模型记录](zeng-figure-method-metadata.json)保留了唯一响应数和结果身份的哈希。
