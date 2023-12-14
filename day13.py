from utils import get_input, print_map
import numpy as np

INPUT = "input_13"
TEST_INPUT = "test_input_13"

def check_specific_row(map, split):
    for i in range(min(split, map.shape[0] - split)):
        if not all(map[split-i-1, :] == map[split+i, :]):
            return False
    return True


def check_specific_col(map, split):
    for i in range(min(split, map.shape[1]  - split)):
        if not all(map[:, split-i-1] == map[:, split+i ]):
            return False
    return True


def check_rows(map):
    for i in range(1,len(map)):
        if check_specific_row(map,i):
            return i
    return 0


def check_cols(map):
    for i in range(1, map.shape[1]):
        if check_specific_col(map, i):
            return i
    return 0


def check_row_with_smudge(map, split):
    difference = 0
    for i in range(min(split, map.shape[0] - split)):
        if (num_false := list(map[split-i-1,:] == map[split+i, :]).count(False)) > 1:
            return False
        difference += num_false
    return difference == 1


def check_col_with_smudge(map, split):
    difference = 0
    for i in range(min(split, map.shape[1] - split)):
        if (num_false := list(map[:, split-i-1] == map[:, split+i]).count(False)) > 1:
            return False
        difference += num_false
    return difference == 1


def check_rows_with_smudge(map):
    for i in range(1, map.shape[0]):
        if check_row_with_smudge(map, i):
            return i
    return 0


def check_cols_with_smudge(map):
    for i in range(1, map.shape[1]):
        if check_col_with_smudge(map, i):
            return i
    return 0


def part_1(file):
    puzzles = get_input(file).split("\n\n")
    result = 0
    for puzzle in puzzles:
        puzzle = np.array([np.array([x for x in row.strip()]) for row in puzzle.split("\n")])
        result += check_rows(puzzle) * 100
        result += check_cols(puzzle)
    return result


def part_2(file):
    puzzles = get_input(file).split("\n\n")
    result = 0
    for puzzle in puzzles:
        puzzle = np.array([np.array([x for x in row.strip()]) for row in puzzle.split("\n")])
        result += check_rows_with_smudge(puzzle) * 100
        result += check_cols_with_smudge(puzzle)
    return result


if __name__ == "__main__":

    assert part_1(TEST_INPUT) == 405

    print("Part 1:", part_1(INPUT))

    assert(result := part_2(TEST_INPUT)) == 400, f"Expected 400, got {result}"

    print("Part 2:", part_2(INPUT))