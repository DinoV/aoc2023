# ./python -m compiler --static aoc/day_3a.py

import __static__
from __static__ import box, cast, cbool, CheckedList, clen, crange, int64

from typing import Optional


def is_gear(c: str) -> cbool:
    return cbool(c == "*")


def run(example: cbool) -> None:
    f = open("aoc/data/3ex.txt" if example else "aoc/data/3.txt")
    lines = f.readlines()
    y_size = len(lines)
    x_size = len(lines[0].strip())
    d = [[None] * x_size for i in range(y_size)]
    gears_ref_count = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            d[y][x] = char
            if char == "*":
                gears_ref_count[y, x] = []

    for y_pos in crange(clen(d)):
        row: list[str] = d[y_pos]
        borders_gears = set()
        number: Optional[str] = None
        for x, char in enumerate(row):
            if char.isdigit():
                if number is None:
                    number = char
                else:
                    number += char
            else:
                if number is not None:
                    if borders_gears:
                        for gear_x, gear_y in borders_gears:
                            gears_ref_count[gear_y, gear_x].append(int(number))

                borders_gears = set()
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
                        if is_gear(d[box(y_loc)][box(x_loc)]):
                            borders_gears.add((box(x_loc), box(y_loc)))

        if number is not None:
            if borders_gears:
                for gear_x, gear_y in borders_gears:
                    gears_ref_count[gear_y, gear_x].append(int(number))

    sum: int64 = 0
    for borders in gears_ref_count.values():
        if len(borders) == 2:
            sum += int64(borders[0]) * int64(borders[1])

    print(box(sum))


run(False)
