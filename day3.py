from utils import get_input
import numpy as np

TEST_INPUT = "test_input_3"
INPUT = "input_3"


def find_number(schema, i, j):
    start_j = j
    while schema[i, j] in "1234567890":
        j += 1
    return schema[i, start_j:j], start_j, j


def check_for_symbols(schema, i, start_j, end_j):

    for symbol in "$/-+@&=%#*":
        if symbol in schema[i - 1 : i + 2, start_j - 1 : end_j + 1]:
            return True
    return False


def get_schema(file):
    input = get_input(file)
    schema = np.array([np.array([char for char in row]) for row in input.split("\n")])
    schema_shape = schema.shape
    schema = np.pad(schema, 1, "constant", constant_values=".")
    return schema, schema_shape


def get_numbers(file):
    input = get_input(file)
    schema = np.array([np.array([char for char in row]) for row in input.split("\n")])
    schema_shape = schema.shape
    schema = np.pad(schema, 1, "constant", constant_values=".")

    numbers = {}
    number_index = {}
    number_pos = {}
    index = 0
    i = j = 1
    while i <= schema_shape[0]:
        while j <= schema_shape[1]:
            if schema[i, j] in "1234567890":
                number, start_j, j = find_number(schema, i, j)
                number = int("".join(number))
                if check_for_symbols(schema, i, start_j, j):

                    for x in range(start_j, j):
                        numbers[i, x] = number
                        number_pos[i, x] = index
                        number_index[index] = number
                    index += 1
            j += 1
        i += 1
        j = 1
    return numbers, number_pos, number_index


def part_1(file):
    schema, schema_shape = get_schema(file)

    sum = 0
    i = j = 1
    while i <= schema_shape[0]:
        while j <= schema_shape[1]:
            if schema[i, j] in "1234567890":
                number, start_j, j = find_number(schema, i, j)
                number = int("".join(number))
                if check_for_symbols(schema, i, start_j, j):
                    sum += number
            j += 1
        i += 1
        j = 1
    return sum


def part_2(file):
    schema, schema_shape = get_schema(file)
    numbers, number_pos, number_index = get_numbers(file)

    sum = 0
    i = j = 1
    stars = np.where(schema == "*")

    for index in range(len(stars[0])):
        x, y = stars[0][index], stars[1][index]

        value_1 = None
        index_1 = None
        value_2 = None
        for s in range(x - 1, x + 2):
            for t in range(y - 1, y + 2):
                if (s, t) in number_pos:
                    if not value_1:
                        index_1 = number_pos[s, t]
                        value_1 = number_index[index_1]
                    else:
                        if index_1 == number_pos[s, t]:
                            continue
                        else:
                            value_2 = number_index[number_pos[s, t]]
        if value_1 and value_2:
            sum += value_1 * value_2
    return sum


if __name__ == "__main__":
    assert part_1(TEST_INPUT) == 4361
    print("Part 1:", part_1(INPUT))

    assert part_2(TEST_INPUT) == 467835
    print("Part 2:", part_2(INPUT))
