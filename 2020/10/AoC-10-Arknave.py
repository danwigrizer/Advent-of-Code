from collections import *
from functools import lru_cache
import heapq
import itertools
import math
import random
import sys

def main():
    fin = open("AoC-10-Input-Test.txt", "r")
    xs = [int(line.strip()) for line in fin.readlines() if line.strip()]
    xs.sort()

    # List with 0 and last value +3
    xs = [0] + xs + [xs[-1] + 3]

    # Loop through the list and store last value
    last = 0

    #count of 1s and 3s
    a, b = 0, 0

    # #for values of xs
    # for x in xs:
    #
    #     # ensure current value is 3 above prior value
    #     assert x - last <= 3
    #
    #     # if diff is 1 a==1
    #     if x - last == 1:
    #         a += 1
    #
    #     # if diff is 3 a==3
    #     elif x - last == 3:
    #         b += 1
    #     last = x
    # print("part 1", a, b, a * b)

    dp = [1]
    print(dp)
    # for the number of values in xs
    for i in range(1, len(xs)):
        # ans = 0
        ans = 0
        # for the len of the values within i. Meaning, if we are at the fifth value, then
        # range from 1 through 5
        for j in range(i):
            print(f'{i},{j},{xs[j]},{xs[i]}')
            #if
            if xs[j] + 3 >= xs[i]:
                print(f'{xs[j] + 3}')
                ans += dp[j]
                print(dp)
        dp.append(ans)

    print("part 2", dp[-1])

if __name__ == "__main__":
    main()