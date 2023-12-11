"""
Advent of Code 2023
--- Day 10: Pipe Maze ---
"""

from utils import get_input
import numpy as np

INPUT = "input_10"
TEST_INPUT = "test_input_10"
TEST_INPUT_1 = "test_input_10_1"



PIPES = {
    "|": [[1, 0], [-1, 0]],
    "-": [[0, 1], [0, -1]],
    "L": [[-1, 0], [0, 1]],  # |_
    "J": [[-1, 0], [0, -1]],  # _|
    "7": [[0, -1], [1, 0]],
    "F": [[0, 1], [1, 0]],
    ".": [],
}

NEIGHBOURS = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

NEIGHBOUR_PIPES = [["7"], ["|"], ["F"], ["-"], ["-"], ["J"], ["|"], ["L"]]


def find_start(map):
    return [
        [(i, j) for j, col in enumerate(row) if col == "S"]
        for i, row in enumerate(map)
        if "S" in row
    ][0][0]


def pad_matrix(matrix, value="."):
    num_col = len(matrix[0]) + 2
    return (
        [[value] * num_col]
        + [[value] + row + [value] for row in matrix]
        + [[value] * num_col]
    )


def print_map(map):
    for row in map:
        print("".join(row))
    print()


def fill_outside_map(map):
    q = [[0, 0]]
    while q:
        x, y = q.pop()
        map[x][y] = "O"
        for (ix, iy) in NEIGHBOURS:
            if 0 <= x + ix < len(map) and 0 <= y + iy < len(map[0]):
                if map[x + ix][y + iy] == ".":
                    q.append([x + ix, y + iy])
    return map


def blow_up_map(seen, map):
    relevant_map = [
        [x if (i, j) in seen else "." for j, x in enumerate(row)]
        for i, row in enumerate(map)
    ]
    xs, ys = find_start(map)

    if relevant_map[xs + 1][ys] in "|JL" and relevant_map[xs - 1][ys] in "|F7":
        relevant_map[xs][ys] = "|"
    elif relevant_map[xs][ys - 1] in "-LF" and relevant_map[xs][ys + 1] in "-7J":
        relevant_map[xs][ys] = "-"
    elif relevant_map[xs][ys + 1] in "-7J" and relevant_map[xs + 1][ys] in "|LJ":
        relevant_map[xs][ys] = "F"
    elif relevant_map[xs - 1][ys] in "|7F" and relevant_map[xs][ys - 1] in "-FL":
        relevant_map[xs][ys] = "J"
    elif relevant_map[xs - 1][ys] in "|7F" and relevant_map[xs][ys + 1] in "-7J":
        relevant_map[xs][ys] = "L"
    else:
        relevant_map[xs][ys] = "7"
    new_map = [["." for _ in range(len(map[0]) * 2)] for _ in range(len(map) * 2)]
    for x in range(len(map)):
        for y in range(len(map[0])):
            if relevant_map[x][y] == ".":
                continue
            elif relevant_map[x][y] == "J":
                new_map[x * 2][y * 2] = "#"
            elif relevant_map[x][y] == "F":
                new_map[x * 2][y * 2] = "#"
                new_map[x * 2 + 1][y * 2] = "#"
                new_map[x * 2][y * 2 + 1] = "#"
            elif relevant_map[x][y] in "L-":
                new_map[x * 2][y * 2] = "#"
                new_map[x * 2][y * 2 + 1] = "#"
            elif relevant_map[x][y] in "7|":
                new_map[x * 2][y * 2] = "#"
                new_map[x * 2 + 1][y * 2] = "#"
    return new_map


def count_inside_in_blows_map(map):
    count = 0
    for i in range(0, len(map), 2):
        for j in range(0, len(map[0]), 2):
            if map[i][j] == map[i + 1][j] == map[i + 1][j + 1] == map[i][j + 1] == ".":
                count += 1
    return count


def part_1(file):
    raw_map = get_input(file)
    map = [[letter for letter in row] for row in raw_map.split("\n")]
    map = pad_matrix(map)
    x, y = find_start(map)
    seen = {}
    starting_points = []
    # find connected to start
    for i, n in enumerate(NEIGHBOURS):
        dx, dy = n
        if map[x + dx][y + dy] == NEIGHBOUR_PIPES[i][0]:
            starting_points.append([x + dx, y + dy])
    seen[(x, y)] = True
    steps = 1
    q = [starting_points[0]]
    while q:
        x, y = q.pop()
        if (x, y) in seen:
            return steps
        seen[(x, y)] = True
        steps += 1
        nexts = PIPES[map[x][y]]
        for n in nexts:
            dx, dy = n
            if (x + dx, y + dy) not in seen:
                q.append([x + dx, y + dy])
    return steps // 2


def part_2(file):
    raw_map = get_input(file)
    map = [[letter for letter in row] for row in raw_map.split("\n")]
    map = pad_matrix(map)
    x, y = find_start(map)
    seen = {}
    starting_points = []
    for i, n in enumerate(NEIGHBOURS):
        dx, dy = n
        if map[x + dx][y + dy] == NEIGHBOUR_PIPES[i][0]:
            starting_points.append([x + dx, y + dy])
    seen[(x, y)] = True
    steps = 1
    q = [starting_points[0]]
    while q:
        x, y = q.pop()
        if (x, y) in seen:
            return steps
        seen[(x, y)] = True
        steps += 1
        nexts = PIPES[map[x][y]]
        for n in nexts:
            dx, dy = n
            if (x + dx, y + dy) not in seen:
                q.append([x + dx, y + dy])
    b_map = blow_up_map(seen, map)
    filled_map = fill_outside_map(b_map)
    count = count_inside_in_blows_map(filled_map)
    return count


if __name__ == "__main__":
    assert (result := find_start([[0, 0, 0, 0, "S"], [0, 0, 0, 0, 0]])) == (
        0,
        4,
    ), f"Expected (0,4) got {result}"

    print("Part 1:", part_1(INPUT))

    print("Part 2:", part_2(INPUT))
