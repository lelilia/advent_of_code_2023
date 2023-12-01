"""
Advent of Code 2023 - Day 1
"""

def get_input_lines(filename):
    with open(filename, "r") as f:
        return f.readlines()

def get_input(filename):
    with open(filename, "r") as f:
        return f.read()

def replace_number_words(lines):
    lines = lines.replace("one", "one1one")
    lines = lines.replace("two", "two2two")
    lines = lines.replace("three", "three3three")
    lines = lines.replace("four", "four4four")
    lines = lines.replace("five", "five5five")
    lines = lines.replace("six", "six6six")
    lines = lines.replace("seven", "seven7seven")
    lines = lines.replace("eight", "eight8eight")
    lines = lines.replace("nine", "nine9nine")
    return lines

def get_sum(lines):
    sum = 0
    for line in lines:
        first = last = None
        for char in line:
            if char.isnumeric():
                if not first:
                    first = char
                last = char
        sum += int(first + last)
    return sum

def part_1(input_file):
    lines = get_input_lines(input_file)
    return get_sum(lines)

def part_2(input_file):
    lines = get_input(input_file)
    lines = replace_number_words(lines)
    lines = lines.split("\n")
    return get_sum(lines)

assert part_1("test_intput_1") == 142

print("Part 1:", part_1("input_1"))

assert part_2("test_intput_1_b") == 281

print("Part 2:", part_2("input_1"))