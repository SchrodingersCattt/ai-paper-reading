# Fig. 5 原文核对与问答测试

## 问题与输入

在 Zeng 等人 2020 年论文 PDF 第 6 页，读者要知道 Fig. 5 中各方框及箭头的方向。已有基础问答只收到 Uni-Parser 的第 6 页文本：包含图注和方法描述，不包含图中标签或连线。文字层增强问答另外收到图内文字坐标，但未收到箭头路径。两次原回答在本次测试前已保存。

本次将同一基础提问、同一页解析文本，加上从同一原 PDF 提取的节点和矢量箭头记录，传给相同的 `gpt-5-nano` 接口两次。新输入增加了原图结构，不能把结果当成只有提示措辞变化的消融实验。单个案例和两次回答也不能证明对其他 PDF 稳定有效。

## 运行前人工核对的原图

Fig. 5 的节点按原图为：Molecular system；Sampling with ReaxFF；Redundancy removal；Dataset；QM calculation；NN training；Re-sampling；New data?；Final dataset。Active learning 是包围区域的名称，YES、NO 是分支标记。

逐条箭头为：

1. Molecular system → Sampling with ReaxFF。
2. Sampling with ReaxFF → Redundancy removal。
3. Redundancy removal → Dataset。
4. Dataset → QM calculation。
5. QM calculation → NN training。
6. NN training → Re-sampling。
7. Re-sampling → New data?。
8. New data? → Dataset，分支 YES。
9. New data? → Final dataset，分支 NO。

## 验收项目

每次输出与原图独立对照并记录：

1. 九个节点名称与节点身份；Active learning 不是一个流程节点。
2. 九条箭头的方向，尤其 Redundancy removal → Dataset 和 Dataset → QM calculation。
3. YES 回到 Dataset、NO 到 Final dataset，不能把该流程误写成单向直线。
4. ReaxFF 是初始采样，QM 计算参考能量和力，NN 用参考数据训练；缺乏图文依据的额外细节单独标记。
5. 将图中信息与原文 Methods 的补充信息分开，标注 PDF 第 6 页 Fig. 5 或方法页。

真实响应全部保存。节点和箭头先由程序输出，再由原图核查；当检测到形状或方向不明确时程序报错，不自动补边。验证条件是本篇有文字层和矢量路径的 PDF，不外推至扫描件或其他图形。
