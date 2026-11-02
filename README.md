# 一篇开放获取论文，够不够支撑下一步

读者经常把摘要里的“可推广”当成自己的下一步已经能做。这里的阅读问题只有一个：给定一篇允许再分发的全文，和一个写明的后续工作，方法与条件覆盖不覆盖那一步。

例子来自含能材料。Wang et al., *Nature Communications* 9, 2444 (2018)，DOI [10.1038/s41467-018-04897-z](https://doi.org/10.1038/s41467-018-04897-z)，PDF 末页是 CC BY 4.0。后续工作被写成：不新合成、不测感度，只用文中的材料基因组筛选，判断一个五元杂环能不能同时达到 HMX 的能量和 TATB 的感度。

## 方法

难点不在摘要，而在三处容易滑过去的地方：筛选库的化学范围、数字是计算还是实测、以及结论句是不是已经做过的实验。

Skill `method-fit-check-v1` 把这三处写成固定步骤。文件在 `skill/SKILL.md`。它不包含这两篇论文的答案。

1. 先数页。结果或讨论不在文件里，就停止，不凭记忆补。
2. 方法、温度、密度、力场或筛选库，每条抄短句并写页码。
3. 标签只有三种：原文事实、推断、不能确定。
4. 把后续工作拆开。有一条关键条件不覆盖，结论就不是“可用”。

没有把 Skill 放进目录时，同一段任务、同一个模型、同一份 PDF 直接回答。这样对照的是步骤，不是把基线问得更含糊。

## 这次对照实际看到的

模型是 Cursor agent CLI 里的 `grok-4.7-high`。有 Skill 的三次都写成“不可用”，并把依据落在页上：已执行的库是 14 种六元环；9169 m s−1 是用实测密度 1.95 g cm−3 交给 EXPLO5 算出的爆速，不是打靶测到的；撞击和摩擦感度来自合成 ICM-102 之后的测试。三次耗时 420.5 s、372.3 s、486.8 s。原文见 `examples/A-with-1/answer.md`。

没有 Skill 的两次更快，164.6 s 和 151.2 s。模型在会话里也得出“不覆盖”，并提到六元环、EXPLO5 和合成后的测试，见 `examples/A-without-1/visible-from-stream.md`。它没有逐条页码。落盘的 `answer.md` 还是问号和非法 UTF-8 字节。可见中文只存在于会话日志。增益是可核对的页码和一份能打开的结果文件，不是把一个错误结论改成正确结论。多出来的时间要算进去。

第二篇用同一 Skill，不改版本。Zeng et al., *Nature Communications* 11, 5713 (2020)，CC BY 4.0。问题换成：约 1 atm、低于 2000 K、燃料用惰性气体稀释的甲烷–空气火焰，这篇势能能不能用来预测污染物路径。结果是“不可用”。生产轨迹是 3000 K、0.25 g/cm3 的 100 个 CH4 加 200 个 O2，作者把更接近实验的条件写成未来工作。285.0 s。`examples/B-with/answer.md`。

残缺件只保留 Wang 2018 的前两页，文件名写明 constructed。两次都停在“材料不足停止”，没有补出后文的 14 种六元环或 EXPLO5。224.3 s 和 293.4 s。

## 玻尔里同一类问题会漏什么

`bohr paper search` 用 DOI `10.1038/s41524-024-01407-2` 返回 0 条。用 “RDX molecular crystal” 返回的是别的 RDX 晶体论文，不是 Lee et al. 2024。DOI 检索不能代替打开 PDF。

`bohr chat` 的返回模型是 `chenkun/gpt-5-nano`。提示词在 `bohrium-pass/prompt.txt`，原返回去掉账户余额后在 `bohrium-pass/chat-public.json`。中文提示必须交给 `node` 运行 `bohr-cli/run.js`。走 `bohr.cmd` 时，请求只带了约 71 个 prompt token，模型根本没看到摘录。

摘录送达之后（413 个 prompt token），模型仍把 Smith–Bharadwaj 势是不是反应力场留成开放问题，因为摘录没有“非反应”三个字，并把热动力学写成部分可用。全文第 8 页写的是当前模型 non-reactive，且不适用于化学反应。玻尔的回答按原话保留，没有改成希望的结论。

Lee et al. 2024 的 PDF 第 11 页是 CC BY-NC-ND，不是期刊页面上容易默认的 CC BY。那篇因此没有放进本仓库。公开文件只保留末页写明 CC BY 4.0 的两篇 Nature Communications 全文。规则在 `materials/LICENSE.md`。

## 复现

1. 安装 Cursor agent CLI，模型固定为 `grok-4.7-high`。不要用 Auto。
2. 新建空目录，只放入一篇 PDF 和 `cases/A/task.md` 的正文。有 Skill 的那次再放入 `skill/SKILL.md`。
3. 运行新进程，不要 `--resume`：

```text
agent --print --output-format stream-json --model grok-4.7-high --trust --force --sandbox disabled --workspace <该目录>
```

两侧都加 `--force`，避免一边停在审批、另一边没有。
4. 对照 `cases/A/acceptance.md`。该文件在计分运行前写定，运行目录里没有它。
5. 玻尔一侧：`bohr chat` 读取 `bohrium-pass/prompt.txt`。费用以 CLI 返回为准；这里不把未知费用写成 0。

## 材料索引

| 路径 | 是什么 |
| --- | --- |
| `skill/SKILL.md` | 可复用步骤，版本 method-fit-check-v1 |
| `materials/source/wang2018-hedm-genome.pdf` | 案例 A 全文，CC BY |
| `materials/source/zeng2020-methane-nn-md.pdf` | 案例 B 全文，CC BY |
| `examples/A-with-1/answer.md` | 有 Skill 的一次原始结果 |
| `examples/A-without-1/visible-from-stream.md` | 无 Skill 的会话可见文本 |
| `cases/` | 运行前的任务和验收标准 |
| `bohrium-pass/` | 玻尔提示词和删去余额后的返回 |
