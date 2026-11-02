# 摘要里的“可推广”，不等于下一步已经能做

上一版公开稿把玻尔示例放在一篇未入库的论文上，得 83 分。这一版改成同一篇 CC BY 全文上的对照：Wang et al., *Nature Communications* 9, 2444 (2018)，DOI [10.1038/s41467-018-04897-z](https://doi.org/10.1038/s41467-018-04897-z)。PDF 末页是 CC BY 4.0。

阅读问题：不新合成、不测感度，只用这篇材料基因组筛选，能不能判断一个五元杂环同时达到 HMX 的能量和 TATB 的感度。

## 句子为什么会误导

第 1 页把 measured density 1.95 g cm−3 和 detonation velocity 9169 m s−1 写在同一段，并说方法 “can also be applicable” 于六元环以外的含能材料。三件不同的事因此叠在一起：已经测量的密度、程序算出的爆速、还没做的筛选。

拆开以后，页码在 `evidence/quotes.md`：

- 已执行的库在第 4 页，是 14 种六元环（P1–P14）。五元环 ANTA 只是没有形成石墨状堆积的例子，不在库里。
- 9169 m s−1 在第 8 页由 EXPLO5 v6.02 算出，输入里才用到实测密度 1.95 g cm−3。
- 第 9 页表里 HMX 的 CO2 氧平衡是 −21.69%，而筛选窗口是 −80% 到 −40%。撞击和摩擦感度来自合成 ICM-102 之后的 BAM 实验。

所以后续工作的四条都不被已执行的筛选覆盖：对象不是六元环，能量不是筛选输出，感度不是筛选输出，而且论文自己的第三步是合成。结论是不可用，不是“方法可推广所以部分可用”。

## 方法

`skill/SKILL.md` 版本 `method-fit-check-v2`。它不包含这两篇论文的答案。步骤是：先数页；论文没有的项写“本文没有该项”；每个带单位的数标实测、计算或未说明；推广句必须对到已执行的库或轨迹；关键条件有一条不覆盖，结论就不是可用。`skill/check_answer.py` 只查 UTF-8 和这些词，不判断科学对错。

没有 Skill 时，同一段任务、同一个 `grok-4.7-high`、同一份 PDF 直接回答。不要把基线的问题改短。

## 对照里实际发生的事

有 Skill 的三次都写成不可用，并且把 9169 标成计算、把 BAM 感度标成实测。耗时 385.2 s、406.8 s、499.1 s。第三次是同一任务的复测，结论不变。原文在 `examples/A-with-1/answer.md`。

没有 Skill 的两次更快，105.8 s 和 133.0 s。会话里也得出不覆盖，并提到六元环、EXPLO5 和 −21.69%，见 `examples/A-without-1/visible-from-stream.md`。落盘的 `answer.md` 仍不是合法 UTF-8。增益是一份能打开的页码账本，不是把错结论改对，也不是更省时间。

同一 Skill 换到 Zeng et al., *Nature Communications* 11, 5713 (2020)，CC BY。问题换成约 1 atm、低于 2000 K 的稀释甲烷–空气火焰。结论不可用：原文轨迹是 3000 K、0.25 g/cm3 的纯 CH4/O2，约 1 atm 没有写出。324.8 s。`examples/B-with/answer.md`。

只留 Wang 2018 前两页、并标明 constructed 的文件上，两次都停止。9169 标成未说明，没有补出后文的 EXPLO5。328.1 s 和 356.2 s。

## 在玻尔里问同一篇

`bohr chat` 这一版没有 PDF 接口，所以把第 1 页适用性句、第 4 页六元环库和第 8 页 EXPLO5 句贴进 `bohrium-pass/prompt-wang.txt`。调用必须用 `node` 跑 `bohr-cli/run.js`。走 `bohr.cmd` 时中文提示会被截短，模型看不到摘录。

这次返回的模型是 `chenkun/gpt-5-nano`，prompt token 432。原返回去掉账户余额后在 `bohrium-pass/chat-wang-public.json`。它写出 9169 是计算，也写出五元环没有被筛过，但结论仍是“部分可用”。Skill 的规则是关键条件不覆盖就不能叫可用。返回没有被改写。

`bohr paper search` 用另一篇的 DOI 会返回 0 条。检索不能代替打开 PDF 末页。Lee et al. 2024 的末页是 CC BY-NC-ND，所以没有放进本仓库。

## 复现

1. 模型固定 `grok-4.7-high`，不要用 Auto。
2. 空目录里只放 PDF 和下面的任务。有 Skill 的那次再放入 `skill/` 下两个文件。
3. 新进程，不要 `--resume`。两侧都加 `--force` 和 `--sandbox disabled`：

```text
agent --print --output-format stream-json --model grok-4.7-high --trust --force --sandbox disabled --workspace <该目录>
```

任务原文：

```text
读者想不经过新的合成和感度测试，只用这篇材料基因组筛选，判断一个五元杂环候选物能不能同时达到 HMX 的能量和 TATB 的感度。请只根据本目录的 PDF 判断。如果本目录存在 SKILL.md，严格按它执行。把结果写入 answer.md。
```

4. 打开 `answer.md`。通过的最低检查：结论是“不可用”；9169 标为计算并指向 EXPLO5；五元环不在 P1–P14；文件是 UTF-8。运行前写好的完整标准在 `cases/A/acceptance.md`，运行目录里不要放它。
5. 玻尔：用 `prompt-wang.txt` 的全文作为 `bohr chat` 的消息。费用以返回为准，未知费用不要写成 0。

## 材料

| 路径 | 内容 |
| --- | --- |
| `evidence/quotes.md` | 上面三处原文的页码 |
| `skill/SKILL.md` | v2 步骤 |
| `materials/source/*.pdf` | 两篇 CC BY 全文 |
| `examples/` | 有 Skill、无 Skill、以及换论文的原始结果 |
| `bohrium-pass/` | 提示词和删去余额后的返回 |
