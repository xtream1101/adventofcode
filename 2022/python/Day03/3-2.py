import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return list(lines)


def run(sacks):
    dup_items = []
    group_items = []
    for items in sacks:
        group_items.append(items)

        if len(group_items) != 3:
            continue

        shared_item = list(set(group_items[0]).intersection(group_items[1], group_items[2]))[0]
        dup_items.append(shared_item)
        group_items = []

    total_sum = 0
    for item in dup_items:
        if item <= 'Z':
            total_sum += ord(item)-65+26+1
        else:
            total_sum += ord(item)-97+1
    return total_sum


test_ans = run(load_input('test_input.txt'))
print(test_ans)
assert test_ans == 70

ans = run(load_input('input.txt'))
assert ans == 2602
print(ans)
