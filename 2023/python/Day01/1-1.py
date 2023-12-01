import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(data):
    total = 0
    for line in data:
        num = ""
        for i in line:
            num += i if i.isdigit() else ""
        total += int(num[0] + num[-1])

    return total


test_ans = run(load_input("test_input_1.txt"))
print(test_ans)
assert test_ans == 142

ans = run(load_input("input.txt"))
assert ans == 54605
print(ans)
