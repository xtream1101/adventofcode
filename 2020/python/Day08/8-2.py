import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        report = f.read().splitlines()
    return report


def run(boot_code):

    changes = set()
    done = False
    while done is not True:
        accumulator = 0
        idx = 0
        change_made = False
        used_idxs = set()
        while True:
            if idx in used_idxs:
                break
            try:
                cmd, value = boot_code[idx].split(' ')
            except IndexError:
                done = True
                break
            value = int(value)

            used_idxs.add(idx)
            if change_made is False and idx not in changes and cmd in ('jmp', 'nop'):
                cmd = 'jmp' if cmd == 'nop' else 'nop'
                changes.add(idx)
                change_made = True

            # print(idx, cmd, value, change_made)
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
assert test_ans == 8

ans = run(load_input('input.txt'))
assert ans == 1245

print(ans)
