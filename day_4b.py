# ./python -X jit -m compiler --static aoc/day_4a.py

import __static__
from __static__ import box, cbool, crange, int64

from collections import deque
from dataclasses import dataclass

from typing import List


@dataclass
class Card:
    card_id: int64
    count: int64

    def __init__(self, card_id: int64, count: int64) -> None:
        self.card_id = card_id
        self.count = count

def run(example: cbool) -> None:
    with open("aoc/data/4ex.txt" if example else "aoc/data/4.txt") as f:
        lines = f.readlines()

    cards: List[Card] = []
    queue: deque[Card] = deque()
    card: Card

    for card_id, line in enumerate(lines):
        winners_list, havers_list = line.split(":")[1].split("|")
        winners = {int(winner) for winner in winners_list.strip().split(" ") if winner}
        havers = {int(haver) for haver in havers_list.strip().split(" ") if haver}

        card = Card(int64(card_id), int64(len(winners.intersection(havers))))
        queue.append(card)
        cards.append(card)

    card_count: int64 = 0
    while queue:
        card_count += 1

        card = queue.popleft()

        for new_card_cnt in crange(card.count):
            queue.append(cards[card.card_id + new_card_cnt + 1])

    print(box(card_count))


run(False)
