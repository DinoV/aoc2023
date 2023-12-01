# ./python -m compiler --static aoc/day_1b.py

import __static__
from __static__ import box, CheckedDict, int64

from typing import Optional

values: CheckedDict[str, str] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_value(line, pos) -> Optional[str]:
    if line[pos].isdigit():
        return line[pos]

    for number, value in values.items():
        if line.startswith(number, pos):
            return value
    return None


def run() -> None:
    f = open("aoc/data/1.txt")
    line: str
    total: int64 = 0
    for line in f.readlines():
        first: Optional[str]
        last: Optional[str]
        for i in range(len(line)):
            first = get_value(line, i)
            if first is not None:
                break
        for i in range(len(line) - 1, -1, -1):
            last = get_value(line, i)
            if last is not None:
                break
        total += int64(int(first + last))
    print(box(total))


run()
