
def main():
    fin = open("AoC-04-Input", "r")
    lines = [ x.strip() for x in fin.readlines()]

    exp = ["pid", "ecl", "hcl", "hgt", "eyr", "iyr", "byr"]
    s = {}
    ans = 0
    for line in lines:
        if not line:
            print([x in line for x in exp], line)
        # chunks = line.split()
        # for c in chunks:
        #     k, v = c.split(":")
        #     s[k] = v
        #     print(s[k])



print(main())