"""
Advent of Code 2023
--- Day 12: Hot Springs ---
"""
from utils import get_input
import logging

INPUT = "input_12"
TEST_INPUT = "test_input_12"

seen = {}


def recurse(springs, checks):
    global seen
    if (springs, checks) in seen:
        return seen[(springs, checks)]
    if len(springs) == 0:
        if len(checks) > 0:
            return 0

    if len(checks) == 0:
        if "#" in springs:
            return 0
        return 1
    if springs[0] == ".":
        recurse(springs[1:], checks)
    next_check = checks[0]
    possibilities = 0

    max_start = len(springs) - sum(checks) - len(checks) + 1
    max_start_signs = springs.find("#")
    if max_start_signs >= 0:
        max_start = min(max_start, max_start_signs)
    for i in range(max_start + 1):

        logging.debug(f"i: {i}, springs[i:i+next]: {springs[i:i+next_check]}")
        if "." in springs[i : i + next_check]:
            continue
        else:
            if i > 0 and springs[i - 1] == "#":
                continue
            if i + next_check < len(springs) and springs[i + next_check] == "#":
                continue
        j = 1
        while i + next_check + j < len(springs) and springs[i + next_check + j] == ".":
            j += 1
        possibilities += recurse(springs[i + next_check + j :], checks[1:])
    seen[(springs, checks)] = possibilities
    return possibilities


def part_1(file):
    rows = get_input(file)
    count = 0
    for row in rows.split("\n"):
        springs, checks = row.split(" ")
        checks = tuple([int(x) for x in checks.split(",")])
        count += recurse(springs, checks)
    return count


def part_2(file):
    rows = get_input(file)
    count = 0
    for i, row in enumerate(rows.split("\n")):
        print(i)
        springs, checks = row.split(" ")
        springs = "?".join([springs] * 5)
        checks = tuple([int(x) for x in ",".join([checks] * 5).split(",")])
        count += recurse(springs, checks)
    return count


if __name__ == "__main__":
    assert (result := recurse("???", (1, 1))) == (
        expected := 1
    ), f"Expected {expected}, got {result}"
    assert (result := recurse("?#?#?#?#?#?#?#?", (1, 3, 1, 6))) == (
        expected := 1
    ), f"Expected {expected}, got {result}"
    assert (result := recurse("???.###", (1, 1, 3))) == (
        expected := 1
    ), f"Expected {expected}, got {result}"
    assert (result := recurse(".??..??...?##.", (1, 1, 3))) == (
        expected := 4
    ), f"Expected {expected}, got {result}"
    assert (result := recurse("????.#...#...", (4, 1, 1))) == (
        expected := 1
    ), f"Expected {expected}, got {result}"
    assert (result := recurse("????.######..#####.", (1, 6, 5))) == (
        expected := 4
    ), f"Expected {expected}, got {result}"
    assert (result := recurse("?###????????", (3, 2, 1))) == (
        expected := 10
    ), f"Expected {expected}, got {result}"
    assert (result := recurse("?.?????#???#?", (1, 1, 2, 2))) == (
        expected := 22
    ), f"Expected {expected}, got {result}"
    assert (result := recurse("????.#????#?????#??#", (1, 2, 1, 1, 7))) == (
        expected := 5
    ), f"Expected {expected}, got {result}"
    assert (result := recurse("???#?.???????.?", (3, 1, 1, 1, 1))) == (
        expected := 22
    ), f"Expected {expected}, got {result}"
    assert (result := recurse(".??..??...?##.", (1, 1, 3))) == (
        expected := 4
    ), f"Expected {expected}, got {result}"
    assert (result := recurse("????.######..#####.", (1, 6, 5))) == (
        expected := 4
    ), f"Expected {expected}, got {result}"
    assert (result := recurse("?#.??.?#.#?#?????", (1, 2, 2, 4, 1))) == (
        expected := 3
    ), f"Expected {expected}, got {result}"

    assert (result := part_1(TEST_INPUT)) == 21, f"Expected 21, got {result}"
    print("Part 1:", part_1(INPUT))

    assert (result := part_2(TEST_INPUT)) == 525152, f"Expected 525152, got {result}"
    print("Part 2:", part_2(INPUT))
