"""
--- Day 10s: Pipe Maze ---
https://adventofcode.com/2023/day/10
"""

from collections import namedtuple

# just the loop
test_input1 = """.....
.S-7.
.|.|.
.L-J.
.....
"""

# loop with all the other pipes
test_input2 = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""

position = namedtuple("Position", ["pipe", "r", "c", "origin"])

options = {
    "S": ["up", "down", "right", "left"],
    "|": ["up", "down"],
    "-": ["left", "right"],
    "L": ["up", "right"],
    "J": ["up", "left"],
    "7": ["down", "left"],
    "F": ["down", "right"],
}

moves = {
    "up": ["7", "|", "F", "S"],
    "down": ["J", "|", "L", "S"],
    "right": ["-", "J", "7", "S"],
    "left": ["-", "F", "L", "S"],
}

offsets = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

opposites = {
    "up": "down",
    "down": "up",
    "right": "left",
    "left": "right",
}


def prepare_data(input):
    data = {}
    lines = input.splitlines()
    n_rows = len(lines)
    n_cols = len(lines[0])

    for r in range(n_rows):
        for c in range(n_cols):
            data[(r, c)] = lines[r][c]
    return data, n_rows, n_cols


def part1(data, n_rows, n_cols):
    start = [k for k, v in data.items() if v == "S"][0]  # starting coordinates

    current = position("S", start[0], start[1], None)

    positions = []

    steps = 0

    # walk the maze, count steps and stop when arriving back to start
    while True:
        for option in set(options[current.pipe]) - {current.origin}:
            new_c = max(min(current.c + offsets[option][1], n_cols), 0)
            new_r = max(min(current.r + offsets[option][0], n_rows), 0)
            if data[(new_r, new_c)] in moves[option]:
                current = position(
                    data[(new_r, new_c)], new_r, new_c, opposites[option]
                )
                positions.append(current)
                steps += 1
                break
        if current.pipe == "S":
            return positions, steps // 2


with open("10/input.txt") as f:
    input = f.read()

# part 1
test_data1, n_rows, n_cols = prepare_data(test_input1)
test_data2, n_rows, n_cols = prepare_data(test_input2)
_, test_result1 = part1(test_data1, n_rows, n_cols)
_, test_result2 = part1(test_data2, n_rows, n_cols)

assert (
    test_result1 == 4
), f"Test result in part 1 just loop should be 4, not {test_result1}"
assert test_result2 == 4, f"Test result in part 1 loop should be 4, not {test_result2}"

data1, n_rows, n_cols = prepare_data(input)
_, result1 = part1(data1, n_rows, n_cols)
print(result1)  # 7012
