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
    check_bags = []
    bag_options = set()
    for idx, rule in enumerate(rules):
        parent, children = rule.split(' bags contain ')
        bags[parent] = []
        for child_match in re.finditer(child_pattern, children):
            child = child_match.group('child')
            bags[parent].append(child)
            if child == 'shiny gold':
                check_bags.append(parent)
                bag_options.add(parent)

    while check_bags:
        next_bag = check_bags.pop()
        for parent, child in bags.items():
            if next_bag in child:
                check_bags.append(parent)
                bag_options.add(parent)

    return len(bag_options)


test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 4

ans = run(load_input('input.txt'))
assert ans == 287

print(ans)
