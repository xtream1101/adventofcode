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
                    other_seats = []
                    for r_shift in (-1, 0, 1):
                        for c_shift in (-1, 0, 1):
                            if r_shift == 0 and c_shift == 0:
                                continue
                            if (r_idx + r_shift < len(layout) and r_idx + r_shift >= 0) and (c_idx + c_shift < len(row) and c_idx + c_shift >= 0):
                                other_seats.append(prev_layout[r_idx + r_shift][c_idx + c_shift])

                    if '#' not in other_seats:
                        layout[r_idx][c_idx] = '#'

                elif seat == '#':
                    count = 0
                    for r_shift in (-1, 0, 1):
                        for c_shift in (-1, 0, 1):
                            if r_shift == 0 and c_shift == 0:
                                continue
                            if (r_idx + r_shift < len(layout) and r_idx + r_shift >= 0) and (c_idx + c_shift < len(row) and c_idx + c_shift >= 0):
                                if prev_layout[r_idx + r_shift][c_idx + c_shift] == '#':
                                    count += 1

                    if count >= 4:
                        layout[r_idx][c_idx] = 'L'

        # pprint(layout)
        # input()

    total = 0
    for row in layout:
        total += row.count('#')

    return total


test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 37

ans = run(load_input('input.txt'))
assert ans == 2113

print(ans)
