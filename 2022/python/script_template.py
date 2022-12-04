import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(data):
    total_val = 0

    return total_val


test_ans = run(load_input('test_input.txt'))
print(test_ans)
assert test_ans == 0000

ans = run(load_input('input.txt'))
# assert ans == 0000
print(ans)
