import logging
import re



def get_data():
    file = open("AoC-08-Input.txt", "r")
    lines = [ [x[:3].strip(), int(x[3:].strip())] for x in file.readlines()]
    return lines

current_line = 0
accumulator = 0
past_instructions = []


def program_p1(lines, accumulator, current_line):
        inst = lines[current_line]
        value = inst[1]
        lenh = len(lines) - 1
        if not current_line in past_instructions:
            if not current_line >= lenh:
                if inst[0] == 'acc':
                    past_instructions.append(current_line)
                    accumulator += value
                    current_line += 1
                    program_p1(lines, accumulator, current_line)
                if inst[0] == 'jmp':
                    past_instructions.append(current_line)
                    current_line += value
                    program_p1(lines, accumulator, current_line)
                if inst[0] == 'nop':
                    past_instructions.append(current_line)
                    current_line += 1
                    program_p1(lines, accumulator, current_line)
            else:
                print(accumulator)
       # comment out for part one
        else:
            print(accumulator)


tmp = []
def part_two():
    new = list(get_data())

    for idx, x in enumerate(new):
        if 'jmp' in x:
            j = get_data()
            j[idx][0] = 'nop'
            tmp.append(j)
        if 'nop' in x and 0 not in x:
            n = get_data()
            n[idx][0] = 'jmp'
            tmp.append(n)


# PART ONE
# d = list(get_data())
# program_p1(d,  accumulator, current_line)

## PART TWO
part_two()
for t in tmp:
    past_instructions = []
    program_p1(t, accumulator, current_line)