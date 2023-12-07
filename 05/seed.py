"""
--- Day 5: If You Give A Seed A Fertilizer ---
https://adventofcode.com/2023/day/5
"""

test_input1 = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


def prepare_data(input):
    data = {}
    for subsection in input.split("\n\n"):
        name, values = subsection.split(":")
        data[name.replace(" map", "")] = [
            [int(num) for num in row.split(" ")] for row in values.strip().split("\n")
        ]
    data["seeds"] = data["seeds"][0]  # flatten seeds values
    # print(data)
    return data


def _translate(source, destination):
    result = {}
    for source_value in source:
        result[source_value] = source_value  # default
        for row in destination:
            if row[1] <= source_value < row[1] + row[2]:
                result[source_value] = source_value + row[0] - row[1]
    return result


def part1(data):
    # seed_to_soil = _translate(data["seeds"], data["seed-to-soil"])
    # soil_to_fertilizer = _translate(seed_to_soil.values(), data["soil-to-fertilizer"])
    seeds = data["seeds"]
    data_wo_seeds = data.copy()
    data_wo_seeds.pop("seeds")

    result = {}

    for source, destination in zip(data, data_wo_seeds):
        if destination == "seed-to-soil":  # first iteration
            result[destination] = _translate(seeds, data[destination])
        else:
            result[destination] = _translate(result[source].values(), data[destination])

    return min(result["humidity-to-location"].values())


with open("05/input.txt") as f:
    input = f.read()

test_data1 = prepare_data(test_input1)
test_result1 = part1(test_data1)
assert test_result1 == 35, f"Test result in part 1 should be 35, not {test_result1}"

data1 = prepare_data(input)
result1 = part1(data1)
print(result1)  # 389056265
