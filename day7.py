"""
Advent of Code

"""
from utils import get_input_lines
from functools import cmp_to_key

TEST_INPUT = "test_input_7"
INPUT = "input_7"


class Game:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.value_1 = None
        self.value_2 = None
        self.order_1 = "AKQJT98765432"[::-1]
        self.order_2 = "AKQT98765432J"[::-1]

        self.get_value_part_1()
        self.get_value_part_2()

    def __repr__(self):
        return f"<{self.hand} -> {self.value_1}>"

    def get_hand_type_part_1(self):
        counts = sorted([self.hand.count(x) for x in set(self.hand)])
        max_counts = max(counts)
        if max_counts == 5:  # five of a kind
            return 6
        if max_counts == 4:  # four of a kind
            return 5
        if max_counts == 3:
            if counts == [2, 3]:  # full house
                return 4
            else:  # three of a kind
                return 3
        if max_counts == 2:
            if counts == [1, 2, 2]:  # two pair
                return 2
            else:  # one pair
                return 1
        return 0  # high card

    def get_hand_type_part_2(self):
        cnt_jokers = self.hand.count("J")
        if cnt_jokers == 5:
            return 6
        counts = sorted([self.hand.count(x) for x in set(self.hand) - set("J")])
        max_counts = max(counts)
        if max_counts + cnt_jokers == 5:  # five of a kind
            return 6
        if max_counts + cnt_jokers == 4:  # four of a kind
            return 5
        if max_counts + cnt_jokers == 3:
            if counts == [2, 3] or counts == [2, 2]:  # full house
                return 4
            else:  # three of a kind
                return 3
        if max_counts + cnt_jokers == 2:
            if (
                counts == [1, 2, 2] or counts == [1, 1, 1, 2] and cnt_jokers == 1
            ):  # two pair
                return 2
            else:  # one pair
                return 1
        return 0  # high card

    def get_value_part_1(self):
        value = self.get_hand_type_part_1()
        for card in self.hand:
            value *= 100
            value += self.order_1.index(card)
        self.value_1 = value

    def get_value_part_2(self):
        value = self.get_hand_type_part_2()
        for card in self.hand:
            value *= 100
            value += self.order_2.index(card)
        self.value_2 = value


def parse_input(file):
    games = get_input_lines(file)
    games = [game.strip().split(" ") for game in games]
    return games


def solve(file, part):
    games_input = parse_input(file)
    winnings = 0
    games = []
    for game in games_input:
        hand, bid = game
        games.append(Game(hand, int(bid)))
    if part == 1:
        games = sorted(games, key=lambda x: x.value_1)
    else:
        games = sorted(games, key=lambda x: x.value_2)
    for i, game in enumerate(games):
        winnings += game.bid * (i + 1)
    return winnings


def part_1(file):
    return solve(file, 1)


def part_2(file):
    return solve(file, 2)


if __name__ == "__main__":

    assert (result := Game("KTJJT", 0).value_1) == (
        expected := 21108090908
    ), f"Expected {expected}, got {result}"

    assert (result := part_1(TEST_INPUT)) == 6440, f"Expected 6440, got {result}"

    print("Part 1:", part_1(INPUT))

    assert (result := part_2(TEST_INPUT)) == 5905, f"Expected 5905, got {result}."

    print("Part 2:", part_2(INPUT))
