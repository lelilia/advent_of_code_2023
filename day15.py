from utils import get_input
import re

TEST_INPUT = "test_input_15"
INPUT = "input_15"


def get_hash(word, start=0):
    current_value = start
    for char in word:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


def part_1(file):
    puzzles = get_input(file)
    result = 0
    for puzzle in puzzles.split(","):
        result += get_hash(puzzle)
    return result


def part_2(file):
    puzzles = get_input(file)
    boxes = {}
    result = 0

    for puzzle in puzzles.split(","):
        label = re.findall("[a-z]+", puzzle)[0]
        box = get_hash(label)
        operation = re.findall("[-=]", puzzle)[0]
        if operation == "=":
            focal_length = int(re.findall("\d", puzzle)[0])
            if box not in boxes:
                boxes[box] = [[label, focal_length]]
            if any([l for l, f in boxes[box] if l == label]):
                boxes[box] = [
                    [l, f] if l != label else [l, focal_length] for l, f in boxes[box]
                ]
            else:
                boxes[box].append([label, focal_length])
        else:
            if box not in boxes:
                continue
            boxes[box] = [[l, f] for l, f in boxes[box] if l != label]

    for box in boxes:
        for i, (_, f) in enumerate(boxes[box]):
            result += (box + 1) * (i + 1) * f
    return result


if __name__ == "__main__":
    assert get_hash("HASH") == 52
    assert (result := get_hash("rn=1")) == 30, f"Expected 30, got {result}"
    assert (result := part_1(TEST_INPUT)) == 1320, f"Expected 1320, got {result}"
    print("Part 1:", part_1(INPUT))

    assert (result := get_hash("rn")) == 0, f"Expected 0, got {result}"
    assert (result := get_hash("qp")) == 1, f"Expected 1, got {result}"
    assert (result := get_hash("cm")) == 0, f"Expected 0, got {result}"

    assert (result := part_2(TEST_INPUT)) == 145, f"Expected 145, got {result}"
    print("Part 2:", part_2(INPUT))
