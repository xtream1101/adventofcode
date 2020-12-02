import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        report = f.read().splitlines()
    return report


def run(lines):
    total_valid = 0
    for line in lines:
        idx_1, idx_2 = line.split(' ')[0].split('-')
        idx_1 = int(idx_1)
        idx_2 = int(idx_2)
        letter = line.split(' ')[1][:-1]
        password = line.split(': ')[-1]
        # print(password[idx_1-1], letter, password[idx_2-1], letter)
        match = 0
        if password[idx_1-1] == letter:
            match += 1
        if password[idx_2-1] == letter:
            match += 1
        if match == 1:
            total_valid += 1

    return total_valid


test_ans = run(load_input('test_input.txt'))
assert test_ans == 1

ans = run(load_input('input.txt'))
assert ans == 360

print(ans)
