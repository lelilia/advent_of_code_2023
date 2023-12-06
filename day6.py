"""
Advend of Code 2023
--- Day 6: Wait For It ---
"""

import re
from utils import get_input_lines

TEST_INPUT = "test_input_6"
INPUT = "input_6"


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


def part_1(file: str) -> int:
    records = get_input_lines(file)
    times, distances = [[int(x) for x in re.findall(r"\d+", y)] for y in records]

    result = 1
    for i, time in enumerate(times):
        distance = distances[i]
        count_wins = win_one_race(time, distance)
        result *= count_wins
    return result


def part_2(file: int) -> int:
    records = get_input_lines(file)
    time, distance = [int(x.replace(" ", "").split(":")[1]) for x in records]

    return win_one_race(time, distance)


if __name__ == "__main__":
    assert (result := part_1(TEST_INPUT)) == 288, f"Expected 288, got {result}."

    print("Part 1:", part_1(INPUT))

    assert (result := part_2(TEST_INPUT)) == 71503, f"Expected 71503, got {result}."

    print("Part 2:", part_2(INPUT))
