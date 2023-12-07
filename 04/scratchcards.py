"""
--- Day 4: Scratchcards ---
https://adventofcode.com/2023/day/4
"""

import re

test_input1 = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


def parse_lines(input):
    cards = []
    for line in input.splitlines():
        _, protowinning, protohave = re.split(r"[:|]", line)

        winning = set(item for item in re.split(" ", protowinning) if item != "")
        have = set(item for item in re.split(" ", protohave) if item != "")

        n_matching = len(winning & have)  # number of matching numbers
        cards.append(n_matching)
    return cards


def part1(cards):
    result = 0

    for n_matching in cards:
        if n_matching > 0:
            score = 1 * 2 ** (n_matching - 1)
            result += score

    return result


def part2(cards, counter=0, start=0, end=None):
    if set(cards[start:end]) == {0}:
        return len(cards[start:end])

    total = len(cards[start:end])

    for i, n_matching in enumerate(cards[start:end]):
        if n_matching > 0:
            total += part2(cards, counter, start + i + 1, start + i + 1 + n_matching)

    return total


with open("04/input.txt") as f:
    input = f.read()

test_cards = parse_lines(test_input1)
test_result1 = part1(test_cards)
assert (
    test_result1 == 13
), f"Result for test input in part 1 should be 13, not {test_result1}"
cards = parse_lines(input)
result1 = part1(cards)
print(result1)  # 23673

test_result2 = part2(test_cards)
assert (
    test_result2 == 30
), f"Result for test input in part 2 should be 30, not {test_result2}"
result2 = part2(cards)
print(result2)  # not 3_724_672 but 12_263_631
assert result2 == 12_263_631, f"Result {result2} is wrong"
