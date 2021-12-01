import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return list(map(int, lines))


def run(report):
    prev_val = None
    inc = 0
    for idx, entry in enumerate(report):
        if prev_val is None:
            prev_val = entry
            continue
        # print(prev_val, entry, prev_val < entry)
        if prev_val < entry:
            inc += 1
        prev_val = entry

    return inc


test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 7

ans = run(load_input('input.txt'))
assert ans == 1559

print(ans)
