# Zeng 2020：方法适用性对照

[任务](task.md)询问论文的方法能否用于约 1 atm、低于 2000 K 的稀释甲烷—空气火焰；[验收标准](acceptance.md)列出需要核对的原文条件。输入是仓库内的 [Zeng 2020 PDF](../../materials/source/zeng2020-methane-nn-md.pdf)。

| 目录 | 设置 | 耗时 | 主要结果 |
| --- | --- | ---: | --- |
| [with](with/) | 加载 [method-fit-check-v3](skill-v3/SKILL.md) | 375.5 s | 不覆盖；逐项给出页码和模拟条件 |
| [without-1](without-1/) | 不加载 Skill | 133.2 s | 不覆盖；列出模拟条件并自行估算压力 |
| [without-2](without-2/) | 不加载 Skill | 104.8 s | 不覆盖；给出关键条件，但未写轨迹时长与步长 |

每个目录保留原始 `answer.md`、运行 `meta.json`，以及从真实原始流中选出的初始化、用户任务和结束事件 `trace-summary.jsonl`。摘要删除了本机工作目录与会话标识；它不是完整运行日志。三次均以 `grok-4.7-high` 参数启动，Cursor agent CLI 版本为 2026.10.19-6bbf2c4。一次无 Skill 运行的界面初始化名称显示为 `Grok 4.7 High`，另两次显示为 `Grok 4.7 256K High`；具体模型权重版本未提供。

三次运行的覆盖结论一致；该表用于比较页码和条件记录，也保留耗时差异。这些是 2026-11-02 的 v3 运行，和仓库当前 v4 Skill 分开记录。
