此记录来自单独的 Cursor/Grok 会话：将提交 62748（commit `14c0d79399e33703a5315c5aa12c3a404082b00a`）的材料包解压到新目录，依赖使用本机已安装的版本和配置的 PYTHONPATH。进程中断后恢复了同一会话；两次初始化显示名分别为 `Grok 4.7 High` 和 `Grok 4.7 256K High`，请求的模型 ID 均为 `grok-4.7-high`。本机用户名和绝对路径已脱敏。

# 离线复现检查

检查范围是当前解压目录中的 `README.md` 与 `docs/reproduction.md`。输出只写在 `audit-test/`。论文、脚本、图、任务和已保存回答都没有改。

这次实际跑完的本地步骤没有发现缺文件、断掉的相对链接、图结构不符、提问哈希不符，或压力估算与论文第 2 页及无 Skill 回答冲突。下面的退出码 1 来自检查程序自己的参数传递，重跑后已通过；它们不是教程命令的失败。

指定解释器：`<workspace>\_tmp\cq1-py311\Scripts\python.exe`。图提取、提问重建、`check_fig5.py`、四次 `--dry-run` 和压力脚本都用它。教程里的 `./figure-run` 改写到 `audit-test/figure-run`，`check_fig5.py` 的新目录用 `audit-test/fig5-check`，避免在作品目录里另建输出。

## 实际执行的命令

| 命令 | 退出码 | 结果 |
| --- | --- | --- |
| 指定解释器 `--version` | 0 | Python 3.11.14 |
| `audit-test/probe_fitz.py`（指定解释器） | 0 | PyMuPDF 1.26.7 |
| `audit-test/probe_fitz.py`（PATH 上的 Python 3.12.8） | 0 | PyMuPDF 1.26.7 |
| `audit-test/check_links.py` | 0 | `README.md` 与 `docs/reproduction.md` 的 110 个相对链接都在；缺 0 个。唯一外链是 DOI，按离线要求没有打开 |
| `bohrium-pass/extract_fig5_graph.py --pdf materials/source/zeng2020-methane-nn-md.pdf --out audit-test/figure-run` | 0 | 9 个节点、9 条箭头；YES 为 N8→N7，NO 为 N8→N9 |
| `bohrium-pass/build_figure_question.py --mode baseline --out audit-test/figure-run/baseline.txt` | 0 | 写出 baseline 提问 |
| `bohrium-pass/build_vector_prompt.py --baseline audit-test/figure-run/baseline.txt --graph audit-test/figure-run/graph.json --out audit-test/figure-run` | 0 | `prompt_sha256: 1c2d5d9bb22955eff561a02e9ad976b9092ed5165feff990fdc4ec34c0ad94cc` |
| `bohrium-pass/check_fig5.py --out audit-test/fig5-check` | 0 | 与 `bohrium-pass/zeng-figure-vector-protocol.md` 的九个节点、九条边及 YES/NO 一致 |
| `examples/zeng-v5/reproduce_a.py --with-skill --out audit-test/paper-with --dry-run` | 0 | 见下方哈希；`--out` 目录没有创建 |
| `examples/zeng-v5/reproduce_a.py --out audit-test/paper-without --dry-run` | 0 | 同上，`skill_sha256` 为 null |
| `examples/zeng-v5/reproduce_a.py --compact --with-skill --out audit-test/paper-compact-with --dry-run` | 0 | 简洁任务哈希与有 Skill 一侧相同 |
| `examples/zeng-v5/reproduce_a.py --compact --out audit-test/paper-compact-without --dry-run` | 0 | 简洁任务哈希相同，`skill_sha256` 为 null |
| `bohrium-pass/estimate_initial_ideal_pressure.py` | 0 | M = 26.6793333333 g/mol；P = 2306.75741523 atm |
| `audit-test/extract_page2.py` | 0 | 抽出 PDF 第 2 页文本，共 9 页 |
| `audit-test/compare_outputs.py`（修正 f-string 后） | 0 | 生成文件与随包哈希一致 |
| `C:\Program Files\nodejs\node.exe --version` | 0 | v24.11.1 |
| `C:\Program Files\nodejs\npm.cmd --version` | 0 | 11.6.2 |
| `npm.cmd ls -g @dptech-corp/bohr-cli --depth=0 --offline` | 0 | `@dptech-corp/bohr-cli@2.9.21` |

标准输出和标准错误在 `audit-test/*.stdout` 与 `audit-test/*.stderr`。第一次完整命令记录在 `audit-test/run-log.txt`。

检查器第一次调用指定解释器和 Python 3.12 的 `-c "import fitz..."` 时，参数被拆开，两边都是退出码 1，报 `SyntaxError: import`。这不表示缺少 PyMuPDF；随后的 `probe_fitz.py` 以及成功的图提取都显示 1.26.7。`Start-Process` 直接启动 `npm.ps1` 时也失败（不是有效的 Win32 程序）。改用 `npm.cmd` 后退出码 0。

## 图、提问和验收

抽出的节点是：Molecular system；Sampling with ReaxFF；Redundancy removal (Coulomb matrixes and Mini Batch Kmeans)；QM calculation；NN training；Re-sampling (with NN-based short MDs)；Dataset；New data?；Final dataset。

箭头是 N1→N2、N2→N3、N3→N7、N7→N4、N4→N5、N5→N6、N6→N8、N8→N7（YES）、N8→N9（NO）。`check_fig5.py` 把它们对应到协议中的短名：Redundancy removal → Dataset，Dataset → QM calculation，New data? → Dataset [YES]，New data? → Final dataset [NO]。

| 文件 | sha256 | 与记录一致 |
| --- | --- | --- |
| `audit-test/figure-run/baseline.txt` | `6395d624a8a8bd70ae0ef7bbc45ef27d6c8e6b0cfa2c3b58d6fff8b95c708281` | 是，`zeng-figure-comparison-metadata.json` 的 baseline |
| `audit-test/figure-run/vector-prompt.txt` | `1c2d5d9bb22955eff561a02e9ad976b9092ed5165feff990fdc4ec34c0ad94cc` | 是，`zeng-figure-vector-metadata.json` |
| `audit-test/figure-run/graph.json` | `e35432e2076ecd4320ae5edc622b5c841f7da014fd587fcfd2844ee65a3c6ff3` | 是，与随包 `zeng-figure-vector-graph.json` 及 `fig5-check/graph.json` 字节相同 |
| `audit-test/figure-run/vector-supplement.txt` | 与 `bohrium-pass/zeng-figure-vector-supplement.txt` 字节相同（706 字节） | 是 |

PDF、原任务、简洁任务、Skill、验收标准和协议的哈希也分别等于 `47987f62…384e`、`a9b01043…fc91`、`99b7ab4c…82b1`、`54e99ece…c44d`、`54bdd272…7ec2`、`e3064880…5091`。

## Skill 预检

四次都保留了 `--dry-run`，没有启动模型。两次原任务的 `pdf_sha256` 与 `task_sha256` 相同；两次 `--compact` 的论文哈希相同，任务哈希同为 `99b7ab4c78557f18a2353ddd9c1d734e9f846df96332ba5540bc451b524382b1`。只有 `--with-skill` 的两次带 `skill_sha256` `54e99ecebb8c8c51f3c688cbd1fec4ddfaca5dd3225dd02e498bab8689d6c44d`。模型字段是 `grok-4.7-high`，程序字段是 `Cursor agent CLI 2026.10.19-6bbf2c4`，`agent_available` 为 true。这些值与 `docs/reproduction.md` 以及 `examples/zeng-v5/A-with-1`、`A-with-2`、`A-without-1`、`A-without-2`、`A-compact-with`、`A-compact-without` 的 `meta.json` 一致。四个 `--out` 目录都没有生成。

## 压力估算

脚本输入是 n(CH₄)=100、n(O₂)=200、M(CH₄)=16.042 g/mol、M(O₂)=31.998 g/mol、ρ=0.25 g/cm³、T=3000 K、R=82.057 cm³·atm/(mol·K)。分子数、密度和温度能在 PDF 第 2 页对上：100 个 CH₄、200 个 O₂、共 900 个原子、密度 0.25 g/cm³、NVT、步长 0.1 fs、Berendsen 恒温器、3000 K。同一页写 “relatively high density (and thus high pressure)”，没有给出 atm 数值。全文检索 “atm” 时，唯一命中是第 6 页 “treatment” 里的字母序列，不是压力单位。

单位可以消掉：g/cm³ × cm³·atm/(mol·K) × K / (g/mol) = atm。计算结果是平均摩尔质量 26.6793333333 g/mol，记到 0.01 g/mol 为 26.68 g/mol；P = 2306.75741523 atm，三位有效数字为 2.31 × 10³ atm。`examples/zeng-v5/A-without-1/answer.md` 写 M = 26.68 g/mol、R = 82.057 cm³·atm/(K·mol)、P ≈ 2.31 × 10³ atm。摩尔和开尔文在分母中的写法不同，量纲相同。README 中的 26.679 g/mol 和约 2,307 atm 是同一结果的舍入。脚本最后一行写明这是所列假设下的估算，不是论文报告的轨迹实际压力；该计算用的是尚未反应的初始分子数，论文第 2 页也没有把这个 atm 数写成轨迹压力。

## 解释器、Node 和 Bohr CLI

指定的 Python 3.11.14 和 PATH 上的 Python 3.12.8 都存在，并且都有 PyMuPDF 1.26.7。`where node` 的第一项是 Cursor agent 自带的 `<local-path>\AppData\Local\cursor-agent\versions\2026.10.19-6bbf2c4\node.exe`，版本 v24.5.0。教程所记的 Node.js v24.11.1 在 `C:\Program Files\nodejs\node.exe`，这次已核对版本。已执行的检查没有用 `node` 调用玻尔。

`bohr.cmd` 与 `bohr.ps1` 在 `<local-path>\AppData\Roaming\npm\`。离线的 `npm ls -g --offline` 显示已安装 `@dptech-corp/bohr-cli@2.9.21`。没有执行 `bohr`，因此没有登录，也没有发请求。

## 按要求没有做的联网和模型步骤

以下命令没有运行：`python -m pip install PyMuPDF==1.26.7`，`npm install -g @dptech-corp/bohr-cli@2.9.21`，`bohr auth login`，`node … chat … --model gpt-5-nano`，`parse_zeng.py submit/poll`，以及去掉 `--dry-run` 的 `reproduce_a.py`。当前环境里 PyMuPDF 1.26.7 和 Bohr CLI 2.9.21 已经存在，所以这次离线检查没有安装它们。`docs/reproduction.md` 里的六页空白 PDF 测试和 `--mode guarded` 不在本次列出的检查中，也没有跑。已保存的玻尔问答和 Skill 正式回答只用来对照哈希与压力数字，没有重新生成。
