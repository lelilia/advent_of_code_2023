RULES_1 = {"red": 12, "green": 13, "blue": 14}


def get_input(filename):
    with open(filename, "r") as f:
        return f.readlines()


def part_1(filename, rules):
    games = get_input(filename)

    sum_correct_ids = 0

    for game in games:
        is_possible = True
        game = game.strip()
        game_id, game_moves = game.split(":")
        game_id = int(game_id.replace("Game ", ""))

        for move in game_moves.split(";"):
            for cubes in move.strip().split(","):
                cubes = cubes.strip()
                number, color = cubes.split(" ")
                number = int(number)
                if number > rules[color]:
                    is_possible = False
                    break
        if is_possible:
            sum_correct_ids += game_id
    return sum_correct_ids


def part_2(filename):
    games = get_input(filename)

    sum_powers = 0

    for game in games:
        is_possible = True
        game = game.strip()
        game_id, game_moves = game.split(":")
        game_id = int(game_id.replace("Game ", ""))

        min_cubes = {}
        for move in game_moves.split(";"):
            for cubes in move.strip().split(","):
                cubes = cubes.strip()
                number, color = cubes.split(" ")
                number = int(number)
                if color in min_cubes:
                    min_cubes[color] = max(min_cubes[color], number)
                else:
                    min_cubes[color] = number
        powers = 1
        for value in min_cubes.values():
            powers *= value
        sum_powers += powers
    return sum_powers


assert part_1("test_input_2", RULES_1) == 8

print("Part 1:", part_1("input_2", RULES_1))

assert part_2("test_input_2") == 2286

print("Part 2:", part_2("input_2"))
