"""
--- Day 7: Camel Cards ---
https://adventofcode.com/2023/day/7
"""

from collections import Counter

import dataclasses


test_input1 = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

STRENGHTS = {
    symbol: rank for rank, symbol in enumerate("2 3 4 5 6 7 8 9 T J Q K A".split(" "))
}

UPDATED_STRENGHTS = {
    symbol: rank for rank, symbol in enumerate("J 2 3 4 5 6 7 8 9 T Q K A".split(" "))
}


@dataclasses.dataclass
class Hand:
    cards: str
    strenghts: list
    type: str
    bid: int


def _calculate_type(cards):
    counter_values = tuple(count for symbol, count in Counter(cards).most_common())
    categories = {
        counts: rank
        for rank, counts in enumerate(
            [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1), (3, 1, 1), (3, 2), (4, 1), (5,)]
        )
    }
    return categories[counter_values]


def _recalculate_type(cards):
    if set(cards) != {"J"}:
        tempcards = cards.replace("J", "")
    else:
        tempcards = cards
    most_common = Counter(tempcards).most_common(1)[0][0]
    cards_substituted = cards.replace("J", most_common)

    counter_values = tuple(
        count for symbol, count in Counter(cards_substituted).most_common()
    )

    categories = {
        counts: rank
        for rank, counts in enumerate(
            [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1), (3, 1, 1), (3, 2), (4, 1), (5,)]
        )
    }
    return categories[counter_values]


def parse_lines(input, strenghts_mapping=STRENGHTS):
    hands = []
    for line in input.splitlines():
        cards, bid = line.split(" ")
        _type = _calculate_type(cards)
        strenghts = [strenghts_mapping[card] for card in cards]
        hands.append(Hand(cards, strenghts, _type, int(bid)))
    return hands


def part1(hands):
    result = 0

    sorted_hands = sorted(hands, key=lambda x: (x.type, x.strenghts))

    for rank, hand in enumerate(sorted_hands, start=1):
        result += rank * hand.bid
    return result


def part2(hands):
    result = 0

    # special joker behaviour
    for hand in hands:
        hand.type = _recalculate_type(hand.cards)

    # rest is the same as part 1
    sorted_hands = sorted(hands, key=lambda x: (x.type, x.strenghts))

    for rank, hand in enumerate(sorted_hands, start=1):
        result += rank * hand.bid
    return result


with open("07/input.txt") as f:
    input = f.read()

test_hands = parse_lines(test_input1)
test_result1 = part1(test_hands)

assert (
    test_result1 == 6440
), f"Result for test input in part 1 should be 6440, not {test_result1}"
hands = parse_lines(input)
result1 = part1(hands)
print(result1)  # 251136060

test_hands = parse_lines(test_input1, UPDATED_STRENGHTS)
test_result2 = part2(test_hands)
assert (
    test_result2 == 5905
), f"Result for test input in part 2 should be 5905, not {test_result2}"
hands2 = parse_lines(input, UPDATED_STRENGHTS)
result2 = part2(hands2)
print(result2)  # not 249653873, 249240696 but 249400220
