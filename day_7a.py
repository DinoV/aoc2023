# ./python -X jit -m compiler --static aoc/day_7a.py
from __future__ import annotations

import __static__

from __static__ import Array, box, cbool, CheckedDict, CheckedList, clen, crange, int64

from enum import IntEnum

from typing import List


class HandType(IntEnum):
    FiveOfAKind = 0
    FourOfAKind = 1
    FullHouse = 2
    ThreeOfAKind = 3
    TwoPair = 4
    OnePair = 5
    HighCard = 6


STRENGTHS: CheckedDict[str, int] = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


class Hand:
    def __init__(self, cards: str, bid: int64):
        d: CheckedDict[int, int] = {}
        self.cards: CheckedList[int] = []
        self.bid: int64 = bid
        for card in cards:
            s = STRENGTHS[card]
            self.cards.append(s)
            if s in d:
                d[s] += 1
            else:
                d[s] = 1

        hand_type = HandType.HighCard
        for s, cnt in d.items():
            if cnt == 5:
                hand_type = HandType.FiveOfAKind
                break
            elif cnt == 4:
                hand_type = HandType.FourOfAKind
                break
            elif cnt == 3:
                if hand_type == HandType.OnePair:
                    hand_type = HandType.FullHouse
                    break
                else:
                    hand_type = HandType.ThreeOfAKind
            elif cnt == 2:
                if hand_type == HandType.ThreeOfAKind:
                    hand_type = HandType.FullHouse
                    break
                elif hand_type == HandType.OnePair:
                    hand_type = HandType.TwoPair
                    break
                else:
                    hand_type = HandType.OnePair

        self.card_str = cards
        self.hand_type = hand_type

    def __gt__(self, other: Hand):
        if self.hand_type < other.hand_type:
            return True
        elif self.hand_type > other.hand_type:
            return False
        for l, r in zip(self.cards, other.cards):
            if l > r:
                return True
            elif l < r:
                return False

    def __lt__(self, other: Hand):
        return other.__gt__(self)

    def __repr__(self):
        return f"{self.card_str}: {self.hand_type} {box(self.bid)} {self.hand_type}"


def run(example: cbool) -> None:
    lines: List[str]
    hands: CheckedList[Hand] = []
    with open("aoc/data/7ex.txt" if example else "aoc/data/7.txt") as f:
        lines = f.readlines()

        for line in lines:
            cards, bid = line.split(" ")
            hands.append(Hand(cards, int64(int(bid))))

    hands.sort()
    hand: Hand
    tot: int64 = 0
    for i, hand in enumerate(hands):
        tot += hand.bid * (int64(i) + 1)
        print(hand)

    print(box(tot))


run(False)
