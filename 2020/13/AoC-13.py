import fileinput
import copy
from math import prod


file = [x.strip() for x in fileinput.input("AoC-13-Input.txt")]
earliest_time = int(file[0])
b = file[1].split(',')
buses_one = [int(x) for x in b if not x == 'x']

lines = list(fileinput.input("AoC-13-Input.txt"))
t = lines[1].strip().split(',')
times = [(int(y),-x) for x,y in enumerate(t) if y != 'x']

N = prod(time for time, _ in times)
time = 0
for m, bi in times:
    Ni = N // m
    xi = Ni ** (m - 2) % m
    time += bi * Ni * xi
    print("bi", bi, "Ni", Ni, "mi", xi, "prod", m, "time", time)
print(time % N)


# ** Part One **
times = []
for bus in buses_one:
    time = 0
    while time < earliest_time:
        time += bus
    times.append((time-earliest_time, bus))
times.sort()
print(times)

# Brute force part two
def find_value(num, remainders, k):
    x = 1
    while True:
        right_answers = 0
        while right_answers < k:
            # getting the index of already correct answers will get us
            # the next number in the list
            if  (x-num[right_answers]) % num[right_answers] != (remainders[right_answers]):
                break
            right_answers += 1
        if right_answers == k:
            return x
        x += 1
lee = len(times)
# print(find_value(n, r, lee ))
