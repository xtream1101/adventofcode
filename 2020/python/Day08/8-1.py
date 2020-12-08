import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        report = f.read().splitlines()
    return report


def run(boot_code):
    accumulator = 0
    idx = 0
    used_idxs = set()
    while True:
        try:
            cmd, value = boot_code[idx].split(' ')
        except IndexError:
            break
        value = int(value)

        if idx in used_idxs:
            break
        used_idxs.add(idx)
        # print(idx, cmd, value)
        # a = input()  # Used to step through
        if cmd == 'acc':
            accumulator += value
        elif cmd == 'jmp':
            idx += value
            continue

        idx += 1

    return accumulator


test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 5

ans = run(load_input('input.txt'))
assert ans == 1420

print(ans)
