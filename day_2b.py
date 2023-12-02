# ./python -m compiler --static aoc/day_2a.py

import __static__
from __static__ import box, cbool, int64


def run(example: cbool) -> None:
    f = open("aoc/data/2ex.txt" if example else "aoc/data/2.txt")
    total_power: int64 = 0
    for game_id, line in enumerate(f.readlines()):
        sets = line.split(":")[1].split(";")

        matches: cbool = True
        max_red: int64 = 0
        max_blue: int64 = 0
        max_green: int64 = 0
        for cur_set in sets:
            red: int64 = 0
            blue: int64 = 0
            green: int64 = 0

            for cubes in cur_set.split(","):
                count, color = cubes.strip().split(" ")
                if color == "red":
                    red = int64(int(count))
                    max_red = red if max_red < red else max_red
                elif color == "blue":
                    blue = int64(int(count))
                    max_blue = blue if max_blue < blue else max_blue
                elif color == "green":
                    green = int64(int(count))
                    max_green = green if max_green < green else max_green
        power: int64 = max_red * max_blue * max_green
        total_power += power

    print(box(total_power))


run(False)
