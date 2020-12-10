import os
import sys

from collections import defaultdict


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        data = f.read().splitlines()
    return list(map(int, data))


def run(joltage):
    output = 0
    diff_count = defaultdict(lambda: 0)
    for _ in range(len(joltage)):
        # print(output)
        for i in (1, 2, 3):
            if output + i in joltage:
                diff_count[i] += 1
                joltage.remove(output + i)
                output += i
                break

    return diff_count[1] * (diff_count[3] + 1)


test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 35

test_ans = run(load_input('test_input_2.txt'))
# print(test_ans)
assert test_ans == 220

ans = run(load_input('input.txt'))
assert ans == 1656

print(ans)
