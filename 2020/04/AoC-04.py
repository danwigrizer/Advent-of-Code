# Count passports with all non CID fields
# remove CID, if key count = 7
# if key count = 8 good, or key count = 7 && no CID.
import fileinput
import itertools
import re

def data(file):
    with open(file, newline='') as r:
        lines = r.read().split("\n\n")
        d_a = [x.split() for x in [x.replace("\n", " ") for x in lines]]
        dt = []
        for value in d_a:
            new_list = []
            for v in value:
                new_list.append(v[:3])
            dt.append(new_list)
        return dt


def part_one(data):
    count = 0
    c = data
    d = []
    for passp in c:
        if 'cid' in passp:
            passp.remove('cid')
        count += len(passp) == 7
    print(count)

"""

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

"""

def data_two():
    with open("AoC-04-Input", newline='') as r:
        lines = r.read().split("\n\n")
        d_a = [x.split() for x in [x.replace("\n", " ") for x in lines]]
        a_d = []
        for x in d_a:
            r = [l for l in x if 'cid' not in l]
            if len(r) == 7:
                a_d.append(r)
            # elif len(x) == 7:
            #     a_d.append(x)
            #     print(len(x))
        newl = []
        for x in a_d:
            dict = {l[:3]: l[4:] for l in x}

            if (    1920 <= int(dict['byr']) <= 2002
                    and 2010 <= int(dict['iyr']) <= 2020
                    and 2020 <= int(dict['eyr']) <= 2030
                    and re.search('[a-f0-9]{6}', dict['hcl'])
                    and len(dict['hcl']) == 7
                    and dict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                    and len(dict['ecl']) == 3
                    and re.search('\d{9}', dict['pid'])
                    and len(dict['pid']) == 9
            ):
                if re.search('in', dict['hgt']):
                    if 59 <= int(re.match('\d{2,3}(?=in)', dict['hgt'])[0]) <= 76:
                        newl.append(x)
                elif re.search('cm', dict['hgt']):
                    if 150 <= int(re.match('\d{2,3}(?=cm)', dict['hgt'])[0]) <= 193:
                        newl.append(x)
        print(len(newl))
                    # re.search('\d{2,3}(?=in|cm)', dict['hgt'])
                    # and (59 <= int(re.match('\d{2,3}', dict['hgt'])[0]) <= 76 or 150 <= int(re.match('\d{2,3}', dict['hgt'])[0]) <= 193)


                # print(re.match('\d{2,3}(?=in|cm)', dict['hgt'])[0])





data_two()


