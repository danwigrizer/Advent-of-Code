import re

def data():
    file = open("AoC-12-Input.txt")
    lines = [x.strip() for x in file.readlines()]
    d = [(re.search("\D", x)[0],int(re.search("\d+", x)[0])) for x in lines]
    return d

def travel():
    ew, ns = 0,0
    facing = ['E', 'S', 'W', 'N']
    current_facing = 'E'

    for d, l in data():
        if d == 'N':
            ns += l
        elif d == "S":
            ns += -l
        elif d == "E":
            ew += l
        elif d == "W":
            ew += -l
        elif d == "L":
            turns = - l / 90
            current_facing = facing[int(facing.index(current_facing) + turns) % 4]
        elif d == 'R':
            turns = l / 90
            current_facing = facing[int(facing.index(current_facing) + turns) % 4]
        elif d == 'F':
            if current_facing == 'E':
                ew += l
            elif current_facing == 'N':
                ns += l
            elif current_facing == 'W':
                ew += -l
            elif current_facing == 'S':
                ns += -l

    print(abs(ew) + abs(ns))

# travel()
way_x, way_y = 10, 1
def waypoint():
    way_x, way_y = 10, 1
    boat_x, boat_y = 0,0

    change = []
    for d, l in data():
        facing = [(way_x, way_y), (way_y, -way_x), (-way_x, -way_y), (-way_y, way_x)]
        if d == 'N':
            way_y += l
        elif d == "S":
            way_y += -l
        elif d == "E":
            way_x += l
        elif d == "W":
            way_x += -l
        if d == "L":
            turns = - l / 90
            current_facing = facing[(0 + int(turns)) % 4]
            way_x, way_y = current_facing
        if d == "R":
            turns = l / 90
            current_facing = facing[(0 + int(turns)) % 4]
            way_x, way_y = current_facing
        if d == "F":
            boat_x += (l * way_x)
            boat_y += (l * way_y)
    print(abs(boat_x) + abs(boat_y))

travel()
waypoint()

