import math

def get_data():
    file = open("AoC-10-Input.txt", "r")
    adapter_list = [int(x.strip()) for x in file.readlines()]
    return adapter_list

def get_updated_list():
    data = get_data()
    sort = sorted(data)
    max = sort[-1]+3
    sort.append(max)
    return sort

def part_one(data):
    list_diff = []
    new_list = []
    current_value = 0
    total_paths = []
    for i in range(len(data)):
        next_values = [option for option in data if current_value+1 <= option <=  current_value+3]
        selection = min(next_values)
        # if len(next_values) == 1:
        #     total_paths.append(current_value)
        difference = selection - current_value
        current_value = selection
        list_diff.append(difference)


    one = list_diff.count(1)
    three = list_diff.count(3)+1
    answer = one * three
    return list_diff

data = get_updated_list()
diffs = (part_one(get_updated_list()))

def part_one_answer():
    threes = diffs.count(3)
    ones = diffs.count(1)
    return threes * ones

def find_split_points():
    spl = []
    values = [25,50,75]
    for x in values:
        i = diffs.index(3,x)
        spl.append(i)

    s_1 = (0, data[:spl[0]+1])
    s_2 = (data[spl[0]], data[spl[0]+1: spl[1]+1])
    s_3 = (data[spl[1]], data[spl[1]+1: spl[2]+1])
    s_4 = (data[spl[2]], data[spl[2]+1:])
    # s_1 = (0,data[:46])
    # s_2 = (data[45], data[46:78])
    # s_3 = (data[77], data[78:])
    return [s_1,s_2,s_3,s_4]

print(find_split_points())
ls = 0
def part_three(data, current_value, max):
    global ls
    next_values = [option for option in data if current_value+1 <= option <=  current_value+3]
    for x in next_values:
        if max in next_values:
            ls += 1
        part_three(data, x, max)
    # print(ls)

def get_part_two():
    list = find_split_points()
    list_of_results = []
    for x in list:
        "new"
        part_three(x[1], x[0], x[1][-1])
        list_of_results.append(ls)
    return list_of_results

def final_values():
    ans = get_part_two()
    answers = []
    for idx,x in enumerate(ans):
        if  idx == 0:
            answers.append(x)
        else:
            answers.append(x - ans[idx-1])
    return math.prod(answers)

print(final_values())
print(part_one_answer())

"""
Question:
Any given adapter can take an input 1, 2, or 3 jolts lower than its rating and still produce its rated output joltage.
3 pts higher than max in bag
If you use every adapter in your bag at once, what is the distribution of joltage differences between the charging outlet, the adapters, and your device?

Every input must be between 1-3 lower than value
However, in order to not skip any adapters,

Find the chain that uses all of your adapters
1 jolt diff x 3

Jolt = Value + Next Value(Min[Value+1, Value+2, Value+3])
diff = Next Value - Value

Value
Next Value Poss = [X for x in adapter list if value+1 <= x <= value+3

152
"""