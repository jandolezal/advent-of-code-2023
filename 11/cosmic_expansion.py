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
    lines = input.splitlines()

    # check rows and cols to expand
    ok_cols = []
    ok_rows = []
    for i, line in enumerate(input.splitlines()):
        if "#" in line:
            ok_rows.append(i)
            ok_cols.extend([j for j, char in enumerate(line) if char == "#"])
    exp_rows = list(set(range(len(lines))) - set(ok_rows))
    exp_cols = list(set(range(len(lines[0]))) - set(ok_cols))

    # gather galaxies coordinates as id_: (i, j)
    galaxies = {}
    id_ = 1
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "#":
                galaxies[id_] = (i, j)
                id_ += 1

    return galaxies, exp_rows, exp_cols


def part1(data, exp_rows, exp_cols, multiplier=2):
    galaxies = data
    pairs = list(combinations(data, 2))
    distances = []

    for f, s in pairs:
        expandable_rows = sum(
            [
                galaxies[f][0] < row < galaxies[s][0]
                or galaxies[s][0] < row < galaxies[f][0]
                for row in exp_rows
            ]
        )
        expandable_cols = sum(
            [
                galaxies[f][1] < col < galaxies[s][1]
                or galaxies[s][1] < col < galaxies[f][1]
                for col in exp_cols
            ]
        )

        distance = (
            abs(galaxies[s][0] - galaxies[f][0])
            + expandable_rows * (multiplier - 1)
            + abs(galaxies[s][1] - galaxies[f][1])
            + expandable_cols * (multiplier - 1)
        )  # manhattan distance altered with expandable rows/cols
        distances.append(distance)

    return sum(distances)


with open("11/input.txt") as f:
    input = f.read()


# part 1
test_result1 = part1(*prepare_data(test_input1))
assert test_result1 == 374, f"Test result in part 1 should be 374, not {test_result1}"

result1 = part1(*prepare_data(input))
print(result1)  # not 9532259 -> expand also cols, 9769724

# part2
test_result2 = part1(*prepare_data(test_input1), multiplier=10)
assert test_result2 == 1030, f"Test result in part 2 should be 1030, not {test_result2}"

result2 = part1(*prepare_data(input), multiplier=1_000_000)
print(result2) # 603020563700
