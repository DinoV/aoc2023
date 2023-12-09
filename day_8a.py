# ./python -X jit -m compiler --static aoc/day_8a.py
from __future__ import annotations

import __static__

from __static__ import Array, box, cbool, CheckedDict, CheckedList, clen, crange, int64

from typing import Tuple


def repeat(x: str) -> None:
    while True:
        for value in x:
            yield value


def run(example: cbool) -> None:
    dirs: CheckedDict[str, Tuple[str, str]] = {}
    with open("aoc/data/8ex.txt" if example else "aoc/data/8.txt") as f:
        lines = f.readlines()
        instrs: str = lines[0].strip()
        for line in lines[2:]:
            line = line.strip()
            entry, nexts = line.split(" = ")
            l, r = nexts.lstrip("(").rstrip(")").split(", ")
            dirs[entry] = l, r

    inst_iter = iter(repeat(instrs))
    cur = "AAA"
    steps: int64 = 0
    while cur != "ZZZ":
        direction = next(inst_iter)
        if direction == "L":
            cur = dirs[cur][0]
        else:
            cur = dirs[cur][1]

        steps += 1

    print(box(steps))


run(False)
