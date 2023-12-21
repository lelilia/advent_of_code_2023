from utils import get_input, print_map
import numpy as np
import re

INPUT = "input_18"
TEST_INPUT = "test_input_18"

DIRECTION = {
    "U": [-1, 0],
    "L": [0, -1],
    "D": [1, 0],
    "R": [0, 1]
}




def decode_hex(hex):
    hex = re.findall(r"[a-z0-9]{6}", hex)[0]
    distance = int(hex[:-1], 16)
    direction = "RDLU"[int(hex[-1])]
    return direction, distance

def part_1(file):
    raw_paths = get_input(file)
    area = 0
    y = 0
    last_direction = raw_paths.split("\n")[-1].split(" ")[0]
    for path in raw_paths.split("\n"):
        direction, distance, _ = path.strip().split(" ")
        distance = int(distance)
        if direction == "R":
            area += distance * y
        elif direction == "L":
            area -= distance * y
        elif direction == "U":
            y += distance
        elif direction == "D":
            y -= distance
        extra = 0.25
        if last_direction + direction in "LDRUL":
            extra = -0.25
        area += distance / 2 + extra
        last_direction = direction
    return int(area)


def part_2(file):
    raw_paths = get_input(file)
    area = 0
    y = 0
    last_direction, _ = decode_hex(raw_paths.split("\n")[-1])
    for path in raw_paths.split("\n"):
        direction, distance  = decode_hex(path)
        distance = int(distance)
        if direction == "R":
            area += distance * y
        elif direction == "L":
            area -= distance * y
        elif direction == "U":
            y += distance
        elif direction == "D":
            y -= distance
        extra = 0.25
        if last_direction + direction in "LDRUL":
            extra = -0.25
        area += distance / 2 + extra
        last_direction = direction
    return abs(int(area))



if __name__ == "__main__":
    assert (result:= part_1(TEST_INPUT)) == 62, f"Expected 62, got {result}"
    print("Part 1:", part_1(INPUT))


    assert (result := decode_hex("#70c710")) == (expected := ("R", 461937)), f"Expected {expected}, got {result}"
    assert (result := decode_hex("#0dc571")) == (expected := ("D", 56407)), f"Expected {expected}, got {result}"

    assert(result := part_2(TEST_INPUT)) == (expected := 952408144115), f"Expected {expected}, got {result}"
    print("Part 2:", part_2(INPUT))