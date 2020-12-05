"""
Rows = 127
F = Front half
B = Back Half

Columns = 7
R= Upper Half
L= Lower half

multiply row by 8 then add column

highest seat id
"""
import math

data = open("AoC-05-Input", "r")
seat_id = []
all_seats = [x * 8 + c for c in range(0, 8) for x in range(0, 128)]
# all_seats_tuple = [(x, c) for c in range(0, 8) for x in range(0, 128)]


def part_one():
    for line in data:
        ticket = line.strip()
        row, column = ticket[:7], ticket[7:]
        r_final, c_final = 0, 0
        r_range = (0, 127)
        c_range = (0, 7)

        for idx, r_value in enumerate(row):
            if idx < 6:
                if r_value == 'F':
                    r_range = (r_range[0], r_range[0]+(r_range[1]-r_range[0])//2)
                    # print(r_value, r_range)
                elif r_value == 'B':
                    r_range = (math.ceil(r_range[0]+(r_range[1]-r_range[0])/2), r_range[1])
                    # print(r_value,r_range)
            else:
                if r_value == 'F':
                    r_final += r_range[0]
                elif r_value == 'B':
                    r_final += r_range[1]

        for idx, c_value in enumerate(column):
            if idx < 2:
                if c_value == 'L':
                    c_range = (c_range[0], c_range[0]+(c_range[1]-c_range[0])//2)
                    # print(c_value, c_range)
                elif c_value == 'R':
                    c_range = (math.ceil(c_range[0]+(c_range[1]-c_range[0])/2), c_range[1])
                    # print(c_value, c_range)
            else:
                if c_value == 'L':
                    c_final += c_range[0]
                elif c_value == 'R':
                    c_final += c_range[1]
        # print(r_final, c_final, (r_final * 8 + c_final))
        seat_id.append(r_final * 8 + c_final)
    return max(seat_id)


def part_two():
    return [x for x in all_seats if x not in seat_id and x+1 in seat_id and x-1 in seat_id][0]


print(part_one())
print(part_two())

