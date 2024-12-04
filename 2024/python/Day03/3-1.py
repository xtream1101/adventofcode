import os
import sys
import re
from rich import print


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read()
    return lines


def run(data):
    total_val = 0
    regex = r"mul\((\d{1,3}),(\d{1,3})\)"

    matches = re.findall(regex, data)
    for match in matches:
        total_val += int(match[0]) * int(match[1])

    return total_val


test_ans = run(load_input("test_input_1.txt"))
print(test_ans)
assert test_ans == 161

ans = run(load_input("input.txt"))
assert ans == 168539636
print(ans)
