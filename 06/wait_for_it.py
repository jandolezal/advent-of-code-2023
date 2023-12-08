"""
--- Day 6: Wait For It ---
https://adventofcode.com/2023/day/6
"""

import math

test_input1 = """Time:      7  15   30
Distance:  9  40  200
"""


def prepare_data(input):
    data = []
    for line in input.splitlines():
        data.append(
            [int(num) for num in line.split(":")[-1].strip().split(" ") if num != ""]
        )
    return data


def prepare_data2(input):
    return [
        int("".join([char for char in line if char.isdigit()]))
        for line in input.splitlines()
    ]


def part1(data):
    num_ways = []

    for game_duration, record_distance in zip(data[0], data[1]):
        num_ways.append(
            sum(
                [
                    ((game_duration - charging) * charging) > record_distance
                    for charging in range(game_duration)
                ]
            )
        )

    return math.prod(num_ways)


def part2(data):
    game_duration = data[0]
    record_distance = data[1]

    num_ways = []

    for charging in range(game_duration):
        num_ways.append(((game_duration - charging) * charging) > record_distance)

    return sum(num_ways)


with open("06/input.txt") as f:
    input = f.read()

# part1
test_data1 = prepare_data(test_input1)
test_result1 = part1(test_data1)
assert test_result1 == 288, f"Test result in part 1 should be 288, not {test_result1}"

data1 = prepare_data(input)
result1 = part1(data1)
print(result1)  # 1731600


# part 2
test_data2 = prepare_data2(test_input1)
test_result2 = part2(test_data2)
assert (
    test_result2 == 71503
), f"Test result in part 2 should be 71503, not {test_result1}"

data2 = prepare_data2(input)
result2 = part2(data2)
print(result2)  # 40087680
