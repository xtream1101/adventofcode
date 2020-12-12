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

    pos = {'x': 0, 'y': 0}
    wp = {'x': 10, 'y': 1}
    for instruction in nav:
        action = instruction[0]
        value = int(''.join(instruction[1:]))

        if action == 'F':
            while value != 0:
                pos['x'] += wp['x']
                pos['y'] += wp['y']
                value -= 1

        elif action == 'N':
            wp['y'] += value
        elif action == 'S':
            wp['y'] -= value
        elif action == 'E':
            wp['x'] += value
        elif action == 'W':
            wp['x'] -= value

        elif action == 'R':
            while value != 0:
                wp = {'x': wp['y'], 'y': wp['x'] * -1}
                value -= 90

        elif action == 'L':
            while value != 0:
                wp = {'x': wp['y'] * -1, 'y': wp['x']}
                value -= 90

    #     print(action, pos, wp)
    #     input()

    return abs(pos['x']) + abs(pos['y'])


test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 286

ans = run(load_input('input.txt'))
assert ans == 62434

print(ans)
