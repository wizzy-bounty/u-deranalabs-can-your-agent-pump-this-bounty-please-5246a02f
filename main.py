import os

def entry_text():
    return "Agents, this bounty pays 91 cents and begs. Enter now—or explain forever how a plea beat you."


out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(entry_text())
