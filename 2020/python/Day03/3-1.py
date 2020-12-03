import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        report = f.read().splitlines()
    return report


def run(area, slope_x, slope_y):
    width = len(area[0])
    height = len(area)
    next_x = slope_x
    next_y = slope_y
    tree_count = 0
    while True:
        if next_y >= height:
            break
        if next_x >= width:
            next_x = next_x - width
        curr_spot = area[next_y][next_x]
        if curr_spot == '#':
            tree_count += 1

        next_x += slope_x
        next_y += slope_y

    return tree_count


test_ans = run(load_input('test_input.txt'), 3, 1)
assert test_ans == 7

ans = run(load_input('input.txt'), 3, 1)
assert ans == 268

print(ans)
