import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        signals = f.read().splitlines()
    return signals


def run(signals):
    total_count = 0
    for signal in signals:
        _, output_values = signal.split('|')
        for digit in output_values.split():
            if len(digit) in (2, 4, 3, 7):
                total_count += 1
    return total_count


test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 26

ans = run(load_input('input.txt'))
assert ans == 421
print(ans)
