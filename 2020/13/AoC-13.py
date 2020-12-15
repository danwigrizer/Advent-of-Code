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

print(times)

def modInverse(a, m):
    a = a % m
    for x in range(1, m):
        if ((a * (x)) % m == 1):
            return x
    return 1
#

N = prod(time for time, _ in times)
time = 0
for m, bi in times:
    Ni = N // m
    xi = Ni ** (m - 2) % m
    time += bi * Ni * xi
    x = bi * Ni * xi
    print(bi, Ni, xi, x)
    # print("bi", bi, "Ni", Ni, "mi", xi, "prod", m, "time", time)
# print(time)
print(time % N)

values = []
tot = 0
for b, i  in times:
    # integers messed it up so had to floor this
    Ni = N // b
    mi = modInverse(Ni, b)
    v = i*Ni*mi
    print(i, Ni, mi, v)
    # print("i", i , "Ni", Ni, "mi", mi, "prod", b, "v", v)
    tot += v
# print(tot)
print(tot % N)

# ** Part One **
times = []
for bus in buses_one:
    time = 0
    while time < earliest_time:
        time += bus
    times.append((time-earliest_time, bus))
times.sort()

#
# n = []
# times = []
# # r = []
# N = 1
# for i,b in enumerate(times):
#     if b != 'x':
#         b = int(b)
#         i %= b
#         # r.append((b-idx)%b)
#         times.append(((b - i) % b, b))
#         N *= int(b)
#
# print(N)

# x = 0mod67
# n = 13mod2

def find_value(num, remainders, k):
    x = 1
    while True:
        right_answers = 0
        while right_answers < k:
            # getting the index of already correct answers will get us
            # the next number in the list
            if  (x-num[right_answers]) % num[right_answers] != (remainders[right_answers]):
            # if 0 != (x+remainders[right_answers])%num[right_answers]:
                break
            # print(num[right_answers] - x)
            # print(f'Number:{num[right_answers]} - X:{x}')
            right_answers += 1
        if right_answers == k:
            return x
        x += 1
# values time - remainder  = t0
# 41s time - 95 = to
lee = len(times)
# print(find_value(n, r, lee ))

# # x ≡ a mod p
# # x = remainder of a mod P
# # when you divide x / p it gives you remainder of a
# # X = 13a+2
# # x = 2 mod 13
# # X = 7b + 0
# # x = 2 mod 13
# # x = n13 + 2
#

def inv(a, m):
    m0 = m
    x0 = 0
    x1 = 1

    if (m == 1):
        return 0

    # Apply extended Euclid Algorithm
    while (a > 1):
        # q is quotient
        q = a // m
        # print(f'q:{q}')
        t = m
        # print(f't:{t}')
        # m is remainder now, process
        # same as euclid's algo
        m = a % m
        # print(f'm:{m}')
        a = t
        # print(f'a:{a}')
        t = x0
        # print(f't:{t}')
        x0 = x1 - q * x0
        # print(f'x0:{x1}{q}{x0}')
        x1 = t
        # print(f'x1:{x1}')
        # Make x1 positive
    if (x1 < 0):
        x1 = x1 + m0

    return x1
#
#
def modInverse(a, m):
    a = a % m
    for x in range(1, m):
        if ((a * (x)) % m == 1):
            return x
    return 1
#
#
# # Driver Code
# # Function call
# # print(modInverse(a, m, r))
#
values = []
tot = 0
for i, b in times:
    Ni = N / b
    mi = inv(Ni, b)
    print("inv", ind, "pp:", pp, "num", num, "r", i)
    v = i*mi*Ni
    tot += v
print(tot%int(N))

# print(r1)
# print(n)
# other_val = []
# m = math.prod(n)
# for idx, n in enumerate(n):
#     prodovernum = m/n
#     modofprod = prodovernum%n
#     v = prodovernum*modofprod*r[idx]
#     other_val.append(v)
# print(other_val)
# print(sum(other_val))
# print(sum(other_val)%m)


# m = 1
# end = False
# start = int(new_bus_list[0][0])
# N_DP = {}
# time = 0
# at_bus = 1
# while end is False:
#     ans = 0
#     an = []
#     for i in range(at_bus, len(newb)):
#         bus, diff = newb[i]
#         while not (int(bus) * m - diff) % start == 0:
#             m+=1
#         end = True
#         print(m*int(bus))



#
# r = offset
# find the greatest common divisor where
#
# find the number where 19/7 mod 7 = true
#

#
# DP = {}
# m = 1
# def dp(b,m):
#     if b == len(new_bus_list):
#         return 1
#     if b in DP[b]:
#         return DP[b]
#     start = int(new_bus_list[0][0])
#     bus, diff = newb[b]
#     while not (int(bus) * m - diff) % start == 0:
#         m += 1
#     print()
#
#
# dp(1,1)
        #
        #
        # print(newb[i], start)
        # bus, diff = newb[i]
        # y = int(bus) * m - diff
        # if y % start == 0:
        #     print()
        #     at_bus += 1
        #     ans += 1
        #     an.append(y)
        # else:
        #     m += 1
    # if ans == len(newb)-1:
    #     print(int(bus) * m - diff)

# def dp(t):
#     for bus in newb:
#         print(bus)
#         bus_interval, after_time = bus
#         print(bus_interval, after_time)
#         if t+int(after_time) % int(bus_interval) == 0:
#             t += 23
#             dp(t)
#         else:
#             print(t)
#