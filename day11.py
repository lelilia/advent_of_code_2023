from utils import get_input, print_map
import numpy as np

TEST_INPUT = "test_input_11"
INPUT = "input_11"


def solve(file, expansion):
    raw_galaxies = get_input(file)
    galaxy_map = np.array(
        [np.array([x for x in row]) for row in raw_galaxies.split("\n")]
    )
    empty_cols = [i for i, x in enumerate(galaxy_map) if "#" not in galaxy_map[:, i]]
    empty_rows = [i for i, x in enumerate(galaxy_map) if "#" not in x]
    galaxies = np.where(galaxy_map == "#")
    distances = 0
    for i in range(len(galaxies[0])):
        for j in range(i + 1, len(galaxies[0])):
            x_1 = galaxies[0][i]
            x_2 = galaxies[0][j]
            y_1 = galaxies[1][i]
            y_2 = galaxies[1][j]

            distance = abs(x_1 - x_2) + abs(y_1 - y_2)
            for r in range(min(x_1, x_2) + 1, max(x_1, x_2)):
                if r in empty_rows:
                    distance += expansion - 1
            for c in range(min(y_1, y_2) + 1, max(y_1, y_2)):
                if c in empty_cols:
                    distance += expansion - 1
            distances += distance
    return distances


def part_1(file):
    return solve(file, 2)


def part_2(file, expansion=1000000):
    return solve(file, expansion)


if __name__ == "__main__":
    assert (result := part_1(TEST_INPUT)) == 374, f"Expected 374, got {result}"

    print("Part 1:", part_1(INPUT))

    assert (result := part_2(TEST_INPUT, 10)) == 1030, f"Expected 1030, got {result}"

    print("Part 2:", part_2(INPUT))
