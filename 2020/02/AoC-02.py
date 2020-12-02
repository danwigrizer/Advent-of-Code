import fileinput


def input_data():
    data = [str.strip(line, '\n') for line in fileinput.input("AoC-02-Input")]
    return data


def part_one(data):
    total_valid = 0
    for line in data:
        split_line = str.split(line, ": ")
        rule = str.strip(split_line[0])
        rule_number_criteria = str.split(rule)[0]
        rule_letter = rule[-1]
        password = str.strip(split_line[1])
        rule_minimum = int(str.split(rule_number_criteria, "-")[0])
        rule_maximum = int(str.split(rule_number_criteria, "-")[1])
        count_value_occurrences = password.count(rule_letter)
        if rule_minimum <= count_value_occurrences <= rule_maximum:
            total_valid += 1

    return total_valid

def part_two(data):
    total_valid = 0
    for line in data:
        split_line = str.split(line, ": ")
        rule = str.strip(split_line[0])
        rule_number_criteria = str.split(rule)[0]
        rule_letter = rule[-1]
        password = str.strip(split_line[1])
        rule_first_index = int(str.split(rule_number_criteria, "-")[0])
        rule_second_index = int(str.split(rule_number_criteria, "-")[1])
        letter_first_index = password[rule_first_index-1]
        letter_second_index = password[rule_second_index-1]
        indexes = [letter_first_index, letter_second_index]

        if indexes.count(rule_letter) == 1:
            total_valid += 1

    return total_valid


def test_part_one():
    test_input = [
        '1-2 t: ttttkdx',
        '2-4 f: cfkmf',
        '5-5 m: mmmmm',
        '5-12 a: abadbailaa',
        '10-11 b: tbdopoine',
        '1-3 b: popjopdqp',
    ]
    assert part_one(test_input) == 3


def test_part_two():
    test_input = [
        '1-2 t: tt',
        '1-2 f: tft',
        '1-4 a: bcdadf',
    ]
    assert part_two(test_input) == 2



if __name__ == '__main__':
    test_part_one()
    test_part_two()
    data = input_data()
    print(f'Part One:{part_one(data)}')
    print(f'Part Two:{part_two(data)}')
