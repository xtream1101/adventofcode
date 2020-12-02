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
        min_count, max_count = line.split(' ')[0].split('-')
        min_count = int(min_count)
        max_count = int(max_count)
        letter = line.split(' ')[1][:-1]
        password = line.split(': ')[-1]
        letter_count = password.count(letter)
        # print(password, letter, min_count, max_count, letter_count)
        if letter_count >= min_count and letter_count <= max_count:
            total_valid += 1

    return total_valid


test_ans = run(load_input('test_input.txt'))
assert test_ans == 2

ans = run(load_input('input.txt'))
assert ans == 542

print(ans)
