import os
import sys
from rich import print, pretty
import itertools


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(data):
    total_val = 0

    # First expand...
    rows_with_galaxies = []
    cols_with_galaxies = []
    for r_idx, r in enumerate(data):
        if "#" in r:
            rows_with_galaxies.append(r_idx)
            for c_idx, c in enumerate(r):
                if c == "#":
                    cols_with_galaxies.append(c_idx)

    # Expand rows & cols with no galaxies
    expanded_map = []
    for r_idx, r in enumerate(data):
        new_row = []
        for c_idx, c in enumerate(r):
            if c_idx not in cols_with_galaxies:
                new_row.append("..")
            else:
                new_row.append(c)
        expanded_map.append("".join(new_row))
        if r_idx not in rows_with_galaxies:
            # add the row again
            expanded_map.append("".join(new_row))

    # print()
    # for r in expanded_map:
    #     print(r)

    # Second: Find pos of galaxies
    galaxies = {}
    for r_idx, r in enumerate(expanded_map):
        for c_idx, c in enumerate(r):
            if c == "#":
                galaxies[(r_idx, c_idx)] = 0

    # Third: Find the closest galaxy to each point
    for galaxy_a, galaxy_b in itertools.combinations(galaxies, 2):
        # Manhattan distance
        dist = abs(galaxy_a[0] - galaxy_b[0]) + abs(galaxy_a[1] - galaxy_b[1])
        # print(f'{galaxy_a} to {galaxy_b} is {dist}')
        galaxies[galaxy_a] += dist

    return sum(galaxies.values())


test_ans = run(load_input("test_input.txt"))
print(test_ans)
assert test_ans == 374

ans = run(load_input('input.txt'))
assert ans == 9918828
print(ans)
