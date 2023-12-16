from utils import get_input, print_map
import numpy as np
import logging

INPUT = "input_16"
TEST_INPUT = "test_input_16"

def energize_map(map, x, y, ix, iy):
    energized = {}

    q = [[x,y,ix,iy]]
    while q:
        x, y, ix, iy = q.pop(0)
        if x < 0 or x > map.shape[0] - 1:
            continue
        if y < 0 or y > map.shape[1] - 1:
            continue
        if (x,y) in energized:
            if energized[(x,y)] == (ix, iy):
                continue
        energized[(x,y)] = (ix,iy)
        tile = map[x,y]
        if tile == "." or tile == "|" and iy == 0 or tile == "-" and ix == 0:
            q.append([x+ix,y+iy,ix,iy])
        elif tile == "|" and iy != 0:
            q.append([x-1, y, -1, 0]) # up
            q.append([x+1,y, 1, 0])   # down
        elif tile == "-" and ix != 0:
            q.append([x,y-1, 0, -1]) # left
            q.append([x,y+1, 0, 1]) # right
        elif tile == "/":
            if ix == 1: # coming from up
                q.append([x, y-1, 0, -1] ) # left
            elif iy == 1: # coming from left
                q.append([x - 1,y, -1, 0] ) # up
            elif ix == -1: # coming from down
                q.append([x, y + 1, 0, 1]) # right
            else: # coming from right
                q.append([x + 1, y, 1, 0] ) # down
        elif tile == "\\":
            if ix == 1: # coming from up
                q.append([x, y + 1, 0, 1] ) # right
            elif iy == -1: # coming from right
                q.append([x - 1, y, -1, 0] ) # up
            elif ix == -1: # coming from down
                q.append([x, y-1, 0, -1] ) # left
            else: # coming from left
                q.append([x + 1, y, 1, 0] ) # down
    return len(energized)


def part_1(file):
    raw_map = get_input(file)
    map = np.array([np.array([x for x in row.strip()]) for row in raw_map.split("\n")])
    return energize_map(map, 0, 0, 0, 1)


def part_2(file):
    raw_map = get_input(file)
    map = np.array([np.array([x for x in row.strip()]) for row in raw_map.split("\n")])

    max_x = map.shape[0] - 1
    max_y = map.shape[1] - 1
    max_e = 0
    for x in range(max_x + 1):
        max_e = max(max_e, energize_map(map, x, 0, 0, 1))
        max_e = max(max_e, energize_map(map, x, max_y, 0, -1))
    for y in range(max_y + 1):
        max_e = max(max_e, energize_map(map, 0, y, 1, 0))
        max_e = max(max_e, energize_map(map, max_x, y, -1, 0))
    return max_e


if __name__ == "__main__":
    assert (result := part_1(TEST_INPUT)) == 46, f"Expected 46, got {result}"
    print("Part 1:", part_1(INPUT))

    assert (result := part_2(TEST_INPUT)) == 51, f"Expected 51, got {result}"
    print("Part 2:", part_2(INPUT))