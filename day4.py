"""
Advent of Code 2023
--- Day 4: Scratchcards ---
"""

import re
from utils import get_input_lines

TEST_INPUT = "test_input_4"
INPUT = "input_4"


def get_number_of_winns(game):
    game = game.strip().replace(":", "|")
    _, winning, my_numbers = game.split("|")
    winning = set([int(x) for x in re.findall(r"(\d+)", winning)])
    my_numbers = set([int(x) for x in re.findall(r"(\d+)", my_numbers)])
    return len(winning.intersection(my_numbers))


def part_1(file):
    games = get_input_lines(file)
    points = 0
    for game in games:
        cnt_winning = get_number_of_winns(game)
        if cnt_winning:
            points += 2 ** (cnt_winning - 1)
    return points


def part_2(file):
    games = get_input_lines(file)
    number_of_cards = [1] * len(games)

    for game_round, game in enumerate(games):
        cnt_winns = get_number_of_winns(game)
        for i in range(game_round + 1, game_round + cnt_winns + 1):
            number_of_cards[i] += number_of_cards[game_round]
    return sum(number_of_cards)


if __name__ == "__main__":
    assert (result := part_1(TEST_INPUT)) == 13, f"Expected 13 got {result}"
    print("Part 1:", part_1(INPUT))

    assert (result := part_2(TEST_INPUT)) == 30, f"Expected 30 but got {result}"
    print("Part 2:", part_2(INPUT))
