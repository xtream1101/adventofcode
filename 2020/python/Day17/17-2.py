import os
import sys
import copy


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        data = f.read().splitlines()
    return [list(r) for r in data]


def default_layer(n):
    return [['.']*n for _ in range(n)]


def pcube(cubes):
    for w, z_cubes in cubes.items():
        for z, cube in z_cubes.items():
            print(f"z={z}, w={w}")
            for r in cube:
                print(''.join(r))


def expand_cubes(cubes):
    for cube_w in cubes.values():
        for cube_z in cube_w.values():
            for row in cube_z:
                row.insert(0, '.')
                row.append('.')
            cube_z.insert(0, ['.'] * len(cube_z[0]))
            cube_z.append(['.'] * len(cube_z[0]))

    return cubes


def generate_neighbors():
    neighbors = []
    for w_offset in range(-1, 2):
        for z_offset in range(-1, 2):
            for y_offset in range(-1, 2):
                for x_offset in range(-1, 2):
                    # (w, z, y, x)
                    if w_offset == 0 and z_offset == 0 and y_offset == 0 and x_offset == 0:
                        continue
                    neighbors.append((w_offset, z_offset, y_offset, x_offset))
    return neighbors


def run(cubes, cycles):
    cubes = {
        0: {  # w
            0: cubes  # z
        }
    }

    neighbors = generate_neighbors()

    for cycle in range(1, cycles + 1):
        cubes = expand_cubes(cubes)
        cubes_snapshot = copy.deepcopy(cubes)
        for w in range(cycle * -1, cycle + 1):
            if w not in cubes:
                cubes[w] = {}
                cubes_snapshot[w] = {}

            for z in range(cycle * -1, cycle + 1):
                if z not in cubes[w]:
                    # expand grid
                    cubes_size = len(cubes_snapshot[0][0])
                    cubes[w][z] = default_layer(cubes_size)
                    cubes_snapshot[w][z] = default_layer(cubes_size)

                for y, row in enumerate(cubes_snapshot[w][z]):
                    for x, c in enumerate(row):
                        num_active = 0
                        for n in neighbors:
                            try:
                                w_offset = w + n[0]
                                z_offset = z + n[1]
                                y_offset = y + n[2]
                                x_offset = x + n[3]
                                if x_offset == -1 or y_offset == -1:
                                    continue
                                if cubes_snapshot[w_offset][z_offset][y_offset][x_offset] == '#':
                                    num_active += 1
                            except (IndexError, KeyError):
                                pass

                        if c == '#':
                            if num_active not in (2, 3):
                                cubes[w][z][y][x] = '.'
                        elif c == '.':
                            if num_active == 3:
                                cubes[w][z][y][x] = '#'

        # print("Cycle:", cycle)
        # pcube(cubes)

    total = 0
    for w in cubes.values():
        for z in w.values():
            for row in z:
                total += row.count('#')

    return total


test_ans = run(load_input('test_input.txt'), 6)
# print(test_ans)
assert test_ans == 848

ans = run(load_input('input.txt'), 6)
print(ans)
assert ans == 1524

try:
    from aocd import submit
    submit(ans, part="b", day=17, year=2020)
except ModuleNotFoundError:
    print("Answer did not auto submit")
