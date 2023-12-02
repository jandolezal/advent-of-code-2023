"""
--- Day 1: Trebuchet?! ---
https://adventofcode.com/2023/day/1
"""

test_input1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

test_input2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


valid_digits = {
    word: str(digit + 1)
    for digit, word in enumerate(
        ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    )
}


def part1(input):
    result = 0
    for line in input.split():
        digits = [char for char in line if char.isdigit()]
        digit = digits[0] + digits[-1]
        result += int(digit)
    return result


def part2(input):
    result = 0
    for line in input.split():
        digits = []
        substring = ""
        for char in line:
            if char.isdigit():
                digits.append(char)
                substring = ""
            else:
                substring += char
                for k in valid_digits.keys():
                    if k in substring:
                        digits.append(valid_digits[k])
                        substring = char  # string digits can overlap
        result += int(digits[0] + digits[-1])
    return result


with open("01/input.txt") as f:
    input = f.read()

# part 1
test_result1 = part1(test_input1)
assert test_result1 == 142, "Result should be 142"
result1 = part1(input)
print(result1)

# part2
test_result2 = part2(test_input2)
assert test_result2 == 281, "Result should be 281"
result2 = part2(input)
print(result2)
