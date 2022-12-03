import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return list(lines)


def run(sacks):
    dup_items = []
    for items in sacks:
        half_idx = int(len(items) / 2)
        first_half = items[:half_idx]
        sec_half = items[half_idx:]
        dup_items.append(list(set(first_half).intersection(sec_half))[0])

    total_sum = 0
    for item in dup_items:
        if item <= 'Z':
            total_sum += ord(item) - 65 + 26 + 1
        else:
            total_sum += ord(item) - 97 + 1
    return total_sum


test_ans = run(load_input('test_input.txt'))
print(test_ans)
assert test_ans == 157

ans = run(load_input('input.txt'))
assert ans == 7990
print(ans)
