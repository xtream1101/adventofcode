import os
import sys
import re


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        report = f.read().splitlines()
    return report


child_pattern = re.compile(r"(?P<count>\d+) (?P<child>.+?) bags?")


def run(rules):
    bags = {}
    for idx, rule in enumerate(rules):

        parent, children = rule.split(' bags contain ')
        bags[parent] = []
        for child_match in re.finditer(child_pattern, children):
            bags[parent].append((
                child_match.group('child'),
                child_match.group('count'),
            ))

    return bag_count(bags, 'shiny gold') - 1


def bag_count(bags, name, count=1):
    total_count = int(count)
    for bag in bags[name]:
        total_count += bag_count(bags, bag[0], int(bag[1])) * count

    return total_count


test_ans = run(load_input('test_input.txt'))
assert test_ans == 32

test_ans = run(load_input('test_input_2.txt'))
# print(test_ans)
assert test_ans == 126

ans = run(load_input('input.txt'))
assert ans == 48160

print(ans)
