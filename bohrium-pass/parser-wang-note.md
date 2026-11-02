# 玻尔 PDF 解析对照

时间：2026-11-02。Bohr CLI 2.9.17。文件是 `materials/source/wang2018-hedm-genome.pdf`，11 页。

命令：

```text
node bohr-cli/run.js pdf parse --file wang2018-hedm-genome.pdf --equation 1 --table 2 --textual 1 --sync
```

返回 `status` 为 success。`charged_amount` 是 0.55，`amount_fen` 是 55。完整 JSON 里有账户字段，没有放进仓库。

文本层用 pypdf 抽出，解析结果用 `pdf result --formatted markdown`。

| 位置 | 文本层 | 解析结果 |
| --- | --- | --- |
| 第 9 页注 k | `C aHbNcOd:OB (%) = 1600×(d−a−b/2)/Mw` | `CaHbNcOg:OB (%) = 1600×(d-a—b/2)/Mw` |
| 方法里的元素分析计算值 | `C 4H6N6O4 (202.0451)` | `C4HNO4 (202.0451)` |

注 k 的 d 被写成 g。式子里 b 前面的减号被写成破折号。C4H6N6O4 的两个下标 6 没有了，括号里的 202.0451 还在。按解析出来的 C4HNO4 算，式量对不上 202.0451。
