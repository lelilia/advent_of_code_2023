"""
Advent of Code 2023
--- Day 5: If You Give A Seed A Fertilizer ---
"""
import re
from utils import get_input

INPUT = "input_5"
TEST_INPUT = "test_input_5"


class Item:
    def __init__(self, start, range):
        self.start = start
        self.range = range

    def __repr__(self) -> str:
        return f"<{self.start} -> {self.range}>"

    def __eq__(self, __value: object) -> bool:
        return self.start == __value.start and self.range == __value.range


class MapEntry:
    def __init__(self, map_string):
        digits = [int(x) for x in map_string.split(" ")]
        self.destination = digits[0]
        self.source = digits[1]
        self.range = digits[2]

    def __repr__(self) -> str:
        return f"<{self.destination}, {self.source}, {self.range}>"


def find_mapping(item, mappings):

    for mapping in mappings:
        if item in range(mapping.source, mapping.source + mapping.range + 1):
            return item - (mapping.source - mapping.destination)
    return item


def find_mapping_and_split(item, mappings):
    new_item = item
    check_again_items = []

    for mapping in mappings:
        # item     |-----|
        # mapping      |-----|
        if (
            item.start
            < mapping.source
            < item.start + item.range - 1
            < mapping.source + mapping.range - 1
        ):
            check_again_items.append(Item(item.start, mapping.source - item.start))
            new_item = Item(
                mapping.destination, item.range - (mapping.source - item.start)
            )

        # item          |-----|
        # mapping  |------|
        elif (
            mapping.source
            < item.start
            < mapping.source + mapping.range - 1
            < item.start + item.range - 1
        ):
            new_item = Item(
                item.start - (mapping.source - mapping.destination),
                mapping.source + mapping.range - item.start,
            )
            check_again_items.append(
                Item(
                    mapping.source + mapping.range,
                    item.range - (mapping.source + mapping.range - item.start),
                )
            )

        # item       |--|
        # mapping  |------|
        elif (
            mapping.source
            <= item.start
            <= item.start + item.range - 1
            <= mapping.source + mapping.range - 1
        ):
            new_item = Item(
                item.start - mapping.source + mapping.destination, item.range
            )

        # item    |-------|
        # mapping    |--|
        elif (
            item.start
            < mapping.source
            < mapping.source + mapping.range - 1
            < item.start + item.range - 1
        ):
            new_item = Item(mapping.destination, mapping.range)
            check_again_items.append(Item(item.start, mapping.source - item.start))
            check_again_items.append(
                Item(
                    mapping.source + mapping.range,
                    item.start + item.range - mapping.source - mapping.range,
                )
            )

    return new_item, check_again_items


def part_1(file):
    almanac = get_input(file).split("\n\n")

    item_list = re.findall(r"\d+", almanac[0])
    items = []
    for seed in item_list:
        items.append(int(seed))

    for map_part in almanac[1:]:
        map_list = re.findall(r"\d+\s\d+\s\d+", map_part)
        mappings = []
        for entry in map_list:
            mappings.append(MapEntry(entry))
        new_items = []
        for seed in items:
            new_items.append(find_mapping(seed, mappings))
        items = new_items

    return min(items)


def part_2(file):
    almanac = get_input(file).split("\n\n")

    seed_list = re.findall(r"\d+\s\d+", almanac[0])
    items = []
    for item in seed_list:
        item_start, item_range = [int(x) for x in item.split(" ")]
        items.append(Item(item_start, item_range))

    for map_part in almanac[1:]:
        map_list = re.findall(r"\d+\s\d+\s\d+", map_part)
        mappings = []
        for entry in map_list:
            mappings.append(MapEntry(entry))

        q = [item for item in items]
        new_items = []
        while q:
            curr = q.pop()
            new_item, add_to_q = find_mapping_and_split(curr, mappings)
            if new_item not in new_items:
                new_items.append(new_item)
            q += add_to_q

        items = [item for item in new_items]
    return min([x.start for x in items])


if __name__ == "__main__":
    assert (result := part_1(TEST_INPUT)) == 35, f"Expected 35 got {result}"
    print("Part 1:", part_1(INPUT))

    assert (result := find_mapping_and_split(Item(0, 10), [MapEntry("15 5 30")])) == (
        expected := (Item(15, 5), [Item(0, 5)])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(5, 10), [MapEntry("13 0 10")])) == (
        expected := (Item(18, 5), [Item(10, 5)])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(5, 10), [MapEntry("13 0 20")])) == (
        expected := (Item(18, 10), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(0, 30), [MapEntry("13 10 10")])) == (
        expected := (Item(13, 10), [Item(0, 10), Item(20, 10)])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(57, 13), [MapEntry("49 53 8")])) == (
        expected := (Item(53, 4), [Item(61, 9)])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(61, 9), [MapEntry("49 53 8")])) == (
        expected := (Item(61, 9), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(74, 3), [MapEntry("45 77 23")])) == (
        expected := (Item(74, 3), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(76, 1), [MapEntry("45 77 23")])) == (
        expected := (Item(76, 1), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(76, 1), [MapEntry("68 64 13")])) == (
        expected := (Item(80, 1), [])
    ), f"Expected {expected}, got {result}"

    assert (result := find_mapping_and_split(Item(79, 14), [MapEntry("50 98 2")])) == (
        expected := (Item(79, 14), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(79, 14), [MapEntry("52 50 48")])) == (
        expected := (Item(81, 14), [])
    ), f"Expected {expected}, got {result}"

    assert (result := find_mapping_and_split(Item(81, 14), [MapEntry("0 15 37")])) == (
        expected := (Item(81, 14), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(81, 14), [MapEntry("37 52 2")])) == (
        expected := (Item(81, 14), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(81, 14), [MapEntry("39 0 15")])) == (
        expected := (Item(81, 14), [])
    ), f"Expected {expected}, got {result}"

    assert (result := find_mapping_and_split(Item(81, 14), [MapEntry("49 53 8")])) == (
        expected := (Item(81, 14), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(81, 14), [MapEntry("0 11 42")])) == (
        expected := (Item(81, 14), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(81, 14), [MapEntry("42 0 7")])) == (
        expected := (Item(81, 14), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(81, 14), [MapEntry("57 7 4")])) == (
        expected := (Item(81, 14), [])
    ), f"Expected {expected}, got {result}"

    assert (result := find_mapping_and_split(Item(81, 14), [MapEntry("88 18 7")])) == (
        expected := (Item(81, 14), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(81, 14), [MapEntry("18 25 70")])) == (
        expected := (Item(74, 14), [])
    ), f"Expected {expected}, got {result}"

    assert (result := find_mapping_and_split(Item(74, 14), [MapEntry("45 77 23")])) == (
        expected := (Item(45, 11), [Item(74, 3)])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(74, 14), [MapEntry("81 45 19")])) == (
        expected := (Item(74, 14), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(74, 14), [MapEntry("68 64 13")])) == (
        expected := (Item(78, 3), [Item(77, 11)])
    ), f"Expected {expected}, got {result}"

    assert (result := find_mapping_and_split(Item(45, 11), [MapEntry("0 69 1")])) == (
        expected := (Item(45, 11), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(45, 11), [MapEntry("1 0 69")])) == (
        expected := (Item(46, 11), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(73, 3), [MapEntry("0 69 1")])) == (
        expected := (Item(73, 3), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(73, 3), [MapEntry("1 0 69")])) == (
        expected := (Item(73, 3), [])
    ), f"Expected {expected}, got {result}"

    assert (result := find_mapping_and_split(Item(46, 11), [MapEntry("60 56 37")])) == (
        expected := (Item(46, 11), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(46, 11), [MapEntry("56 93 4")])) == (
        expected := (Item(46, 11), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(73, 3), [MapEntry("60 56 37")])) == (
        expected := (Item(77, 3), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(73, 3), [MapEntry("56 93 4")])) == (
        expected := (Item(73, 3), [])
    ), f"Expected {expected}, got {result}"

    assert (result := find_mapping_and_split(Item(82, 1), [MapEntry("50 98 2")])) == (
        expected := (Item(82, 1), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(82, 1), [MapEntry("52 50 48")])) == (
        expected := (Item(84, 1), [])
    ), f"Expected {expected}, got {result}"

    assert (result := find_mapping_and_split(Item(84, 1), [MapEntry("0 15 37")])) == (
        expected := (Item(84, 1), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(84, 1), [MapEntry("37 52 2")])) == (
        expected := (Item(84, 1), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(84, 1), [MapEntry("39 0 15")])) == (
        expected := (Item(84, 1), [])
    ), f"Expected {expected}, got {result}"

    assert (result := find_mapping_and_split(Item(84, 1), [MapEntry("49 53 8")])) == (
        expected := (Item(84, 1), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(84, 1), [MapEntry("0 11 42")])) == (
        expected := (Item(84, 1), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(84, 1), [MapEntry("42 0 7")])) == (
        expected := (Item(84, 1), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(84, 1), [MapEntry("57 7 4")])) == (
        expected := (Item(84, 1), [])
    ), f"Expected {expected}, got {result}"

    assert (result := find_mapping_and_split(Item(84, 1), [MapEntry("88 18 7")])) == (
        expected := (Item(84, 1), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(84, 1), [MapEntry("18 25 70")])) == (
        expected := (Item(77, 1), [])
    ), f"Expected {expected}, got {result}"

    assert (result := find_mapping_and_split(Item(77, 1), [MapEntry("45 77 23")])) == (
        expected := (Item(45, 1), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(77, 1), [MapEntry("81 45 19")])) == (
        expected := (Item(77, 1), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(77, 1), [MapEntry("68 64 13")])) == (
        expected := (Item(77, 1), [])
    ), f"Expected {expected}, got {result}"

    assert (result := find_mapping_and_split(Item(45, 1), [MapEntry("0 69 1")])) == (
        expected := (Item(45, 1), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(45, 1), [MapEntry("1 0 69")])) == (
        expected := (Item(46, 1), [])
    ), f"Expected {expected}, got {result}"

    assert (result := find_mapping_and_split(Item(46, 1), [MapEntry("60 56 37")])) == (
        expected := (Item(46, 1), [])
    ), f"Expected {expected}, got {result}"
    assert (result := find_mapping_and_split(Item(46, 1), [MapEntry("56 93 4")])) == (
        expected := (Item(46, 1), [])
    ), f"Expected {expected}, got {result}"

    assert (result := part_2(TEST_INPUT)) == 46, f"Expected 46 got {result}"
    print("Part 2:", part_2(INPUT))
