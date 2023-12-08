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


def part2(data, start=0, end=100):
    """Brute force solution starting from location and looking for corresponding seed."""
    location = start
    while location < end:
        if location % 1_000_000 == 0:
            print(location)
        target = location
        for mapping in list(data.keys())[::-1]:
            if mapping != "seeds":
                for row in data[mapping]:
                    if row[0] <= target < row[0] + row[2]:
                        target = target + row[1] - row[0]
                        break
                if (mapping == "seed-to-soil") and any(
                    [
                        data["seeds"][i]
                        <= target
                        < data["seeds"][i] + data["seeds"][i + 1]
                        for i in range(0, len(data["seeds"]), 2)
                    ]
                ):
                    print("lowest location: ", location, "target: ", target)
                    return location

        location += 1

    return


with open("05/input.txt") as f:
    input = f.read()

test_data1 = prepare_data(test_input1)
test_result1 = part1(test_data1)
assert test_result1 == 35, f"Test result in part 1 should be 35, not {test_result1}"

data1 = prepare_data(input)
result1 = part1(data1)
print(result1)  # 389056265


test_result2 = part2(test_data1)
assert test_result2 == 46, f"Test result in part 2 should be 46, not {test_result2}"
result2 = part2(data1, start=0, end=800_000_000)
print(result2)  # 137516820
