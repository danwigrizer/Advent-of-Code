import itertools
import fileinput
import math


def get_input():
    return [int(line) for line in fileinput.input("AoC-01-Input")]

# Part 1


def part_one(input_data):
    for val in itertools.combinations(input_data, 2):
        if sum(val) == 2020:
            return math.prod(val)

# Part 2


def part_two(input_data):
    for val in itertools.combinations(input_data, 3):
        if sum(val) == 2020:
            return math.prod(val)


def test():
    test_input = [1, 2019, 5, 2014]
    assert part_one(test_input) == 2019
    assert part_two(test_input) == 10070


if __name__ == '__main__':
    test()
    v = get_input()
    print(f'part one: {part_one(v)}')
    print(f'part two: {part_two(v)}')

