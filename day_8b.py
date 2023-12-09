# ./python -X jit -m compiler --static aoc/day_8b.py
from __future__ import annotations

import __static__

from __static__ import Array, box, cbool, CheckedDict, CheckedList, clen, crange, int64

from math import lcm

from typing import Tuple


def repeat(x: str) -> None:
    while True:
        for value in x:
            yield value


def divisors_of_num(n):
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            yield i
    yield n


def run(example: cbool) -> None:
    dirs: CheckedDict[str, Tuple[str, str]] = {}
    with open("aoc/data/8exb.txt" if example else "aoc/data/8.txt") as f:
        lines = f.readlines()
        instrs: str = lines[0].strip()
        for line in lines[2:]:
            line = line.strip()
            entry, nexts = line.split(" = ")
            l, r = nexts.lstrip("(").rstrip(")").split(", ")
            dirs[entry] = l, r

    curs = [cur for cur in dirs if cur.endswith("A")]

    steps_required = []
    for cur in curs:
        inst_iter = iter(repeat(instrs))
        steps: int64 = 0
        while not cur.endswith("Z"):
            direction = next(inst_iter)
            if direction == "L":
                cur = dirs[cur][0]
            else:
                cur = dirs[cur][1]

            steps += 1
        steps_required.append(box(steps))

    print(lcm(*steps_required))


run(False)
