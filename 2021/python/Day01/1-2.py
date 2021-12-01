import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return list(map(int, lines))


def run(report):
    prev_sum = None
    inc = 0
    for idx, _ in enumerate(report[:-2]):

        if prev_sum is None:
            prev_sum = sum(report[idx:idx+3])
            continue

        cur_sum = sum(report[idx:idx+3])
        # print(i, prev_sum, cur_sum, prev_sum < cur_sum)
        if prev_sum < cur_sum:
            inc += 1
        prev_sum = cur_sum

    return inc


test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 5

ans = run(load_input('input.txt'))
assert ans == 1600

print(ans)
