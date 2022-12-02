import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        heightmap = f.read().splitlines()
    return [list(map(int, line)) for line in heightmap]


def run(heightmap):
    total = 0
    for r_idx, row in enumerate(heightmap):
        for c_idx, col in enumerate(row):
            is_lowest_value = True
            current_val = heightmap[r_idx][c_idx]
            # check         N        E      S       W
            for r_offset, c_offset in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                try:
                    if current_val >= heightmap[r_idx + r_offset][c_idx + c_offset]:
                        is_lowest_value = False
                except IndexError:
                    pass

            if is_lowest_value:
                total += current_val + 1

    return total


test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 15

ans = run(load_input('input.txt'))
assert ans == 562
print(ans)
