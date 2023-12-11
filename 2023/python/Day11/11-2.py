import os
import sys
from rich import print, pretty
import itertools


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(data, expand_multiplier):
    expand_multiplier -= 1

    # First expand...
    rows_with_galaxies = set()
    cols_with_galaxies = set()
    for r_idx, r in enumerate(data):
        if "#" in r:
            rows_with_galaxies.add(r_idx)
            for c_idx, c in enumerate(r):
                if c == "#":
                    cols_with_galaxies.add(c_idx)

    rows_with_no_galaxies = set(range(len(data))) - rows_with_galaxies
    col_with_no_galaxies = set(range(len(data[0]))) - cols_with_galaxies

    # Second: Find pos of galaxies
    galaxies = {}
    for r_idx, r in enumerate(data):
        r_offset = expand_multiplier * sum(i < r_idx for i in rows_with_no_galaxies)
        for c_idx, c in enumerate(r):
            if c == "#":
                c_offset = expand_multiplier * sum(
                    i < c_idx for i in col_with_no_galaxies
                )
                galaxies[(r_idx + r_offset, c_idx + c_offset)] = 0

    # Third: Find the closest galaxy to each point
    for galaxy_a, galaxy_b in itertools.combinations(galaxies, 2):
        # Manhattan distance
        dist = abs(galaxy_a[0] - galaxy_b[0]) + abs(galaxy_a[1] - galaxy_b[1])
        # print(f'{galaxy_a} to {galaxy_b} is {dist}')
        galaxies[galaxy_a] += dist

    return sum(galaxies.values())


test_ans = run(load_input("test_input.txt"), 2)
print(test_ans)
assert test_ans == 374

test_ans = run(load_input("test_input.txt"), 10)
print(test_ans)
assert test_ans == 1030

test_ans = run(load_input("test_input.txt"), 100)
print(test_ans)
assert test_ans == 8410

ans = run(load_input("input.txt"), 1000000)
assert ans == 692506533832
print(ans)
