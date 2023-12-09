# ./python -X jit -m compiler --static aoc/day_9a.py
from __future__ import annotations

import __static__

from __static__ import Array, box, cbool, CheckedDict, CheckedList, clen, crange, int64

from typing import List


def predict(histories: List[int]) -> int:
    new_hist: List[int] = []
    x = histories[0]
    nonzero: bool = False
    for i, y in enumerate(histories[1:]):
        delta = y - x
        if delta:
            nonzero = True
        new_hist.append(delta)
        x = y

    if nonzero:
        new_val = predict(new_hist)
        below = new_hist[-1] + new_val
        new_hist.append(below)
        return below
    else:
        return 0


def run(example: cbool) -> None:
    with open("aoc/data/9ex.txt" if example else "aoc/data/9.txt") as f:
        lines = f.readlines()

    histories = []
    for line in lines:
        histories.append([int(value) for value in line.strip().split(" ")])

    tot = 0
    for history in histories:
        new_val = predict(history)
        below = history[-1] + new_val
        tot += below

    print(tot)


run(False)
