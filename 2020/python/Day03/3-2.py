import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        report = f.read().splitlines()
    return report


def run(area, slopes):
    width = len(area[0])
    height = len(area)
    total_value = 1
    for slope_x, slope_y in slopes:
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

        total_value *= tree_count

    return total_value


test_ans = run(
    load_input('test_input.txt'),
    (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )
)
assert test_ans == 336

ans = run(load_input('input.txt'), (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )
)
assert ans == 3093068400

print(ans)
