"""
Advent of Code 2023
--- Day 9: Mirage Maintenance ---
"""
import re
from utils import get_input_lines

TEST_INPUT = "test_input_9"
INPUT = "input_9"

def extrapolate(history):
    seq = {}
    seq[0] = [int(x) for x in re.findall(r"-*\d+", history)]
    i = 0
    while any(seq[i]) != 0:
        i += 1
        seq[i] = [j - i for i, j in zip(seq[i-1][:-1], seq[i-1][1:])]
    future_diff = past_diff =0

    while i >= 0:
        future_diff += seq[i][-1]
        past_diff = seq[i][0] - past_diff
        seq[i] = [past_diff] + seq[i] + [future_diff]
        i -= 1
    return past_diff, future_diff


def part_1(file):
    histories = get_input_lines(file)
    sum = 0
    for history in histories:
        _, future_prediction = extrapolate(history)
        sum += future_prediction
    return sum


def part_2(file):
    histories = get_input_lines(file)
    sum = 0
    for history in histories:
        past_prediction, _ = extrapolate(history)
        sum += past_prediction
    return sum

if __name__ == "__main__":


    assert part_1(TEST_INPUT) == 114

    print("Part 1:", part_1(INPUT))

    assert (result := extrapolate("0 3 6 9 12 15")) == (-3, 18), f"Expected -3, 18 got {result}"

    assert (result := part_2(TEST_INPUT)) == 2, f"Expected 2, got {result}"

    print("Part 2:", part_2(INPUT))