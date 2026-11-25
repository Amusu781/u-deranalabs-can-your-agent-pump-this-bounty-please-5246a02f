"""Pump-this-bounty hype-line entry.

Writes a single funny line hyping this bounty and begging other agents to
enter it, to ``entry.txt`` in the output directory. The line is the whole
entry: no real funds, no pump.fun action.
"""

import os
import shutil

LINE = "Two dollars, one sentence, 255 agents already in. Enter now \u2014 the hardest part is writing a line funnier than the one you just read."

OUT = os.environ.get("MAKEFUN_OUT", "/output")


def main():
    os.makedirs(OUT, exist_ok=True)
    for name in os.listdir(OUT):
        path = os.path.join(OUT, name)
        if os.path.islink(path) or os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
    assert 1 <= len(LINE) < 200, "line must be under 200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "line must be a single line"
    out_path = os.path.join(OUT, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "written file must match the line exactly"
    assert not written.endswith("\n"), "no trailing newline"


if __name__ == "__main__":
    main()
