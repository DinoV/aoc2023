# ./python -X jit -m compiler --static aoc/day_5a.py

import __static__

from __static__ import Array, box, cbool, CheckedList, clen, crange, int64

from typing import List


class Range:
    def __init__(self, dest_start: int64, source_start: int64, length: int64):
        self.dest_start: int64 = dest_start
        self.source_start: int64 = source_start
        self.length: int64 = length

    def __repr__(self) -> str:
        return f"Range({box(self.dest_start)}, {box(self.source_start)}, {box(self.length)})"


def parse_ranges(lines: List[str], start: int64, dest: CheckedList[Range]) -> int64:
    while start < clen(lines):
        if not lines[start].strip():
            break
        dest_start, source_start, length = lines[start].strip().split(" ")
        dest.append(
            Range(int64(int(dest_start)), int64(int(source_start)), int64(int(length)))
        )
        start += 1
    return start


def run(example: cbool) -> None:
    lines: List[str]
    with open("aoc/data/5ex.txt" if example else "aoc/data/5.txt") as f:
        lines = f.readlines()

    seeds: Array[int64]
    seed_to_soil: CheckedList[Range] = []
    soil_to_fertilizer: CheckedList[Range] = []
    fertilizer_to_water: CheckedList[Range] = []
    water_to_light: CheckedList[Range] = []
    light_to_temperature: CheckedList[Range] = []
    temperature_to_humidity: CheckedList[Range] = []
    humidity_to_location: CheckedList[Range] = []
    path: CheckedList[CheckedList[Range]] = [
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location,
    ]

    i: int64 = 0
    while i < clen(lines):
        line = lines[i]
        if line.startswith("seeds:"):
            seed_items = [
                int(seed) for seed in lines[0].split(":")[1].strip().split(" ")
            ]
            seeds = Array[int64](len(seed_items))
            for cur_seed in crange(clen(seed_items)):
                seeds[cur_seed] = int64(seed_items[cur_seed])
            i += 1
        elif line.startswith("seed-to-soil map:"):
            i = parse_ranges(lines, i + 1, seed_to_soil)
        elif line.startswith("soil-to-fertilizer map:"):
            i = parse_ranges(lines, i + 1, soil_to_fertilizer)
        elif line.startswith("fertilizer-to-water map:"):
            i = parse_ranges(lines, i + 1, fertilizer_to_water)
        elif line.startswith("water-to-light map:"):
            i = parse_ranges(lines, i + 1, water_to_light)
        elif line.startswith("light-to-temperature map:"):
            i = parse_ranges(lines, i + 1, light_to_temperature)
        elif line.startswith("temperature-to-humidity map:"):
            i = parse_ranges(lines, i + 1, temperature_to_humidity)
        elif line.startswith("humidity-to-location map:"):
            i = parse_ranges(lines, i + 1, humidity_to_location)
        else:
            i += 1

    min_seed: int64 = 0x7FFFFFFFFFFFFFFF
    for seed in seeds:
        s = 0
        for step in path:
            for elm in step:
                if seed >= elm.source_start and seed < elm.source_start + elm.length:
                    seed += elm.dest_start - elm.source_start
                    break
            s += 1

        if seed < min_seed:
            min_seed = seed

    print(box(min_seed))


run(True)
