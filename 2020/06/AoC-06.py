"""
count the number of questions to which anyone answered "yes"

Each group is seperated by a blank line.

"""

file = open("AoC-06-Input.txt", "r", newline="\r\n")
d = file.readlines()

#part one:
data = [x.strip() for x in d][0].split("\n\n")
dat2 = [len(set(x.replace('\n',''))) for x in data]
# print(sum(dat2))

#part two
dat3 = [x.replace('\n','') for x in data]
dat4 = [set(x) for x in dat3]

file2 = open("AoC-06-Input.txt", "r").readlines()
fil2 = [x.strip() for x in file2]
ls, l = [], []
for x in fil2:
    if x:
        l.append(x)
    else:
        ls.append(l)
        l = []
ls.append(l)

answer = 0
for idx, x in enumerate(ls):
    people = len(x)
    for letter in dat4[idx]:
        total = dat3[idx].count(letter)
        answer += total == people


print(answer)
