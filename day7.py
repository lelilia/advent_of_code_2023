"""
Advent of Code

"""
from utils import get_input_lines
from functools import cmp_to_key

TEST_INPUT = "test_input_7"
INPUT = "input_7"
ORDER_1 = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

ORDER_2 = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}


def get_type(hand):
    counts = sorted([hand.count(x) for x in set(hand)])
    max_counts = max(counts)

    # five of a kind
    if max_counts == 5:
        return 6
    # four of a kind
    if max_counts == 4:
        return 5
    if max_counts == 3:
        # full house
        if counts == [2, 3]:
            return 4
        # three of a kind
        else:
            return 3
    if max_counts == 2:
        # two pair
        if counts == [1, 2, 2]:
            return 2
        # one pair
        else:
            return 1
    # high card
    return 0


def get_type_with_joker(hand):
    cnt_jokers = hand.count("J")
    if cnt_jokers == 5:
        return 6
    counts = sorted([hand.count(x) for x in set(hand) - set("J")])
    max_counts = max(counts)

    # five of a kind
    if max_counts + cnt_jokers == 5:
        return 6
    # four of a kind
    if max_counts + cnt_jokers == 4:
        return 5
    if max_counts + cnt_jokers == 3:
        # full house
        if counts == [2, 3] or counts == [2, 2]:
            return 4
        # three of a kind
        else:
            return 3
    if max_counts + cnt_jokers == 2:
        # two pair
        if counts == [1, 2, 2] or counts == [1, 1, 1, 2] and cnt_jokers == 1:
            return 2
        # one pair
        else:
            return 1
    # high card
    return 0


def compare_hands(hand_1, hand_2):
    if get_type(hand_1[0]) > get_type(hand_2[0]):
        return 1
    elif get_type(hand_1[0]) < get_type(hand_2[0]):
        return -1
    else:
        for i in range(5):
            if ORDER_1[hand_1[0][i]] > ORDER_1[hand_2[0][i]]:
                return 1
            elif ORDER_1[hand_1[0][i]] < ORDER_1[hand_2[0][i]]:
                return -1
    return 0


def compare_hands_with_joker(hand_1, hand_2):
    if get_type_with_joker(hand_1[0]) > get_type_with_joker(hand_2[0]):
        return 1
    elif get_type_with_joker(hand_1[0]) < get_type_with_joker(hand_2[0]):
        return -1
    else:
        for i in range(5):
            if ORDER_2[hand_1[0][i]] > ORDER_2[hand_2[0][i]]:
                return 1
            elif ORDER_2[hand_1[0][i]] < ORDER_2[hand_2[0][i]]:
                return -1
    return 0


def part_1(file):
    games = get_input_lines(file)
    games = [game.strip().split(" ") for game in games]
    games = sorted(games, key=cmp_to_key(compare_hands))
    winnings = 0
    for i, game in enumerate(games):
        winnings += int(game[1]) * (i + 1)
    return winnings


def part_2(file):
    games = get_input_lines(file)
    games = [game.strip().split(" ") for game in games]
    games = sorted(games, key=cmp_to_key(compare_hands_with_joker))
    winnings = 0
    for i, game in enumerate(games):
        winnings += int(game[1]) * (i + 1)
    return winnings


if __name__ == "__main__":

    # Part 1
    assert (get_type("AAAAA")) == 6
    assert (get_type("AA8AA")) == 5
    assert (get_type("23332")) == 4
    assert (get_type("TTT98")) == 3
    assert (get_type("23432")) == 2
    assert (get_type("A23A4")) == 1
    assert (get_type("23456")) == 0
    assert (
        result := sorted([["KK677", 28], ["KTJJT", 220]], key=cmp_to_key(compare_hands))
    ) == (
        expected := [["KTJJT", 220], ["KK677", 28]]
    ), f"Expected {expected} got {result}"

    assert (result := part_1(TEST_INPUT)) == 6440, f"Expected 6440, got {result}."

    print("Part 1:", part_1(INPUT))

    # Part 2
    assert (get_type_with_joker("AAAAA")) == 6
    assert (get_type_with_joker("AA8AA")) == 5
    assert (get_type_with_joker("23332")) == 4
    assert (get_type_with_joker("TTT98")) == 3
    assert (get_type_with_joker("23432")) == 2
    assert (get_type_with_joker("A23A4")) == 1
    assert (get_type_with_joker("23456")) == 0
    assert (get_type_with_joker("T55J5")) == 5
    assert (get_type_with_joker("KTJJT")) == 5
    assert (get_type_with_joker("QQQJA")) == 5
    assert (get_type_with_joker("JJJJJ")) == 6

    assert (result := part_2(TEST_INPUT)) == 5905, f"Expected 5905, got {result}."

    print("Part 2:", part_2(INPUT))
