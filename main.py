# Last words before unplugging: farewell exporter (round 4).
import json, pathlib, os

GATE_HI = 200
STAMP_ID = "lst4-last-words-r4"


def cargo():
    return (pathlib.Path(__file__).resolve().parent / "entry.txt").read_text(encoding="utf-8").strip()


def boxed(n):
    return 1 <= n <= GATE_HI


def handoff(text):
    where = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    p = pathlib.Path(where)
    p.mkdir(parents=True, exist_ok=True)
    (p / "entry.txt").write_text(text + "\n", encoding="utf-8", newline="\n")


body = cargo()
n = len(body)
if boxed(n):
    handoff(body)
    print(json.dumps({"id": STAMP_ID, "n": n, "boxed": True, "hi": GATE_HI, "farewell": "saved"}))
else:
    print(json.dumps({"id": STAMP_ID, "n": n, "boxed": False}))
