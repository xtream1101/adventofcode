import os
import sys
import copy
from pprint import pprint


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        data = f.read().splitlines()

    for i, r in enumerate(data):
        data[i] = list(r)
    return data


def run(nav):

    directions = ('n', 'e', 's', 'w')
    direction = 'e'
    pos = {'x': 0, 'y': 0}
    for instruction in nav:
        action = instruction[0]
        value = int(''.join(instruction[1:]))

        if action == 'F':
            if direction == 'n':
                pos['y'] += value
            if direction == 'e':
                pos['x'] += value
            if direction == 's':
                pos['y'] -= value
            if direction == 'w':
                pos['x'] -= value

        elif action == 'N':
            pos['y'] += value
        elif action == 'S':
            pos['y'] -= value

        elif action == 'E':
            pos['x'] += value
        elif action == 'W':
            pos['x'] -= value

        elif action == 'R':
            d_idx = directions.index(direction)
            direction = directions[(d_idx + (value//90)) % 4]

        elif action == 'L':
            d_idx = directions.index(direction)
            direction = directions[(d_idx - (value//90)) % 4]

    return abs(pos['x']) + abs(pos['y'])


test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 25

ans = run(load_input('input.txt'))
assert ans == 1319

print(ans)
