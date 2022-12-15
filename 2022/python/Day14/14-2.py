import os
import sys
import time


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def render_cave(filled, falling_grain=None):
    y_vals = [ r[1] for r in filled.keys() ]
    x_vals = [ r[0] for r in filled.keys() ]
    # Used to offset the render of the cave
    mm_y = (min(y_vals), max(y_vals))
    mm_x = (min(x_vals), max(x_vals))

    for y in range(mm_y[0], mm_y[1] + 2):
        for x in range(mm_x[0], mm_x[1] + 1):
            value = filled.get((x,y), '.')

            if (x,y) == falling_grain:
                value = 'o'
                print('\033[35m', end='')
            elif value == '#':
                print('\033[36m', end='')
            elif value == 'o':
                print('\033[93m', end='')
            elif value == '.':
                print('\033[90m', end='')
            elif value == '+':
                print('\033[31m', end='')

            print(f'{value}\033[0m', end='')

        print()
    rock_floor = '#' * (mm_x[1] - mm_x[0] + 1)
    print(f'\033[36m{rock_floor}\033[0m', end='')
    print()
    print(f"Sand: {list(filled.values()).count('o')}")


def get_all_rocks(rock_range):
    rocks = []
    # Calc all rock locations
    for idx, rock in enumerate(rock_range):
        rocks.append(rock)
        try:
            next_rock = rock_range[idx + 1]
        except IndexError:
            break

        if rock[0] == next_rock[0]:
            if rock[1] < next_rock[1]:
                rocks_range = range(rock[1] + 1, next_rock[1])
            else:
                rocks_range = reversed(range(next_rock[1] + 1, rock[1]))

            for rock_y in rocks_range:
                rocks.append((rock[0], rock_y))

        elif rock[1] == next_rock[1]:
            if rock[0] < next_rock[0]:
                rocks_range = range(rock[0] + 1, next_rock[0])
            else:
                rocks_range = reversed(range(next_rock[0] + 1, rock[0]))

            for rock_x in rocks_range:
                rocks.append((rock_x, rock[1]))

    return rocks


def run(cave_scan, render_speed=0, render_every=1):
    start = (500, 0)
    filled = {
        start: '+'
    }
    for rock_scan in cave_scan:
        rock_range = [
            tuple(map(int, r.split(','))) for r in rock_scan.split(' -> ')
        ]
        for rock in get_all_rocks(rock_range):
            filled[rock] = '#'

    cave_floor_y = max([ r[1] for r in filled.keys() ]) + 2

    falling_grain = start
    while filled[start] != 'o':
        if render_speed and len(filled) % render_every == 0:
            # I know the render_every starts off with including the rocks, but does not matter
            render_cave(filled, falling_grain)
            time.sleep(render_speed)
            # input()

        # Settled on floor
        if falling_grain[1] == cave_floor_y - 1:
            filled[falling_grain] = 'o'
            falling_grain = start

        # Sand down
        elif not filled.get((falling_grain[0], falling_grain[1] + 1)):
            falling_grain = (falling_grain[0], falling_grain[1] + 1)

        # Sand down left
        elif not filled.get((falling_grain[0] - 1, falling_grain[1] + 1)):
            falling_grain = (falling_grain[0] - 1, falling_grain[1] + 1)

        # Sand down right
        elif not filled.get((falling_grain[0] + 1, falling_grain[1] + 1)):
            falling_grain = (falling_grain[0] + 1, falling_grain[1] + 1)

        # Settled on either rock or other sand
        else:
            filled[falling_grain] = 'o'
            falling_grain = start

    # render_cave(filled, grain)
    return list(filled.values()).count('o')


test_ans = run(load_input('test_input.txt'), render_speed=0.005)
print(test_ans)
assert test_ans == 93

ans = run(load_input('input.txt'), render_speed=0, render_every=1000)
assert ans == 28744
print(ans)
