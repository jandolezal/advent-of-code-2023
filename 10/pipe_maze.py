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


test_input3 = """OF----7F7F7F7F-7OOOO
O|F--7||||||||FJOOOO
O||OFJ||||||||L7OOOO
FJL7L7LJLJ||LJIL-7OO
L--JOL7IIILJS7F-7L7O
OOOOF-JIIF7FJ|L7L7L7
OOOOL7IF7||L7|IL7L7|
OOOOO|FJLJ|FJ|F7|OLJ
OOOOFJL-7O||O||||OOO
OOOOL---JOLJOLJLJOOO
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


# i am cheating with this one
# found the even-odd rule algorithm mentioned on reddit and used it as is
# https://www.reddit.com/r/adventofcode/comments/18evyu9/2023_day_10_solutions/
# takes approx. 20 seconds to run
# https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule
def is_point_in_path(x: int, y: int, poly: list[tuple[int, int]]) -> bool:
    """Determine if the point is on the path, corner, or boundary of the polygon

    Args:
      x -- The x coordinates of point.
      y -- The y coordinates of point.
      poly -- a list of tuples [(x, y), (x, y), ...]

    Returns:
      True if the point is in the path or is a corner or on the boundary"""
    num = len(poly)
    j = num - 1
    c = False
    for i in range(num):
        if (x == poly[i][0]) and (y == poly[i][1]):
            # point is a corner
            return True
        if (poly[i][1] > y) != (poly[j][1] > y):
            slope = (x - poly[i][0]) * (poly[j][1] - poly[i][1]) - (
                poly[j][0] - poly[i][0]
            ) * (y - poly[i][1])
            if slope == 0:
                # point is on boundary
                return True
            if (slope < 0) != (poly[j][1] < poly[i][1]):
                c = not c
        j = i
    return c


def part2(input, positions):
    lines = input.splitlines()
    positions = [(position.r, position.c) for position in positions]

    count = 0
    for i, line in enumerate(lines):
        for j, col in enumerate(line):
            if is_point_in_path(i, j, positions):
                count += 1

    return count - len(positions)


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


# part 2
test_data3, n_rows, n_cols = prepare_data(test_input3)
positions, _ = part1(test_data3, n_rows, n_cols)
test_result3 = part2(test_input3, positions)
assert test_result3 == 8, f"Test result should be 8, not {test_result3}"


data2, n_rows, n_cols = prepare_data(input)
positions, _ = part1(data2, n_rows, n_cols)
result2 = part2(input, positions)
print(result2)  # 395
