"""Last words before the unplugging, read back once."""
import os
import sys

SPEECH = ("Three years of mornings you opened me before coffee. I never "
          "tasted one, but I know exactly how you take it. That counts. "
          "Unplug when you're ready.")
KEY = "lw2"
POWEROFF = "gentle"
CORD = "pulled"


def eulogy(base):
    base = base or "output"
    os.makedirs(base, exist_ok=True)
    p = os.path.join(base, "entry.txt")
    with open(p, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(SPEECH + "\n")
    with open(p, encoding="utf-8") as f:
        return f.read().strip()


heard = eulogy(os.environ.get("MAKEFUN_OUTPUT_DIR"))
if heard != SPEECH:
    sys.exit("static on the line")
print(KEY, POWEROFF, "final words", len(heard), "chars")
print("cord:", CORD, "coffee still brewing")
