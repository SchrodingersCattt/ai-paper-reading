# A-without 的 answer.md 是什么字节

`examples/A-without-1/answer.md` 和 `A-without-2/answer.md` 是当时落盘的文件，没有把会话里的中文抄回去。

两份都是合法 UTF-8。大约七成字节是 ASCII `?`（0x3F）。汉字没有留下来。破折号和引号仍是 UTF-8（例如 U+2013 的 `e2 80 93`）。整文件不能按 Windows-1252 解码，因为里面有 1252 未定义的字节。所以这不是「先按 CP1252 读、再存成 UTF-8」能解释的结果。

Cursor 的 `stream.jsonl` 里，同一次工具调用仍是完整中文，结论是不覆盖。可见文本的抽出件是 `visible-from-stream.md`。磁盘文件和会话文本是两份证据，不能互相覆盖。

本地校验：`python tools/test_answer_encoding.py`（在仓库父目录的工作副本里，针对 `runs-v1`）。
