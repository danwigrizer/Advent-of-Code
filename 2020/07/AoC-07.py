# Recursive solution.

import re

debug = False
if debug == True:
    data = open("AoC-07-Input-Test.txt", "r")
else:
    data = open("AoC-07-Input.txt", "r")

data_lines = [x.strip() for x in data.readlines()]

# Part One
def data_p1():
    list = []
    dict_colors = {}
    for x in data_lines:
        ls = []
        for x in re.findall('(\D*).(?=bag)', x):
            ls.append(x.strip())
        if not len(ls) == 1:
            dict_colors[ls[0]]=ls[1:]
    return(dict_colors)


def find_colors(color, dict_colors, list):
    for k, v in dict_colors.items():
        if color in v:
            list.append(k)
            find_colors(k,dict_colors,list)

def part_one():
    gold = []
    dic = data_p1()
    find_colors('shiny gold',dic,gold)
    part_one = len(set(gold))
    return (part_one)

#Part two
def data_p2():
    list = []
    dict_colors_p2 = {}
    for x in data_lines:
        ls = []
        lt = []
        for y in re.findall('(\D*|\d\D*).(?=bag)', x):
            tcolor = y.strip()
            if re.search('\d', tcolor):
                color = str(re.search('\D\S.(\D+)', tcolor)[0])
                bags = int(re.search('\d', tcolor)[0])
                newv = (str(color.strip()+",") * bags).strip().split(",")
                for x in newv:
                    if x:
                        lt.append(x)
            ls.append(tcolor)
        if not len(ls) == 1:
            dict_colors_p2[ls[0]]=lt
    return(dict_colors_p2)

def find_color_values(color, dict_colors, ans):
    for main_color, subcolors in dict_colors.items():
        if main_color == color:
            for subcolor in subcolors:
                ans.append(1)
                find_color_values(subcolor, dict_colors,ans)

ans = []
find_color_values('shiny gold',data_p2(), ans)
print(len(ans))

