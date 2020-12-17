import os
import sys
import copy


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        data = f.read().splitlines()
    return [list(r) for r in data]


def default_layer(n=3):
    return [['.']*n for _ in range(n)]


def pcube(cubes):
    for z, cube in cubes.items():
        print(f"z={z}")
        for r in cube:
            print(''.join(r))


def expand_cubes(cubes):
    for cube_z in cubes.values():
        for row in cube_z:
            row.insert(0, '.')
            row.append('.')
        cube_z.insert(0, ['.'] * len(cube_z[0]))
        cube_z.append(['.'] * len(cube_z[0]))

    return cubes


def generate_neighbors():
    neighbors = []
    for z_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            for x_offset in range(-1, 2):
                # (z, y, x)
                if z_offset == 0 and y_offset == 0 and x_offset == 0:
                    continue
                neighbors.append((z_offset, y_offset, x_offset))
    return neighbors


def run(cubes, cycles):
    cubes = {
        0: cubes
    }

    # (z, y, x)
    neighbors = generate_neighbors()
    for cycle in range(1, cycles + 1):
        cubes = expand_cubes(cubes)
        cubes_snapshot = copy.deepcopy(cubes)
        for z in range(cycle * -1, cycle + 1):
            if z not in cubes:
                cubes[z] = default_layer(len(cubes_snapshot[0][0]))
                cubes_snapshot[z] = default_layer(len(cubes_snapshot[0][0]))

            for y, row in enumerate(cubes_snapshot[z]):
                for x, c in enumerate(row):
                    num_active = 0
                    for n in neighbors:
                        try:
                            z_offset = z + n[0]
                            y_offset = y + n[1]
                            x_offset = x + n[2]
                            if x_offset == -1 or y_offset == -1:
                                continue
                            if z_offset in cubes_snapshot and cubes_snapshot[z_offset][y_offset][x_offset] == '#':
                                num_active += 1
                        except (IndexError, KeyError):
                            pass

                    if c == '#':
                        if num_active not in (2, 3):
                            cubes[z][y][x] = '.'
                    elif c == '.':
                        if num_active == 3:
                            cubes[z][y][x] = '#'

        # print("Cycle:", cycle)
        # pcube(cubes)

    total = 0
    for z in cubes.values():
        for row in z:
            total += row.count('#')

    return total


test_ans = run(load_input('test_input.txt'), 6)
# print(test_ans)
assert test_ans == 112

ans = run(load_input('input.txt'), 6)
print(ans)
assert ans == 291

try:
    from aocd import submit
    submit(ans, part="a", day=17, year=2020)
except ModuleNotFoundError:
    print("Answer did not auto submit")
