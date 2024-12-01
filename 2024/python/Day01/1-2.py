import os
import sys
from rich import print


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(data):
    total_val = 0
    l1 = []
    l2 = []

    for i in data:
        a, b = map(int, i.split())
        l1.append(a)
        l2.append(b)

    for loc in l1:
        total_val += loc * l2.count(loc)

    return total_val


test_ans = run(load_input("test_input.txt"))
print(test_ans)
assert test_ans == 31

ans = run(load_input("input.txt"))
assert ans == 20520794
print(ans)
