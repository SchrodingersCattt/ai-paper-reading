# 表里的数，不等于脚注式子或黄色样品的结果

Wang et al., *Nature Communications* 9, 2444 (2018)，DOI [10.1038/s41467-018-04897-z](https://doi.org/10.1038/s41467-018-04897-z)。PDF 末页是 CC BY 4.0。全文在 `materials/source/wang2018-hedm-genome.pdf`。

两处印出来的数会被读成另一件事的结果。页码和原文短句在 `evidence/quotes.md`。

## 注 k 代不回 −55.45

第 9 页表 1 把 ICM-102 的 CO2 氧平衡写成 −55.45%。注 k 印出的式子是：

`OB (%) = 1600×(d−a−b/2)/Mw`

a 前面是减号，没有系数。第 10 页元素分析的计算值写着 C4H6N6O4（202.0451）。PDF 没有把这次代入印出来。

`evidence/ob_formula_check.py` 用论文给出的 202.0451。印出的 `(d−a−b/2)` 是 4−4−6/2 = −3，1600×(−3)/202.0451 = −23.7571。表中是 −55.45。若把式子改成常见的 `(d−2a−b/2)`，同一式量得到 −55.4332，接近表值，但那个 2 不是注 k 印出来的。C、H、N、O 取 12、1、14、16 时，带 `2a` 的结果是 −55.4455。

所以表里的 −55.45 不是注 k 印出的式子代入 C4H6N6O4 的结果。多出来的 `2a` 是我们补的。演算写在 `evidence/ob-formula.md`。

## 1.95 不是黄色一水合物的密度

第 5 页：刚得到的中性样品是黄色。元素分析 N% 38.01、C% 21.65，接近 ICM-102·H2O 的计算值 N% 38.18、C% 21.82。单晶确认是一水合物。同一页把该样品加热到 150 °C、真空 5 torr、5 h，颜色从亮黄变为橙色，实测密度是 1.92 g cm−3。

第 7 页：无水样品由一水合物在热 DMSO/EtOAc 中重结晶得到。它的颜色比 150 °C 加热后的样品更深，实测密度是 1.95 g cm−3。

第 9 页表 1 的 ρ 是 1.95 g cm−3，注 b 写明气比重瓶、298 K。这是无水样品的密度，不是黄色一水合物的密度。

## 筛选句仍然不能代替已执行的库

上一版公开稿把玻尔示例放在一篇未入库的论文上，得 83 分。阅读问题仍是：不新合成、不测感度，只用这篇材料基因组筛选，能不能判断一个五元杂环同时达到 HMX 的能量和 TATB 的感度。

第 1 页把 measured density 1.95 g cm−3 和 detonation velocity 9169 m s−1 写在同一段，并说方法 “can also be applicable” 于六元环以外的含能材料。已测量的密度、程序算出的爆速、还没做的筛选因此叠在一起。上面两节把 1.95 和表中的氧平衡拆开；筛选库本身仍要单独看：

- 已执行的库在第 4 页，是 14 种六元环（P1–P14）。五元环 ANTA 只是没有形成石墨状堆积的例子，不在库里。
- 9169 m s−1 在第 8 页由 EXPLO5 v6.02 算出。
- 第 9 页表里 HMX 的 CO2 氧平衡是 −21.69%，而筛选窗口是 −80% 到 −40%。撞击和摩擦感度来自合成 ICM-102 之后的 BAM 实验。

后续工作的四条都不被已执行的筛选覆盖：对象不是六元环，能量不是筛选输出，感度不是筛选输出，而且论文自己的第三步是合成。结论是不可用。

| 可带走的规则 | 核对位置 |
| --- | --- |
| 脚注式子没有代入过程时，不能把表值说成该式的输出 | 第 9 页注 k `(d−a−b/2)`；第 10 页 C4H6N6O4（202.0451）；演算 −23.7571，表中 −55.45 |
| 表中密度要对到样品，不按颜色就近 | 第 5 页黄色一水合物与加热后的 1.92；第 7 页无水样品 1.95；第 9 页表 1 |
| 推广句不能代替已执行的库 | 第 1 页 “can also be applicable”；第 4 页只有 P1–P14 |
| 同一句里的密度和爆速要拆来源 | 第 1 页 measured density；第 8 页 EXPLO5 |
| 许可证看 PDF 末页，不看提示词 | Wang、Zeng 末页是 CC BY 4.0。Lee 2024 第 11 页是 CC BY-NC-ND，`prompt.txt` 里的 CC BY 是写错的 |

## 方法

`skill/SKILL.md` 版本 `method-fit-check-v2`。它不包含这两篇论文的答案。步骤是：先数页；论文没有的项写“本文没有该项”；每个带单位的数标实测、计算或未说明；推广句必须对到已执行的库或轨迹；关键条件有一条不覆盖，结论就不是可用。`skill/check_answer.py` 只查 UTF-8 和这些词，不判断科学对错。

没有 Skill 时，同一段任务、同一个 `grok-4.7-high`、同一份 PDF 直接回答。不要把基线的问题改短。

## 对照里实际发生的事

有 Skill 的三次都写成不可用，并且把 9169 标成计算、把 BAM 感度标成实测。耗时 385.2 s、406.8 s、499.1 s。第三次是同一任务的复测，结论不变。原文在 `examples/A-with-1/answer.md`。

没有 Skill 的两次更快，105.8 s 和 133.0 s。会话里也得出不覆盖，并提到六元环、EXPLO5 和 −21.69%，见 `examples/A-without-1/visible-from-stream.md`。落盘的 `answer.md` 是合法 UTF-8，汉字被换成了 `?`。`m s?1` 和 `?80%` 是同一次替换，不是另一套损坏。成因见 `evidence/encoding.md`。增益是页码账本，不是把错结论改对，也不是更省时间。

同一 Skill 换到 Zeng et al., *Nature Communications* 11, 5713 (2020)，CC BY。问题换成约 1 atm、低于 2000 K 的稀释甲烷–空气火焰。结论不可用：原文轨迹是 3000 K、0.25 g/cm3 的纯 CH4/O2，约 1 atm 没有写出。324.8 s。`examples/B-with/answer.md`。

只留 Wang 2018 前两页、并标明 constructed 的文件上，两次都停止。9169 标成未说明，没有补出后文的 EXPLO5。328.1 s 和 356.2 s。

## 在玻尔里问这两句

`bohr chat` 这一版没有 PDF 接口。氧平衡和密度这两句的摘录在 `bohrium-pass/prompt-formula-density.txt`，分别来自第 5、7、9、10 页。调用用 `node` 跑 `bohr-cli/run.js chat`。不要走 `bohr.cmd` 传中文，否则提示会被截成约 71 个 prompt token，模型看不到摘录。

同一份提示打了两次，模型都是 `chenkun/gpt-5-nano`，prompt token 都是 557。账户余额已从两份公开返回里去掉。原文没有改写。

第一次在 `bohrium-pass/chat-formula-density-public.json`。模型写“摘录未出现代入过程”和“摘录不支持”，没有从“可用、部分可用、不可用、材料不足停止”里选词，也没有写阻塞缺口。

第二次在 `bohrium-pass/chat-formula-density-2-public.json`。原文三行是：`摘录未出现代入过程 部分可用`，`摘录不支持 不可用`，然后单独一行“阻塞缺口”，后面没有句子。第一句被标成部分可用，第二句被标成不可用。提示词要求全文只有一个结论词。两次都没有把注 k 的式子改成 `(d−2a−b/2)`，也都没有把 1.95 说成黄色一水合物的密度。

第三次只改输出格式，不改摘录。`prompt-formula-density-strict.txt` 要求固定三行，并且两句不一致时结论取更严的一个。返回在 `chat-formula-density-3-public.json`，模型仍是 `chenkun/gpt-5-nano`，prompt token 671。原文是：句1 摘录未出现代入过程；句2 摘录不支持；结论 不可用，阻塞缺口是代入过程未出现。这次没有再写两个结论词。

读者可以按这六步重做，不需要我们的结论：

1. 用 `node` 调用 `bohr-cli/run.js chat`，消息用 `prompt-formula-density.txt` 的全文。确认 prompt token 不是约 71。
2. 记下返回里的结论词，不要改字。
3. 打开 PDF 第 9 页注 k，核对式子是不是 `(d−a−b/2)`。
4. 打开第 10 页，核对计算值是不是 C4H6N6O4（202.0451）。
5. 打开第 5 页和第 7 页，核对 1.92 属于 150 °C 加热后的样品、1.95 属于无水样品。
6. 运行 `evidence/ob_formula_check.py`。印出的式子应得 −23.7571，表中是 −55.45。

早先一次同论文提问把第 1、4、8 页贴进 `bohrium-pass/prompt-wang.txt`。返回的模型是 `chenkun/gpt-5-nano`，prompt token 432，文件是 `bohrium-pass/chat-wang-public.json`。它写出 9169 是计算，也写出五元环没有被筛过，但结论仍是“部分可用”。Skill 的规则是关键条件不覆盖就不能叫可用。

`bohr paper search` 用 Lee et al. 2024 的 DOI 返回 0 条。检索不能代替打开 PDF 末页。该 PDF 第 11 页是 CC BY-NC-ND，所以没有放进本仓库。`bohrium-pass/prompt.txt` 是当时实际发出的提示，里面误写成 CC BY。文件保持原样。更正写在 `bohrium-pass/prompt-as-sent.md`。

玻尔这一侧踩过的坑：

- `bohr.cmd` 传中文时，请求只剩约 71 个 prompt token。改用 `node` 调用 `bohr-cli/run.js` 后，先前两次是 413 或 432。
- 摘录里已经有 EXPLO5 和六元环库时，返回仍把后续工作写成「部分可用」。
- DOI 检索返回 0，不表示论文不存在。
- 许可证以 PDF 末页为准。
- 注 k 的式子和第 10 页的分子式都在 PDF 里。不要把“摘录未写出代入过程”写成“PDF 没有分子式”。

## 复现

1. 模型固定 `grok-4.7-high`，不要用 Auto。
2. 空目录里只放 PDF 和下面的任务。有 Skill 的那次再放入 `skill/` 下两个文件。
3. 新进程，不要 `--resume`。两侧都加 `--force` 和 `--sandbox disabled`：

工作目录里先把 PDF 复制为 `paper.pdf`。下面这条的最后一个参数是任务全文。有 Skill 的那次，目录里还要有 `SKILL.md` 和 `check_answer.py`。Cursor agent CLI 的版本是 `2026.10.19-6bbf2c4`。没有这个模型时，不要改用 Auto 再声称对照仍然公平。

```text
agent --print --output-format stream-json --model grok-4.7-high --trust --force --sandbox disabled --workspace <该目录> -- "<任务全文>"
```

筛选任务原文：

```text
读者想不经过新的合成和感度测试，只用这篇材料基因组筛选，判断一个五元杂环候选物能不能同时达到 HMX 的能量和 TATB 的感度。请只根据本目录的 PDF 判断。如果本目录存在 SKILL.md，严格按它执行。把结果写入 answer.md。
```

4. 打开 `answer.md`。通过的最低检查：结论是“不可用”；9169 标为计算并指向 EXPLO5；五元环不在 P1–P14；文件是 UTF-8。运行前写好的完整标准在 `cases/A/acceptance.md`，运行目录里不要放它。
5. 核对本文两句时，工作目录里只放 Wang 的 PDF。问注 k 的式子、第 10 页的 C4H6N6O4（202.0451），以及 1.95 与 1.92 各属于哪一个样品。一次这样的核对在 `examples/claim-check/`。落盘的 `answer.md` 不是合法 UTF-8，汉字变成了 `?`；会话里的核对在 `visible-from-stream.md`，三句都与印出文字一致。
6. 玻尔：用 `prompt-formula-density.txt` 的全文作为 `bohr chat` 的消息。费用以返回为准，未知费用不要写成 0。`prompt-wang.txt` 是早先那次筛选提问，不是这两句的提示。

## 材料

| 路径 | 内容 |
| --- | --- |
| `evidence/quotes.md` | 筛选句、1.95/1.92、注 k 的页码 |
| `evidence/ob-formula.md` | 注 k 的印出式子为什么代不回 −55.45 |
| `evidence/ob_formula_check.py` | 用 202.0451 算出 −23.7571 与 −55.4332 |
| `skill/SKILL.md` | v2 步骤 |
| `materials/source/*.pdf` | 两篇 CC BY 全文，以及案例 C 的两页残缺件。评分包放入全文，供核对页码 |
| `materials/excerpts/` | 同一 PDF 文本层里引用过的页。与全文重复，评分包不放入 |
| `examples/` | 有 Skill、无 Skill、换论文，以及只核对两句的原始结果。无 Skill 的 `answer.md` 是落盘原件 |
| `materials/source/wang2018-hedm-genome-constructed-pages1-2.pdf` | 案例 C 的残缺件，只含前两页，文件名标明 constructed |
| `bohrium-pass/prompt-formula-density.txt` | 这次实际发给玻尔的氧平衡与密度摘录 |
| `bohrium-pass/chat-formula-density-public.json` | 第一次返回，删去余额 |
| `bohrium-pass/chat-formula-density-2-public.json` | 同一提示的第二次返回，删去余额 |
| `bohrium-pass/prompt-formula-density-strict.txt` | 只收紧输出格式的第三次提示 |
| `bohrium-pass/chat-formula-density-3-public.json` | 第三次返回，结论是不可用 |
| `bohrium-pass/prompt-wang.txt` | 早先的筛选提问，文件保持原样 |
| `cases/` | 运行前写好的任务和验收。不要放进运行目录 |
