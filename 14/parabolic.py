"""
--- Day 14: Parabolic Reflector Dish ---
https://adventofcode.com/2023/day/14
"""

test_input1 = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""


def prepare_data(input):
    lines = input.splitlines()

    # transpose from cols to rows
    data = ["" for i in range(len(lines[0]))]

    for i in range(len(lines[0])):
        for j in range(len(lines)):
            data[i] += lines[j][i]

    return data


def part1(data):
    result = 0

    for row in data:
        # take advantage of splitting by # and sorting lists
        tilted = "#".join(
            [
                "".join(item)
                for item in [
                    sorted(item, reverse=True) for item in "".join(row).split("#")
                ]
            ]
        )

        for i in range(len(tilted)):
            if tilted[i] == "O":
                result += len(tilted) - i

    return result


with open("14/input.txt") as f:
    input = f.read()


# part 1
test_data1 = prepare_data(test_input1)
test_result1 = part1(test_data1)

assert test_result1 == 136, f"Test result in part 1 should be 136, not {test_result1}"

result1 = part1(prepare_data(input))
print(result1)  # 110677
