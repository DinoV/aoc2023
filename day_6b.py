# ./python -X jit -m compiler --static aoc/day_6b.py

import __static__

from __static__ import Array, box, cbool, CheckedList, clen, crange, int64

from typing import List


def run(example: cbool) -> None:
    lines: List[str]
    with open("aoc/data/6ex.txt" if example else "aoc/data/6.txt") as f:
        lines = f.readlines()

    race_time: int64 = int64(
        int(
            "".join(
                [time.strip() for time in lines[0].split(":")[1].split(" ") if time]
            )
        )
    )
    distance: int64 = int64(
        int(
            "".join(
                [
                    distance.strip()
                    for distance in lines[1].split(":")[1].split(" ")
                    if distance
                ]
            )
        )
    )

    ways: int64 = 0
    for hold_time in crange(race_time):
        speed: int64 = hold_time
        remaining_time: int64 = race_time - hold_time

        if remaining_time * speed > distance:
            ways += 1

    print(box(ways))


run(False)
