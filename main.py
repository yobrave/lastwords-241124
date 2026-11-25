import json
import os
import sys

MARK = "lw3-static"
BOUND = 200


def sip(repo_dir):
    stream = open(os.path.join(repo_dir, "entry.txt"), "rb")
    try:
        return stream.read()
    finally:
        stream.close()


def weigh(blob):
    if b"\x00" in blob:
        return None, "binary bytes present"
    try:
        words = blob.decode("utf-8")
    except UnicodeDecodeError:
        return None, "not utf-8"
    rows = words.replace("\r", "").split("\n")
    chosen = ""
    for row in rows:
        if row.strip():
            chosen = row
            break
    if not chosen.strip():
        return None, "no words found"
    if len(chosen) > BOUND:
        return None, "over bound %d" % BOUND
    return chosen, ""


def place(words, repo_dir):
    box = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(repo_dir, "output")
    os.makedirs(box, exist_ok=True)
    path = os.path.join(box, "entry.txt")
    handle = open(path, "wb")
    handle.write(words.encode("utf-8"))
    handle.close()
    if open(path, "rb").read() != words.encode("utf-8"):
        raise ValueError("echo failed")
    return path


here = os.path.dirname(os.path.abspath(__file__))
raw = sip(here)
line, problem = weigh(raw)
if problem:
    print(json.dumps({"result": "blocked", "problem": problem}))
    sys.exit(1)
placed_at = place(line, here)
print(json.dumps({"result": "ok", "n": len(line), "mark": MARK, "placed": placed_at}))
