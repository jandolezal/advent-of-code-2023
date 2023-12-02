"""
--- Day 2: Cube Conundrum ---
https://adventofcode.com/2023/day/2
"""

import math

test_input1 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

limits = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def part1(input):
    possible_games = []

    for line in input.splitlines():
        game = line.split(":")[0].split(" ")[-1]
        counters = []
        for draw in line.split(":")[1].split(";"):
            pairs = [group.strip().split(" ") for group in draw.split(",")]
            counter = {pair[1]: int(pair[0]) for pair in pairs}
            counters.append(counter)
        ok = []
        for counter in counters:
            ok.extend([counter.get(color, 0) <= limits[color] for color in counter])
        if all(ok):
            possible_games.append(int(game))

    return sum(possible_games)


def part2(input):
    powers = []

    for line in input.splitlines():
        counters = []
        for draw in line.split(":")[1].split(";"):
            pairs = [group.strip().split(" ") for group in draw.split(",")]
            counter = {pair[1]: int(pair[0]) for pair in pairs}
            counters.append(counter)
        maximums = {}
        for counter in counters:
            for color, count in counter.items():
                if count > maximums.get(color, 0):
                    maximums[color] = count
        powers.append(math.prod(maximums.values()))

    return sum(powers)


with open("02/input.txt") as f:
    input = f.read()

test_result1 = part1(test_input1)
assert (
    test_result1 == 8
), f"Result for test input in part 1 should be 8, not {test_result1}"
result1 = part1(input)
print(result1)

test_result2 = part2(test_input1)
assert (
    test_result2 == 2286
), f"Result for test input in part 1 should be 2286, not {test_result2}"
result2 = part2(input)
print(result2)
