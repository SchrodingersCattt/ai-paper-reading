# 玻尔科学空间这次实际做了什么

时间：2026-11-02。身份用本机已经登录的 Bohr CLI 2.9.17，不在这里记录密钥。

## 能用的入口

`bohr chat` 调用的是 Bohrium GPT，这次返回的模型名是 `chenkun/gpt-5-nano`。第一次经 `bohr.cmd` 传递中文提示时，请求只带了约 71 个 prompt token，模型没有看到论文摘录。改用 `node` 直接调用 `bohr-cli/run.js` 后，prompt token 为 413，模型按摘录作答。原始返回在 `chat.json`。公开材料会去掉其中的账户余额字段。

`bohr paper search "10.1038/s41524-024-01407-2"` 和带 Strachan 的题名检索返回 0 条。`bohr paper search "RDX molecular crystal"` 返回了 3 篇其他 RDX 晶体论文，没有 Lee et al. 2024。DOI 检索不能代替打开 PDF。

## 同一次提问的返回

提示词全文在 `prompt.txt`。模型结论是“部分可用”，理由是摘录没有写明 Smith–Bharadwaj 势是不是反应力场，所以它不肯判断断键。冲击被它写成不覆盖。热动力学被它写成部分可用。

这和事后对照原文的差别在于：Methods 写的是经典原子势，讨论写的是结构与均方位移，全文没有反应坐标。不能因为摘录没出现“非反应”三个字，就把断键留成开放问题。这个差别写进 GitHub 的技术洞察，不把模型的措辞改成我们希望的答案。
