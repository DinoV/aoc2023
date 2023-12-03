# ./python -m compiler --static aoc/day_3a.py

import __static__
from __static__ import box, cast, cbool, CheckedList, clen, crange, int64

from typing import Optional


def is_symbol(c: str) -> cbool:
    return cbool(not c.isdigit() and c != ".")


def run(example: cbool) -> None:
    f = open("aoc/data/3ex.txt" if example else "aoc/data/3.txt")
    lines = f.readlines()
    y_size = len(lines)
    x_size = len(lines[0].strip())
    d = [[None] * x_size for i in range(y_size)]
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            d[y][x] = char

    sum: int64 = 0
    for y_pos in crange(clen(d)):
        row: list[str] = d[y_pos]
        borders_symbol: cbool = False
        number: Optional[str] = None
        for x, char in enumerate(row):
            if char.isdigit():
                if number is None:
                    number = char
                else:
                    number += char
            else:
                if number is not None:
                    if borders_symbol:
                        sum += int64(int(number))
                borders_symbol = False
                number = None
                continue

            for y_adj in (-1, 0, 1):
                for x_adj in (-1, 0, 1):
                    y_loc = int64(y_adj) + y_pos
                    x_loc = int64(x_adj) + int64(x)
                    if x_loc == int64(x) and y_loc == y_pos:
                        continue

                    if (
                        x_loc >= 0
                        and x_loc < int64(x_size)
                        and y_loc >= 0
                        and y_loc < int64(y_size)
                    ):
                        if is_symbol(d[box(y_loc)][box(x_loc)]):
                            borders_symbol = True
        if number is not None:
            if borders_symbol:
                sum += int64(int(number))

    print(box(sum))


run(False)
