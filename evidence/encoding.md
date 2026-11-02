# A-without 的 answer.md 是什么字节

`examples/A-without-1/answer.md` 和 `A-without-2/answer.md` 是当时落盘的文件，没有把会话里的中文抄回去。

两份都是合法 UTF-8。大约七成字节是 ASCII `?`（0x3F）。汉字没有留下来。破折号和弯引号仍在，因为它们属于 Windows-1252，存成 UTF-8 后是多字节。整文件不能再按 Windows-1252 解码。

成因对得上：把 `stream.jsonl` 里同一次工具调用的中文，用 Windows-1252 编码，无法表示的字换成 `?`，再存成 UTF-8。这样得到的字节和磁盘文件一致。把工具调用的 UTF-8 字节误当成 1252 来读，得到的是另一串乱码，不是这个文件。`stream.jsonl` 里没有这些问号字节。

本地校验：`python tools/test_answer_encoding.py`（工作副本里的 `runs-v1`）。
