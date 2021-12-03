import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        report = f.read().splitlines()
    return report


def run(report):
    # Pivot list to get counts faster
    report = list(map(list, zip(*report)))
    gamma_rate = ''
    total_len = len(report[0])

    for i in range(len(report)):
        ones_count = report[i].count('1')
        gamma_rate += '1' if ones_count > total_len/2 else '0'

    epsilon_rate = ''.join(['1' if i == '0' else '0' for i in gamma_rate])
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 198

ans = run(load_input('input.txt'))
assert ans == 1025636

print(ans)
