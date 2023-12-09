"""
--- Day 9: Mirage Maintenance ---
https://adventofcode.com/2023/day/9
"""

from itertools import accumulate

test_input1 = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""


def prepare_data(input):
    return [[int(num) for num in line.split(" ")] for line in input.splitlines()]


def _calculate_increment(row):
    diffs = []

    while True:
        if set(row) == {0}:
            return list(accumulate(diffs))[-1]
        else:
            row = [second - first for first, second in zip(row, row[1:])]

        diffs.append(row[-1])


def part1(data):
    predicted = []
    for row in data:
        predicted.append(row[-1] + _calculate_increment(row))

    return sum(predicted)


with open("09/input.txt") as f:
    input = f.read()

# part 1
test_data1 = prepare_data(test_input1)
test_result1 = part1(test_data1)
assert test_result1 == 114, f"Test result in part 1 should be 114, not {test_result1}"

data1 = prepare_data(input)
result1 = part1(data1)
print(result1)  # 1930746032


# part 2
test_data2 = [row[::-1] for row in test_data1]
test_result2 = part1(test_data2)
assert test_result2 == 2, f"Test result in part 2 should be 2, not {test_result2}"

data2 = [row[::-1] for row in data1]
result2 = part1(data2)
print(result2)  # 1154
