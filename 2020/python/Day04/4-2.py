import os
import re
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        report = f.read().splitlines()
    return report


def run(passports):

    fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        # 'cid',
    ]
    num_valid = 0
    current_passport = {}
    for idx, passport in enumerate(passports):
        if passport != '':
            for data in passport.split(' '):
                field, value = data.split(':')
                current_passport[field] = value
            # If not the last line
            if len(passports) != idx + 1:
                continue

        if set(fields).issubset(set(current_passport.keys())):
            if (
                int(current_passport['byr']) >= 1920 and int(current_passport['byr']) <= 2002
                and int(current_passport['iyr']) >= 2010 and int(current_passport['iyr']) <= 2020
                and int(current_passport['eyr']) >= 2020 and int(current_passport['eyr']) <= 2030
                and current_passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
                and re.match(r'^#[0-9a-f]{6}$', current_passport['hcl'])
                and re.match(r'^\d{9}$', current_passport['pid'])
                and ((current_passport['hgt'][-2:] == 'cm' and int(current_passport['hgt'][:-2]) >= 150 and int(current_passport['hgt'][:-2]) <= 193)
                     or (current_passport['hgt'][-2:] == 'in' and int(current_passport['hgt'][:-2]) >= 59 and int(current_passport['hgt'][:-2]) <= 76))
            ):
                num_valid += 1

        current_passport = {}

    return num_valid


test_ans = run(load_input('test_input2.txt'))
assert test_ans == 4

ans = run(load_input('input.txt'))
assert ans == 194
print(ans)
