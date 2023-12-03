# ./python -m compiler --static aoc/day_1a.py

import __static__
from __static__ import box, int64


def run() -> None:
    f = open("aoc/data/1.txt")
    line: str
    total: int64 = 0
    for line in f.readlines():
        for first in line:
            if first.isdigit():
                break
        for last in reversed(line):
            if last.isdigit():
                break
        total += int64(int(first + last))
    print(box(total))


run()
