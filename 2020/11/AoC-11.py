"""
If seat is empty, and seat before and seat after are open, then fill
Seat is filled, and +4 & -4 are filled, then empty

"""
import itertools

def data():
    data = open('AoC-11-Input.txt', "r")
    lines = [ y.replace("#", '1').replace("L", '0').strip() for y in [x for x in data.readlines()]]
    return lines
lines = data()

#part one
def r(ls):
    neighbors = [ [-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1] ]
    new = []
    lines = list(ls)
    for row in range(len(lines)):
        new_row = []
        for seat in range(len(lines[row])):
            neighbor = []
            for x,y in neighbors:
                if 0 <= row + x < len(lines):
                    nrow = row + x
                    if 0 <= seat + y < len(lines[row]):
                        nseat = seat + y
                        neighbor.append(lines[nrow][nseat])
            if lines[row][seat] == '0' and not '1' in neighbor:
                new_row.append('1')

            elif lines[row][seat] == '1' and neighbor.count('1') >= 4:
                new_row.append('0')
            else:
                new_row.append(lines[row][seat])
        new.append(new_row)

    if list(itertools.chain.from_iterable(new)).count('1') == list(itertools.chain.from_iterable(lines)).count('1'):
        print(list(itertools.chain.from_iterable(new)).count('1'))
    else: r(new)

#part two
def r_two(ls):
    neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    new = []
    lines = list(ls)
    for row in range(len(lines)):
        new_row = []
        for seat in range(len(lines[row])):
            neighbor = []
            for n_row, n_seat in neighbors:
                for i in range(1, len(lines)):
                    x = i * n_row
                    y = i * n_seat
                    if 0 <= row + x < len(lines):
                        nrow = row + x
                        if 0 <= seat + y < len(lines[row]):
                            nseat = seat + y
                            if not lines[nrow][nseat] == '.':
                                neighbor.append(lines[nrow][nseat])
                                break

            if lines[row][seat] == '0' and not '1' in neighbor:
                new_row.append('1')

            elif lines[row][seat] == '1' and neighbor.count('1') >= 5:
                new_row.append('0')
            else:
                new_row.append(lines[row][seat])
        new.append(new_row)

    if list(itertools.chain.from_iterable(new)).count('1') == list(itertools.chain.from_iterable(lines)).count('1'):
        print(list(itertools.chain.from_iterable(new)).count('1'))
    else:
        r_two(new)

r(lines)
r_two(lines)



