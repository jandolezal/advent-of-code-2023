"""
--- Day 3: Gear Ratios ---
https://adventofcode.com/2023/day/3
"""

test_input1 = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def read_grid(input):
    width = len(input.splitlines()[0])
    height = len(input.splitlines())

    symbols = []
    ids = []

    digit = None
    building_id = False

    for i, row in enumerate(input.splitlines()):
        for j, char in enumerate(row):
            if char.isdigit():
                if not building_id:
                    digit = {"id": char, "coordinates": set([(i, j)]), "is_part": False}
                    building_id = True
                else:
                    digit["id"] += char
                    digit["coordinates"].add((i, j))
            else:
                if building_id:  # reset id building
                    ids.append(digit)
                    building_id = False
                    digit = None

                if char != ".":
                    symbol = {
                        "character": char,
                        "coordinates": (i, j),
                        "adjacent": set(
                            [
                                (i - 1, j - 1 if j - 1 >= 0 and i - 1 >= 0 else None),
                                (i - 1, j if i - 1 >= 0 else None),
                                (
                                    i - 1,
                                    j + 1 if j + 1 <= width and i - 1 >= 0 else None,
                                ),
                                (i, j - 1 if j - 1 >= 0 else None),
                                (i, j + 1 if j + 1 <= width else None),
                                (
                                    i + 1,
                                    j - 1 if i + 1 <= height and j - 1 >= 0 else None,
                                ),
                                (i + 1, j if i + 1 <= height else None),
                                (
                                    i + 1,
                                    j + 1
                                    if i + 1 <= height and j + 1 <= width
                                    else None,
                                ),
                            ]
                        ),
                    }
                    symbols.append(symbol)
    return symbols, ids


def part1(input):
    symbols, ids = read_grid(input)
    for id_ in ids:
        for symbol in symbols:
            if len(id_["coordinates"] & symbol["adjacent"]) > 0:
                id_["is_part"] = True
                continue
    result = 0
    for id_ in ids:
        if id_["is_part"]:
            result += int(id_["id"])
    return result


def part2(input):
    symbols, ids = read_grid(input)
    result = 0
    for symbol in symbols:
        if symbol["character"] == "*":
            symbol["parts"] = []
            for id_ in ids:
                if len(symbol["adjacent"] & id_["coordinates"]) > 0:
                    symbol["parts"].append(id_["id"])

            if len(symbol["parts"]) == 2:
                result += int(symbol["parts"][0]) * int(symbol["parts"][1])
    return result


with open("03/input.txt") as f:
    input = f.read()

read_grid(test_input1)

test_result1 = part1(test_input1)
assert (test_result1 == 4361), f"Result for test input in part 1 should be 4361, not {test_result1}"
result1 = part1(input)
print(result1)


test_result2 = part2(test_input1)
assert (test_result2 == 467835), f"Result for test input in part 2 should be 467835, not {test_result2}"
result2 = part2(input)
print(result2)
