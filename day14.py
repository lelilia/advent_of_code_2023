from utils import get_input, print_map
import numpy as np

TEST_INPUT = "test_input_14"
INPUT = "input_14"


class Map:
    def __init__(self, file):
        self.map = self.generate_map(file)
        self.shape = self.map.shape
        self.cubes = self.get_stones("#")
        self.rocks = self.get_stones("O")

    def __repr__(self):
        return "\n".join(["".join(row) for row in self.map])

    def generate_map(self, file):
        map_input = get_input(file)
        return np.array(
            [np.array([x for x in row.strip()]) for row in map_input.split("\n")]
        )

    def get_stones(self, shape):
        positions = list(zip(*np.where(self.map == shape)))
        return dict(zip(positions, [True] * len(positions)))

    def get_load(self):
        load = 0
        for rock in self.rocks.keys():
            load += self.shape[0] - rock[0]
        return load

    def full_rotation(self):
        self.rotate_north()
        self.rotate_west()
        self.rotate_south()
        self.rotate_east()

    def rotate_north(self):
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if (i, j) in self.rocks:
                    di = 0
                    while (
                        i - (di + 1) >= 0
                        and (i - (di + 1), j) not in self.rocks
                        and (i - (di + 1), j) not in self.cubes
                    ):
                        di += 1
                    del self.rocks[(i, j)]
                    self.rocks[(i - di, j)] = True

    def rotate_west(self):
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if (i, j) in self.rocks:
                    dj = 0
                    while (
                        j - (dj + 1) >= 0
                        and (i, j - (dj + 1)) not in self.rocks
                        and (i, j - (dj + 1)) not in self.cubes
                    ):
                        dj += 1
                    del self.rocks[(i, j)]
                    self.rocks[(i, j - dj)] = True

    def rotate_south(self):
        for i in range(self.shape[0] - 1, -1, -1):
            for j in range(self.shape[1]):
                if (i, j) in self.rocks:
                    di = 0
                    while (
                        i + (di + 1) < self.shape[0]
                        and (i + (di + 1), j) not in self.rocks
                        and (i + (di + 1), j) not in self.cubes
                    ):
                        di += 1
                    del self.rocks[(i, j)]
                    self.rocks[(i + di, j)] = True

    def rotate_east(self):
        for i in range(self.shape[0]):
            for j in range(self.shape[1] - 1, -1, -1):
                if (i, j) in self.rocks:
                    dj = 0
                    while (
                        j + (dj + 1) < self.shape[1]
                        and (i, j + (dj + 1)) not in self.rocks
                        and (i, j + (dj + 1)) not in self.cubes
                    ):
                        dj += 1
                    del self.rocks[(i, j)]
                    self.rocks[(i, j + dj)] = True

    def print_current_map(self):
        map = np.full(self.shape, ".")
        for x, y in self.cubes.keys():
            map[x, y] = "#"
        for x, y in self.rocks.keys():
            map[x, y] = "O"
        print_map(map)
        print()


def part_1(file):
    map = Map(file)
    map.rotate_north()
    return map.get_load()


def part_2(file):
    map = Map(file)
    seen = {}
    loads = {}
    for i in range(1, 1000000001):
        map.full_rotation()
        rocks = "-".join([f"{x},{y}" for x, y in sorted(list(map.rocks.keys()))])
        if rocks in seen:
            break
        seen[rocks] = i
        loads[i] = map.get_load()
    return loads[(1000000000 - seen[rocks]) % (i - seen[rocks]) + (seen[rocks])]


if __name__ == "__main__":

    assert (result := part_1(TEST_INPUT)) == 136, f"Expected 136, got {result}"
    print("Part 1:", part_1(INPUT))

    assert (part_2(TEST_INPUT)) == 64
    print("Part 2:", part_2(INPUT))
