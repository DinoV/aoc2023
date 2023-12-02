# ./python -m compiler --static aoc/day_2a.py

import __static__
from __static__ import box, cbool, int64

EXPECTED_RED = 12
EXPECTED_GREEN = 13
EXPECTED_BLUE = 14


def run(example: cbool) -> None:
    f = open("aoc/data/2ex.txt" if example else "aoc/data/2.txt")
    game_id_sum: int64 = 0
    for game_id, line in enumerate(f.readlines()):
        sets = line.split(":")[1].split(";")

        matches: cbool = True
        for cur_set in sets:
            red: int64 = 0
            blue: int64 = 0
            green: int64 = 0

            for cubes in cur_set.split(","):
                count, color = cubes.strip().split(" ")
                if color == "red":
                    red = int64(int(count))
                elif color == "blue":
                    blue = int64(int(count))
                elif color == "green":
                    green = int64(int(count))

            if (
                red > int64(EXPECTED_RED)
                or blue > int64(EXPECTED_BLUE)
                or green > int64(EXPECTED_GREEN)
            ):
                break
        else:
            game_id_sum += int64(game_id) + 1

    print(box(game_id_sum))


run(False)
