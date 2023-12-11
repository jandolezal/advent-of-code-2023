"""
--- Day 11: Cosmic Expansion ---
https://adventofcode.com/2023/day/11
"""

from itertools import combinations

test_input1 = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""


def prepare_data(input):
    expanded_ = []
    ok_cols = []  # columns with #

    # expand rows
    for line in input.splitlines():
        if "#" not in line:
            expanded_.extend([line, line])
        else:
            ok_cols.extend([i for i, char in enumerate(line) if char == "#"])
            expanded_.append(line)

    # expand cols
    expanded = []
    for line in expanded_:
        newline = []
        for j, char in enumerate(line):
            if j in ok_cols:
                newline.append(char)
            else:
                newline.extend([char, char])
        expanded.append(newline)

    # gather galaxies coordinates as id_: (i, j)
    galaxies = {}
    id_ = 1
    for i in range(len(expanded)):
        for j in range(len(expanded[0])):
            if expanded[i][j] == "#":
                galaxies[id_] = (i, j)
                id_ += 1
    return galaxies


def part1(data):
    galaxies = data
    pairs = list(combinations(data, 2))
    distances = []
    for f, s in pairs:
        distance = abs(galaxies[s][0] - galaxies[f][0]) + abs(
            galaxies[s][1] - galaxies[f][1]
        )  # manhattan distance
        distances.append(distance)

    return sum(distances)


with open("11/input.txt") as f:
    input = f.read()

# part 1
test_result1 = part1(prepare_data(test_input1))
assert test_result1 == 374, f"Test result in part 1 should be 374, not {test_result1}"
result1 = part1(prepare_data(input))
print(result1)  # not 9532259 -> expand also cols, 9769724
