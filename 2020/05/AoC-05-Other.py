# print(max([int(x.strip().replace("F","0").replace("L","0").replace("B","1").replace("R","1"),2) for x in open("input.txt").readlines()]))

y = open("AoC-05-Input").readlines()
y = [int(x.strip().replace("F", "0").replace("L", "0").replace("B", "1").replace("R", "1"), 2) for x in y]
print(max(y))