import math

def input_data():
    lines = open("AoC-03-input.txt")
    data = [str.strip(line) for line in lines]
    return data


def part_one(data):
    x = 0
    trees = 0
    for line in data:
        multi = int(x / len(line))+1
        new_line = line * multi
        trees += new_line[x] == '#'
        x += 3
    return trees


def part_two(data):
    trees_list = []
    slope = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]
    for slope in slope:
        x, y = 0, 0
        s_x, s_y = slope
        trees = 0
        for idx, line in enumerate(data):
            multi = int(x / len(line)) + 1
            new_line = line * multi
            if idx == y:
                trees += new_line[x] == '#'
                y += s_y
                x += s_x
        trees_list.append(trees)
    return math.prod(trees_list)


def test():
    test_input = [
        '..##.......',
        '#...#...#..',
        '.#....#..#.',
        '..#.#...#.#',
        '.#...##..#.',
        '..#.##.....',
        '.#.#.#....#',
        '.#........#',
        '#.##...#...',
        '#...##....#',
        '.#..#...#.#'
    ]

    assert part_two(test_input) == 336
    assert part_one(test_input) == 7


if __name__ == '__main__':
    test()
    d = input_data()
    print(part_two(d))

