import os
import sys
from collections import defaultdict


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(lines):
    vents = defaultdict(int)
    for line in lines:
        xy1, xy2 = line.split(' -> ')
        x1, y1 = map(int, xy1.split(','))
        x2, y2 = map(int, xy2.split(','))

        vents[(x1, y1)] += 1
        vents[(x2, y2)] += 1
        if x1 == x2:
            y = min(y1, y2)
            for i in range(1, abs(y1 - y2)):
                vents[(x1, y + i)] += 1
        elif y1 == y2:
            x = min(x1, x2)
            for i in range(1, abs(x1 - x2)):
                vents[(x + i, y1)] += 1
        else:
            # angle
            x_dir = 1 if x1 < x2 else -1
            y_dir = 1 if y1 < y2 else -1
            for i in range(1, abs(x1 - x2)):
                x = x1 + (i * x_dir)
                y = y1 + (i * y_dir)
                vents[(x, y)] += 1

    return sum([1 for val in vents.values() if val > 1])


test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 12

ans = run(load_input('input.txt'))
assert ans == 19771
print(ans)
