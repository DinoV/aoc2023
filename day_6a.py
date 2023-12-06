# ./python -X jit -m compiler --static aoc/day_6a.py

import __static__

from __static__ import Array, box, cbool, CheckedList, clen, crange, int64

from typing import List


def run(example: cbool) -> None:
    lines: List[str]
    with open("aoc/data/6ex.txt" if example else "aoc/data/6.txt") as f:
        lines = f.readlines()

    times = [int(time.strip()) for time in lines[0].split(":")[1].split(" ") if time]
    distances = [
        int(distance.strip())
        for distance in lines[1].split(":")[1].split(" ")
        if distance
    ]

    ways_arr = Array[int64](len(times))

    for i in crange(clen(times)):
        race_time: int64 = int64(times[i])
        distance: int64 = int64(distances[i])

        ways: int64 = 0
        for hold_time in crange(race_time):
            speed: int64 = hold_time
            remaining_time: int64 = race_time - hold_time

            if remaining_time * speed > distance:
                ways += 1

        ways_arr[i] = ways

    tot: int64 = 1
    for way in ways_arr:
        tot *= way

    print(box(tot))


run(False)
