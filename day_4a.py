# ./python -m compiler --static aoc/day_4a.py

import __static__
from __static__ import box, cast, cbool, CheckedList, clen, crange, int64

from typing import Optional


def run(example: cbool) -> None:
    f = open("aoc/data/4ex.txt" if example else "aoc/data/4.txt")
    lines = f.readlines()
    score: int64
    for y, line in enumerate(lines):
        winners_list, havers_list = line.split(":")[1].split("|")
        winners = [int(winner) for winner in winners_list.strip().split(" ") if winner]
        havers = [int(haver) for haver in havers_list.strip().split(" ") if haver]

        count = len(set(winners).intersection(havers))
        if count:
            score += int64(pow(2, count - 1))

    print(box(score))


run(False)
