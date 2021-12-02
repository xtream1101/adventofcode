import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        commands = f.read().splitlines()
    return commands


def run(commands):
    h_pos = 0
    d_pos = 0
    aim = 0
    for cmd in commands:
        direction, value = cmd.split(' ')
        value = int(value)

        if direction == 'forward':
            h_pos += value
            d_pos += aim * value
        elif direction == 'up':
            aim -= value
        elif direction == 'down':
            aim += value

    return h_pos * d_pos


test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 900

ans = run(load_input('input.txt'))
assert ans == 1965970888

print(ans)
