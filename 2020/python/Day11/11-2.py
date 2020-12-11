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


def run(layout):
    prev_layout = None
    while prev_layout != layout:
        prev_layout = copy.deepcopy(layout)
        for r_idx, row in enumerate(copy.deepcopy(layout)):
            for c_idx, seat in enumerate(row):
                if seat == '.':
                    continue

                if seat == 'L':
                    see_taken_seat = False
                    for y_shift, x_shift in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
                        y_idx = r_idx + y_shift
                        x_idx = c_idx + x_shift
                        while y_idx >= 0 and y_idx < len(layout) and x_idx >= 0 and x_idx < len(row):
                            if prev_layout[y_idx][x_idx] == '#':
                                see_taken_seat = True
                                break
                            if prev_layout[y_idx][x_idx] == 'L':
                                break
                            y_idx += y_shift
                            x_idx += x_shift

                        if see_taken_seat is True:
                            break

                    if see_taken_seat is False:
                        layout[r_idx][c_idx] = '#'

                elif seat == '#':
                    count = 0
                    for y_shift, x_shift in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
                        y_idx = r_idx + y_shift
                        x_idx = c_idx + x_shift
                        while y_idx >= 0 and y_idx < len(layout) and x_idx >= 0 and x_idx < len(row):
                            if prev_layout[y_idx][x_idx] == '#':
                                count += 1
                                break
                            if prev_layout[y_idx][x_idx] == 'L':
                                break
                            y_idx += y_shift
                            x_idx += x_shift

                    if count >= 5:
                        layout[r_idx][c_idx] = 'L'

        # pprint(layout)
        # input()

    total = 0
    for row in layout:
        total += row.count('#')

    return total


test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 26

ans = run(load_input('input.txt'))
assert ans == 1865

print(ans)
