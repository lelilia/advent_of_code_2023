"""
Advend of Code 2023
--- Day 6: Wait For It ---
"""

import re
from utils import get_input_lines
from math import sqrt, ceil


TEST_INPUT = "test_input_6"
INPUT = "input_6"


def solve(time, distance):
    start = ceil(time / 2 - sqrt(time**2 / 4 - distance) + 0.1)
    return time - 2 * start + 1


def part_1(file):
    records = get_input_lines(file)
    times, distances = [[int(x) for x in re.findall(r"\d+", y)] for y in records]

    result = 1
    for i, time in enumerate(times):
        distance = distances[i]
        count_wins = solve(time, distance)
        result *= count_wins
    return result


def part_2(file: int) -> int:
    records = get_input_lines(file)
    time, distance = [int(x.replace(" ", "").split(":")[1]) for x in records]

    return solve(time, distance)


####### solution with search algorithm ####
def is_win(speed, time, distance):
    return speed * time > distance


def get_wins(time, distance):
    lower_limit = 0
    upper_limit = time + 1
    while upper_limit - lower_limit > 1:
        curr = (lower_limit + upper_limit) // 2
        if is_win(curr, time - curr, distance):
            upper_limit = curr
        else:
            lower_limit = curr

    return time - 2 * upper_limit + 1


def part_1_a(file):
    records = get_input_lines(file)
    times, distances = [[int(x) for x in re.findall(r"\d+", y)] for y in records]

    result = 1
    for i, time in enumerate(times):
        distance = distances[i]
        count_wins = get_wins(time, distance)
        result *= count_wins
    return result


def part_2_a(file: int) -> int:
    records = get_input_lines(file)
    time, distance = [int(x.replace(" ", "").split(":")[1]) for x in records]

    return get_wins(time, distance)


####### brute force solution ######
def win_one_race(time: int, distance: int) -> int:
    count_wins = 0
    if time % 2 == 0:
        count_wins += 1
    for t in range(1, (time + 1) // 2):
        speed = t
        travel = (time - t) * speed
        if travel > distance:
            count_wins += 2
    return count_wins


def part_1_brute_force(file: str) -> int:
    records = get_input_lines(file)
    times, distances = [[int(x) for x in re.findall(r"\d+", y)] for y in records]

    result = 1
    for i, time in enumerate(times):
        distance = distances[i]
        count_wins = win_one_race(time, distance)
        result *= count_wins
    return result


def part_2_brute_force(file: int) -> int:
    records = get_input_lines(file)
    time, distance = [int(x.replace(" ", "").split(":")[1]) for x in records]

    return win_one_race(time, distance)


if __name__ == "__main__":

    assert (result := solve(30, 200)) == 9, f"Expected 9 got {result}"
    assert solve(7, 9) == 4
    assert solve(15, 40) == 8

    assert get_wins(30, 200) == 9
    assert get_wins(7, 9) == 4
    assert get_wins(15, 40) == 8

    assert (result := part_1(TEST_INPUT)) == 288, f"Expected 288, got {result}."

    print("Part 1:", part_1(INPUT))

    assert (result := part_2(TEST_INPUT)) == 71503, f"Expected 71503, got {result}."

    print("Part 2:", part_2(INPUT))
