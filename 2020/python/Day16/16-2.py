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
    rules = {}
    section_number = 0
    valid_tickets = []
    all_rules = []
    your_ticket = None
    for row in notes:
        if row == '':
            section_number += 1
            continue

        if section_number == 0:
            m = re.search(r'(.+?): (\d+-\d+) or (\d+-\d+)', row)
            a = list(map(int, m.group(2).split('-')))
            b = list(map(int, m.group(3).split('-')))
            rules[m.group(1)] = [(a[0], a[1]), (b[0], b[1])]
            all_rules.extend(rules[m.group(1)])

        elif section_number == 1 and row != 'your ticket:':
            your_ticket = list(map(int, row.split(',')))

        elif section_number == 2 and row != 'nearby tickets:':
            is_valid_ticket = True
            for num in map(int, row.split(',')):
                found_match = False
                for rule in all_rules:
                    if num >= rule[0] and num <= rule[1]:
                        found_match = True
                        break
                if found_match is False:
                    is_valid_ticket = False
            if is_valid_ticket is True:
                valid_tickets.append(row)

    # print(valid_tickets)
    valid_fields = {}
    # Add all index to each field
    for name in rules:
        valid_fields[name] = list(range(len(valid_tickets[0].split(','))))

    # print(valid_fields)
    for ticket in valid_tickets:
        ticket = ticket.split(',')
        for idx, num in enumerate(ticket):
            num = int(num)
            for name, rule in rules.items():
                passed = False
                for test in rule:
                    if num >= test[0] and num <= test[1]:
                        passed = True
                # If the valued failed all the tests, remove that index as the possible field
                if passed is False:
                    try:
                        valid_fields[name].remove(idx)
                    except ValueError:
                        pass
    # print(valid_fields)

    fields = {}
    loop = True
    while loop:
        loop = False
        for name, value in valid_fields.items():
            if name in fields:
                continue
            loop = True
            if len(value) == 1:
                fields[name] = value[0]
            else:
                for v in fields.values():
                    try:
                        value.remove(v)
                    except ValueError:
                        pass

    # print("fields")
    # print(fields)
    total = 1
    for field, idx in fields.items():
        # print(field, your_ticket[idx])
        if field.startswith('departure'):
            total *= your_ticket[idx]

    return total


test_ans = run(load_input('test_input_2.txt'))
# print(test_ans)

ans = run(load_input('input.txt'))
print(ans)
assert ans == 1382443095281

try:
    from aocd import submit
    submit(ans, part="b", day=16, year=2020)
except ModuleNotFoundError:
    print("Answer did not auto submit")
