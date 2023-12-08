from utils import get_input, prime_factorization
import re

TEST_INPUT = "test_input_8"
TEST_INPUT_2 = "test_input_8_a"
TEST_INPUT_3 = "test_input_8_b"
INPUT = "input_8"


class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.name}: {self.left}, {self.right}>"

    def ends_with_z(self):
        return self.name[-1] == "Z"


def move_through_map(nodes, rules):
    steps = 0
    current_node = nodes["AAA"]
    while current_node.name != "ZZZ":
        for rule in rules:
            if rule == "L":
                current_node = nodes[current_node.left]
            else:
                current_node = nodes[current_node.right]
            steps += 1
    return steps


def find_cycle(nodes, rules, current_node):
    steps = 0
    while True:
        for rule in rules:
            if current_node.ends_with_z():
                return steps

            steps += 1
            if rule == "L":
                current_node = nodes[current_node.left]
            else:
                current_node = nodes[current_node.right]


def part_1(file):
    input = get_input(file)
    rules, paths = input.split("\n\n")

    nodes = {}
    for path in paths.split("\n"):
        name, left, right = (
            path.strip()
            .replace("(", "")
            .replace(")", "")
            .replace(" =", ",")
            .split(", ")
        )
        nodes[name] = Node(name, left, right)

    return move_through_map(nodes, rules)


def part_2(file):
    input = get_input(file)
    rules, paths = input.split("\n\n")

    nodes = {}
    for path in paths.split("\n"):
        name, left, right = (
            path.strip()
            .replace("(", "")
            .replace(")", "")
            .replace(" =", ",")
            .split(", ")
        )
        nodes[name] = Node(name, left, right)

    starting_points = [key for key in nodes if key[-1] == "A"]
    current_nodes = [nodes[point] for point in starting_points]
    cycles = len(rules)

    for current_node in current_nodes:
        cycles *= find_cycle(nodes, rules, current_node)

    prime = prime_factorization(cycles)
    result = 1
    for prime_factor in set(prime):
        result *= prime_factor
    return result


if __name__ == "__main__":
    assert part_1(TEST_INPUT) == 2
    assert part_1(TEST_INPUT_2) == 6

    print("Part 1:", part_1(INPUT))

    assert (result := part_2(TEST_INPUT_3)) == 6, f"Expected 6 but got {result}"

    print("Part 2:", part_2(INPUT))
