# ./python -X jit -m compiler --static aoc/day_5b.py

from __future__ import annotations

import __static__

from __static__ import Array, box, cbool, CheckedList, clen, crange, int64

from bisect import bisect_left
from typing import List


class Range:
    def __init__(
        self, dest_start: int64, source_start: int64, length: int64, history=None
    ):
        self.dest_start: int64 = dest_start
        self.source_start: int64 = source_start
        self.length: int64 = length
        self.history = history or []

    def __repr__(self) -> str:
        return f"Range(dest_start={box(self.dest_start)}, source_start={box(self.source_start)}, {box(self.length)})"

    def __eq__(self, other: Range) -> bool:
        return box(self.source_start == other.source_start)

    def __lt__(self, other: Range) -> bool:
        return box(self.source_start < other.source_start)

    def __gt__(self, other: Range) -> bool:
        return box(self.source_start > other.source_start)


def parse_ranges(lines: List[str], start: int64, dest: CheckedList[Range]) -> int64:
    while start < clen(lines):
        if not lines[start].strip():
            break
        dest_start, source_start, length = lines[start].strip().split(" ")
        dest.append(
            Range(
                int64(int(dest_start)),
                int64(int(source_start)),
                int64(int(length)),
                ["og"],
            )
        )
        start += 1
    return start


def run(example: cbool) -> None:
    lines: List[str]
    with open("aoc/data/5ex.txt" if example else "aoc/data/5.txt") as f:
        lines = f.readlines()

    seeds: Array[int64]
    seeds_lens: Array[int64]

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
            seeds = Array[int64](len(seed_items) // 2)
            seeds_lens = Array[int64](len(seed_items) // 2)
            for cur_seed in crange(clen(seed_items) // 2):
                seeds[cur_seed] = int64(seed_items[cur_seed * 2])
                seeds_lens[cur_seed] = int64(seed_items[cur_seed * 2 + 1])
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

    i = 1
    src_ranges = path[0]
    while i < clen(path):
        dest_ranges = path[i]
        new_ranges = CheckedList[Range]()

        for src in src_ranges:
            for dest in dest_ranges:
                src_start: int64 = src.dest_start
                src_end: int64 = src.dest_start + src.length

                dest_start: int64 = dest.source_start
                dest_end: int64 = dest.source_start + dest.length

                ovr_start: int64 = src_start if src_start > dest_start else dest_start
                ovr_end: int64 = src_end if src_end < dest_end else dest_end
                ovr_len: int64 = ovr_end - ovr_start

                if ovr_len <= 0:
                    continue

                new_src_start: int64 = src.source_start + ovr_start - src_start
                new_dest_start: int64 = dest.dest_start + ovr_start - dest_start

                new = Range(new_dest_start, new_src_start, ovr_end - ovr_start)
                new.history.append(
                    Range(src.dest_start, src.source_start, src.length, src.history)
                )
                new.history.append(
                    Range(dest.dest_start, dest.source_start, dest.length, dest.history)
                )

                # Include any of the remaining mapping, it's still relevant
                if ovr_start == src_start:
                    # trim from end
                    src.history.append(
                        Range(src.dest_start, src.source_start, src.length)
                    )
                    src.length -= ovr_len
                    src.source_start += ovr_len
                    src.dest_start += ovr_len
                elif ovr_end == src_end:
                    # trim from start
                    src.length -= ovr_len
                else:
                    # trim from middle
                    start_remaining: int64 = new_src_start - src.source_start
                    src_ranges.append(
                        Range(src.dest_start, src.source_start, start_remaining)
                    )
                    src.source_start += start_remaining + ovr_len
                    src.dest_start += start_remaining + ovr_len
                    src.length -= ovr_len + start_remaining

                if ovr_start == dest_start:
                    dest.source_start += ovr_len
                    dest.dest_start += ovr_len
                    dest.length -= ovr_len
                elif ovr_end == dest_end:
                    dest.length -= ovr_len
                else:
                    start_remaining = new_dest_start - dest.dest_start
                    dest_ranges.append(
                        Range(dest.dest_start, dest.source_start, start_remaining)
                    )
                    dest.source_start += start_remaining + ovr_len
                    dest.dest_start += start_remaining + ovr_len
                    dest.length -= ovr_len + start_remaining

                new_ranges.append(new)

        for src in src_ranges:
            if src.length != 0:
                new_ranges.append(src)
        for dest in dest_ranges:
            if dest.length != 0:
                new_ranges.append(dest)
        src_ranges = new_ranges
        i += 1

    min_seed: int64 = 0x7FFFFFFFFFFFFFFF
    i = 0
    src_ranges.sort()
    while i < clen(seeds):
        elm: Range | None = None
        seed_iter: int64 = seeds[i]
        while seed_iter < seeds[i] + seeds_lens[i]:
            seed: int64 = seed_iter

            if elm is None:
                idx = bisect_left(src_ranges, Range(0, seed, 0))
                elm = src_ranges[idx]
                if elm.source_start > seed:
                    elm = src_ranges[idx - 1]

            if not (seed >= elm.source_start and seed < elm.source_start + elm.length):
                idx = bisect_left(src_ranges, Range(0, seed, 0))
                elm = src_ranges[idx]
                if elm.source_start > seed:
                    elm = src_ranges[idx - 1]
                assert (
                    elm.source_start + elm.length <= src_ranges[idx + 1].source_start
                ), f"{elm} {src_ranges[idx + 1]}"

            if seed >= elm.source_start and seed < elm.source_start + elm.length:
                seed += elm.dest_start - elm.source_start
            else:
                seed_iter = elm.source_start + elm.length

            if seed < min_seed:
                min_seed = seed

            seed_iter += 1

        i += 1

    print(box(min_seed))


run(False)
