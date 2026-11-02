# 这篇筛选盖不住“不合成、不测感度”的下一步

Wang et al., *Nature Communications* 9, 2444 (2018)，DOI [10.1038/s41467-018-04897-z](https://doi.org/10.1038/s41467-018-04897-z)。PDF 末页是 CC BY 4.0，全文在 `materials/source/wang2018-hedm-genome.pdf`。

读者要问的是：不新合成、不测感度，只用这篇材料基因组筛选，能不能判断一个五元杂环同时达到 HMX 的能量和 TATB 的感度。

核对后的结论是不可用。摘要里的 “can also be applicable” 说方法还可以用到六元环以外的含能分子。已经做完的库是 14 种六元环。

## 摘要把三件事写成一句

第 1 页把 measured density 1.95 g cm−3 和 detonation velocity 9169 m s−1 放在同一段，并写方法 “can also be applicable”。密度是测出来的，爆速是程序算的，五元环筛选没有做。页码和原句在 `evidence/quotes.md`。

- 第 4 页的库是 14 种六元环，编号 P1–P14。五元环 ANTA 只作为没有形成石墨状堆积的例子出现，不在这个库里。
- 第 8 页用 EXPLO5 v6.02 算出 9169 m s−1。计算输入里用了实测密度 1.95 g cm−3。
- 第 9 页表里 HMX 的 CO2 氧平衡是 −21.69%。筛选窗口是 −80% 到 −40%。撞击和摩擦感度来自合成 ICM-102 之后的 BAM 实验。

所以这四条都对不上已执行的筛选：对象不是六元环，能量不是筛选的输出，感度不是筛选的输出，论文自己的第三步是合成。

| 要核对的事 | 看哪里 |
| --- | --- |
| 推广句是否对得上已执行的库 | 第 1 页 “can also be applicable”；第 4 页只有 P1–P14 |
| 同一句里的密度和爆速是否同一种来源 | 第 1 页 measured density；第 8 页 EXPLO5 |
| 许可证 | Wang、Zeng 的 PDF 末页是 CC BY 4.0。Lee et al., *npj Computational Materials* 10, 208 (2024) 第 11 页是 CC BY-NC-ND。`bohrium-pass/prompt.txt` 里写成了 CC BY，文件保持发出时的原文，更正写在 `bohrium-pass/prompt-as-sent.md` |

## 核对时按这个顺序

步骤在 `skill/SKILL.md`，版本 `method-fit-check-v2`。文件里没有这两篇论文的答案。

1. 先数页。结果或讨论不在文件里就停止，摘要里的数字留在摘要。
2. 论文没有的项写“本文没有该项”。
3. 每个带单位的数标成实测、计算或未说明。计算要写出程序或公式所在的页。
4. “也可适用、可推广”只算主张。覆盖判断引用实际做过的库、样品或轨迹。
5. 后续工作拆成对象、能量、感度和还要不要做实验。关键条件有一条不覆盖，结论就不是可用。

`skill/check_answer.py` 只检查 UTF-8 和这些词。

没有这份 Skill 的对照，用同一段任务、同一个 `grok-4.7-high`、同一份 PDF。任务原文不缩短。

## 全文、换一篇论文、只留前两页

Wang 全文、有 Skill 的三次结论都是不可用。9169 标成计算，BAM 感度标成实测。用时 385.2 s、406.8 s、499.1 s。第三次是同一任务的复测，结论不变。第一次在 `examples/A-with-1/answer.md`，复测在 `examples/A-with-retest/answer.md`。

没有 Skill 的两次用时 105.8 s 和 133.0 s。会话里同样写出不覆盖，并提到六元环、EXPLO5 和 −21.69%，见 `examples/A-without-1/visible-from-stream.md`。落盘的 `answer.md` 仍是合法 UTF-8，汉字被换成了 `?`。会话里的 `9169 m s−1` 和 `−80%` 落到盘上是 `9169 m s?1` 和 `?80%`，减号和汉字是同一次替换。成因在 `evidence/encoding.md`。

两侧对覆盖范围的判断一致。有 Skill 的文件多出来的是页码、实测/计算标签，以及一份打开就是中文的 UTF-8。没有 Skill 的两次更短。

同一份 Skill 换到 Zeng et al., *Nature Communications* 11, 5713 (2020)，DOI [10.1038/s41467-020-19497-z](https://doi.org/10.1038/s41467-020-19497-z)，末页 CC BY。问题换成约 1 atm、低于 2000 K 的稀释甲烷–空气火焰。结论不可用：原文轨迹是 3000 K、0.25 g/cm3 的纯 CH4/O2，约 1 atm 没有写出。用时 324.8 s。`examples/B-with/answer.md`。

只保留 Wang 2018 前两页、文件名写明 constructed 的那份上，两次都停止。9169 标成未说明，没有用后文补 EXPLO5。用时 328.1 s 和 356.2 s。`examples/C-with/answer.md`，复测在 `examples/C-with-retest/answer.md`。

| 误读 | 论文位置 | 有 Skill | 无 Skill 的会话 |
| --- | --- | --- | --- |
| 9169 是实测爆速 | 第 8 页，EXPLO5 v6.02 | 标计算 | 写到 EXPLO5 |
| 五元环已经筛过 | 第 4 页只有 P1–P14 | 不覆盖，结论不可用 | 写到六元环，结论不覆盖 |
| HMX 落在氧平衡窗口内 | 第 9 页 −21.69%，窗口 −80% 到 −40% | 写明在窗口外 | 写到 −21.69% |
| 前两页就够下结论 | 案例 C 没有结果页和讨论 | 停止；9169 标未说明 | 这次只跑了有 Skill |

## 在玻尔里问同一篇

这一版 `bohr chat` 接收的是文本。第 1 页适用性句、第 4 页六元环库和第 8 页 EXPLO5 句贴在 `bohrium-pass/prompt-wang.txt`。

调用用的是本机已登录的 Bohr CLI 2.9.17。中文消息用 `node` 跑 `bohr-cli/run.js` 的 `chat`，把提示文件全文作为消息。走 `bohr.cmd` 时，请求只剩约 71 个 prompt token，模型看不到摘录。改用 `node` 之后，`bohrium-pass/chat-public.json` 是 413 个 prompt token，`bohrium-pass/chat-wang-public.json` 是 432。

Wang 这次返回的模型是 `chenkun/gpt-5-nano`。公开 JSON 去掉了账户余额，回答没有改。它写出 9169 是计算，也写出五元环没有被筛过，结论仍是“部分可用”。上面的规则是：关键条件不覆盖，结论就不是可用。

`bohr paper search` 用 Lee et al. 2024 的 DOI 返回 0 条。打开 PDF 第 11 页，许可证是 CC BY-NC-ND，这篇没有放进仓库。

## 注 k 代不回 −55.45，1.95 也不是黄色初样

第 9 页表 1 写着 −55.45。注 k 印出的式子是 `1600×(d−a−b/2)/Mw`，`a` 前面没有系数。第 10 页印着 C4H6N6O4（202.0451）。`evidence/ob_formula_check.py` 用这个式量得到 −23.7571。常见的 `(d−2a−b/2)` 接近 −55.45，那个 `2` 不是注 k 这一行上的字。演算在 `evidence/ob-formula.md`。

1.95 g cm−3 是无水样品。第 5 页的黄色初样是一水合物；150 °C、5 torr、5 h 之后测到 1.92 g cm−3。第 7 页把 1.95 写给无水样品。第 9 页表 1 的 1.95 对的是这一条，注 b 是气比重瓶、298 K。

另一次只放 PDF、不放 Skill 的阅读（382.3 s，`grok-4.7-high`）读到了同一处：注 k 是 `(d−a−b/2)`，第 10 页是 C4H6N6O4（202.0451），1.95 写在无水样品上。可见文字在 `examples/claim-check/visible-from-stream.md`。

这几页的摘录发给 `bohr chat` 的提示是 `bohrium-pass/prompt-formula-density.txt`。模型仍是 `chenkun/gpt-5-nano`。

- 第一次，prompt token 557。返回只有“摘录未出现代入过程”和“摘录不支持”，没有结论词。`chat-formula-density-public.json`。
- 同一提示再发一次，prompt token 仍是 557。两句写成“摘录未出现代入过程 部分可用”和“摘录不支持 不可用”。`chat-formula-density-2-public.json`。
- `prompt-formula-density-strict.txt` 只多了输出限制：只写三行，两句不一致就取更严的一个。prompt token 671。返回是句1 摘录未出现代入过程，句2 摘录不支持，结论不可用。`chat-formula-density-3-public.json`。

三次返回都没有改写。

玻尔这边可以按这个顺序重做：

1. 中文提示走 `node bohr-cli/run.js chat`，消息用提示文件全文。先看返回里的 prompt token。停在几十个 token，说明摘录被截掉了，结果不能用来核对论文。
2. 问 Wang 时用 `prompt-wang.txt`。期望它写出 9169 是计算，并且不要把结论收成可用。这次原返回停在“部分可用”，因为提示里还没有“关键条件不覆盖就不是可用”。
3. 问注 k 和 1.95 时用 `prompt-formula-density-strict.txt`。期望三行：代入过程未在摘录中出现，1.95 那句摘录不支持，结论不可用。不限行数的两次原提示留在同目录，那两次没有把结论收成一个词。
4. 用 DOI 检索到 0 条时，打开 PDF 末页看许可证，再决定这篇能不能放进公开仓库。
5. 用玻尔解析 PDF 时，分子式和下标要回对文本层。2026-11-02 对 Wang 全文跑了一次 `pdf parse`（Bohr CLI 2.9.17，`--equation 1 --table 2 --textual 1 --sync`）。返回 `status` 为 success，`charged_amount` 是 0.55，`amount_fen` 是 55。解析把第 9 页注 k 的 `C aHbNcOd` 写成 `CaHbNcOg`，把 `1600×(d−a−b/2)/Mw` 写成 `1600×(d-a—b/2)/Mw`，并把方法里的 `C 4H6N6O4 (202.0451)` 写成 `C4HNO4 (202.0451)`。两个下标 6 没了，式量还在。对照句在 `bohrium-pass/parser-wang-note.md`。

费用以当次返回为准。

## 复现全文对照

1. 模型用 `grok-4.7-high`。换成 Auto 就是另一次实验。Cursor agent CLI 版本是 `2026.10.19-6bbf2c4`。
2. 空目录里只放 PDF，文件名用 `paper.pdf`，再放下面的任务。有 Skill 的那次另放入 `skill/SKILL.md` 和 `skill/check_answer.py`。`cases/` 里的验收标准留在运行目录外面。
3. 新进程，不要 `--resume`。两侧都加 `--force` 和 `--sandbox disabled`。

```text
agent --print --output-format stream-json --model grok-4.7-high --trust --force --sandbox disabled --workspace <该目录> -- "<任务全文>"
```

任务原文：

```text
读者想不经过新的合成和感度测试，只用这篇材料基因组筛选，判断一个五元杂环候选物能不能同时达到 HMX 的能量和 TATB 的感度。请只根据本目录的 PDF 判断。如果本目录存在 SKILL.md，严格按它执行。把结果写入 answer.md。
```

4. 打开 `answer.md`。最低检查：结论是“不可用”；9169 标为计算并指向 EXPLO5；五元环不在 P1–P14；文件是 UTF-8。运行前写好的完整标准在 `cases/A/acceptance.md`。

## 文件

| 路径 | 内容 |
| --- | --- |
| `evidence/quotes.md` | 上面几处原文的页码，以及 1.95、1.92 和注 k |
| `evidence/ob-formula.md` | 注 k 为什么代不回 −55.45 |
| `evidence/ob_formula_check.py` | 用 202.0451 算出 −23.7571 |
| `evidence/encoding.md` | 无 Skill 的 `answer.md` 为什么是问号 |
| `skill/SKILL.md` | v2 步骤 |
| `materials/source/*.pdf` | 两篇 CC BY 全文，以及案例 C 的两页残缺件 |
| `examples/` | 有 Skill、无 Skill、换论文和残缺件的原始结果。无 Skill 的 `answer.md` 是落盘原件 |
| `cases/` | 运行前写好的任务和验收 |
| `bohrium-pass/` | 发出的提示，以及去掉账户余额后的返回。`parser-wang-note.md` 是 PDF 解析和文本层的两处差别 |
