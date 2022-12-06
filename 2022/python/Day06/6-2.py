import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines[0]


def run(signal):
    for i in range(len(signal)):
        marker = signal[i:i+14]
        if len(marker) == len(set(marker)):
            return i+14


test_ans = run('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
print(test_ans)
assert test_ans == 19

test_ans = run('bvwbjplbgvbhsrlpgdmjqwftvncz')
print(test_ans)
assert test_ans == 23

ans = run(load_input('input.txt'))
assert ans == 2746
print(ans)
