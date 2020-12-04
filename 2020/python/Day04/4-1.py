import os
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
            num_valid += 1

        current_passport = {}

    return num_valid


test_ans = run(load_input('test_input.txt'))
assert test_ans == 2

ans = run(load_input('input.txt'))
assert ans == 235

print(ans)
