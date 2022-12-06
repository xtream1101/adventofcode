import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines[0]


def run(signal):
    for i in range(len(signal)):
        marker = signal[i:i+4]
        if len(marker) == len(set(marker)):
            return i+4


test_ans = run('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
print(test_ans)
assert test_ans == 7

test_ans = run('bvwbjplbgvbhsrlpgdmjqwftvncz')
print(test_ans)
assert test_ans == 5

ans = run(load_input('input.txt'))
assert ans == 1480
print(ans)
