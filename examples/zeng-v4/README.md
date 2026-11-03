# Zeng 2020：v4 有／无 Skill 对照

四次运行使用同一份 [任务](task.md)和 [PDF](../../materials/source/zeng2020-methane-nn-md.pdf)。[验收标准](acceptance.md)写于运行前，没有放入运行工作目录。

| 运行 | 结果 | 耗时 |
| --- | --- | ---: |
| [with-1](with-1/answer.md) | 核心判断正确；另给出理想气体压力估算 | 304.9 s |
| [without-1](without-1/answer.md) | 核心判断正确；另给出理想气体压力估算 | 433.9 s |
| [with-2](with-2/answer.md) | 核心判断正确；压力数值标为未说明 | 446.6 s |
| [without-2](without-2/answer.md) | 核心判断正确；另给出理想气体压力估算 | 384.5 s |

四次都给出了关键事实的页码，也都区分论文的高温、高密度 CH4/O2 轨迹与目标火焰。验收标准要求论文未给出的压力数值标为未说明；三份回答虽然把数值标成了估算，仍未完全满足这一条。两组的耗时快慢方向不同。

每个目录包含原始 `answer.md`、`meta.json` 及 `trace-summary.jsonl`。摘要从真实事件流保留初始化、任务和结束事件，删除了本机目录、会话标识及与已保存答案重复的结果正文；完整流保存在本地。四次使用相同输入、模型参数、工具权限和预算；有 Skill 的两次加载[存档的 method-fit-check-v4](skill-v4/SKILL.md)，无 Skill 的两次不加载它。
