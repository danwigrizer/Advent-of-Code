"""
- the next number must be the sum of two of those numbers:
- the two numbers in the pair must be different.
- 26th number must be the sum of two distinct numbers from the prior 25 numbers
"""
import itertools

def data():
    fl = open("AoC-09-Input.txt", "r")
    values = [int(x.strip()) for x in fl.readlines()]
    return values

def part_one(values):

    for i in range(25, len(values)):
        preamble = values[i-25:i]
        all_combos = list(itertools.combinations(preamble,2))
        if values[i] not in [x+y for x,y in all_combos]:
            return (values[i])

def part_two(v, number):

    for i in range(len(v)):
        # print(v[i])
        ans = v[i]
        ans_array = [v[i]]
        loc = i
        for value in v[i+1:]:
            while ans < number:
                loc += 1
                ans += v[loc]
                ans_array.append(v[loc])
                # print(v[i], ans_array, ans)
                if ans == number:
                        #1212510616:
                    return (min(ans_array) + max(ans_array))


data = data()
number = part_one(data)

print(part_one(data))
print(part_two(data,number))