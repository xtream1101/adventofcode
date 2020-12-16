import os
import re
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        data = f.read().splitlines()
    # return list(map(int, data))
    return data


def run(notes):
    invalid_numbers = []
    rules = []
    section_number = 0
    for row in notes:
        if row == '':
            section_number += 1
            continue

        if section_number == 0:
            m = re.search(r'(\d+-\d+) or (\d+-\d+)', row)
            a = m.group(1).split('-')
            b = m.group(2).split('-')
            rules.append((int(a[0]), int(a[1])))
            rules.append((int(b[0]), int(b[1])))

        elif section_number == 1:
            # your ticket
            pass

        elif section_number == 2 and row != 'nearby tickets:':
            # print(rules, row)
            for num in map(int, row.split(',')):
                found_match = False
                for rule in rules:
                    if num >= rule[0] and num <= rule[1]:
                        found_match = True
                        break
                if found_match is False:
                    invalid_numbers.append(num)

    return sum(invalid_numbers)


test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 71

ans = run(load_input('input.txt'))
print(ans)
assert ans == 19087

try:
    from aocd import submit
    submit(ans, part="a", day=16, year=2020)
except ModuleNotFoundError:
    print("Answer did not auto submit")
