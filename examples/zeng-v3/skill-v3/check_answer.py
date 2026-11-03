"""Structure check only. It does not know the right scientific answer."""
import sys
from pathlib import Path

path = Path("answer.md")
try:
    text = path.read_text(encoding="utf-8")
except UnicodeDecodeError:
    sys.exit("answer.md is not UTF-8")
if "结论" not in text:
    sys.exit("missing 结论")
allowed = ("可用", "部分可用", "不可用", "材料不足停止")
# The conclusion heading's next non-empty line should be one of the four.
lines = [line.strip() for line in text.splitlines()]
verdict = ""
for i, line in enumerate(lines):
    if line.startswith("#") and "结论" in line:
        for nxt in lines[i + 1:]:
            if nxt:
                verdict = nxt
                break
        break
if verdict not in allowed and not any(verdict.startswith(word) for word in allowed):
    sys.exit("结论 must be one of: " + " / ".join(allowed))
stopped = "材料不足停止" in verdict
if not stopped and not any(tag in text for tag in ("实测", "计算", "未说明")):
    sys.exit("number sources need 实测, 计算, or 未说明")
print("ok")
