import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def render_cave(mm_x, mm_y, rocks, sand, start=(500, 0)):
    for y in range(mm_y[0], mm_y[1] + 1):
        for x in range(mm_x[0], mm_x[1] + 1):
            if (x,y) in rocks:
                print('\033[36m#\033[0m', end='')
            elif (x,y) in sand:
                print('\033[93m0\033[0m', end='')
            elif (x,y) == start:
                print('\033[31m+\033[0m', end='')
            else:
                print('\033[90m.\033[0m', end='')
        print()
    print(f"Sand: {len(sand)}")


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


def run(cave_scan, render=False):
    start = (500, 0)
    rocks = []
    for rock_scan in cave_scan:
        rock_range = [
            tuple(map(int, r.split(','))) for r in rock_scan.split(' -> ')
        ]
        rocks.extend(get_all_rocks(rock_range))

    y_vals = [ r[1] for r in rocks]
    x_vals = [ r[0] for r in rocks]
    # Used to offset the render of the cave
    mm_y = (min(y_vals + [start[1]]), max(y_vals + [start[1]]))
    mm_x = (min(x_vals + [start[0]]), max(x_vals + [start[0]]))

    sand = [start]

    while (sand[-1][0] >= mm_x[0] and sand[-1][0] <= mm_x[1]  # within x range
      and sand[-1][1] >= mm_y[0] and sand[-1][1] <= mm_y[1]   # within y range
    ):
        if render:
            render_cave(mm_x, mm_y, rocks, sand, start=start)
            input()
        grain = sand.pop()
        # Sand down
        if (grain[0], grain[1] + 1) not in rocks + sand:
            sand.append((grain[0], grain[1] + 1))

        # Sand Down left
        elif (grain[0] - 1, grain[1] + 1) not in rocks + sand:
            sand.append((grain[0] - 1, grain[1] + 1))

        # Sand Down right
        elif (grain[0] + 1, grain[1] + 1) not in rocks + sand:
            sand.append((grain[0] + 1, grain[1] + 1))

        else:
            # Sand settled, start falling again
            sand.append(grain)
            sand.append(start)

    # render_cave(mm_x, mm_y, rocks, sand, start=start)
    return len(sand[:-1]) # Last grain does not count since it fell


test_ans = run(load_input('test_input.txt'), render=True)
print(test_ans)
assert test_ans == 24

ans = run(load_input('input.txt'), render=False)
assert ans == 862
print(ans)
