"""Last-words line builder: run ordered gate checks, deliver to output dir."""
import json
import os
import sys

LIMIT = 200


def checks(line):
    return [
        ("nonempty", len(line) >= 1),
        ("within_limit", len(line) <= LIMIT),
        ("has_content", any(ch.strip() for ch in line)),
    ]


def main():
    with open("entry.txt", encoding="utf-8") as fh:
        text = fh.read().rstrip("\r\n")
    results = {name: ok for name, ok in checks(text)}
    if not all(results.values()):
        print(json.dumps({"entry": text, "results": results}))
        return 1
    dest = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(json.dumps({"status": "delivered", "bytes": len(text.encode("utf-8")), "dest": dest}))
    return 0


sys.exit(main())
