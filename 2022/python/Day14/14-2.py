import os
import sys
import collections


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def render_cave(rocks, sand, start=(500, 0)):
    y_vals = [ r[1] for r in rocks + collections.deque([start]) ]
    x_vals = [ r[0] for r in rocks + sand + collections.deque([start]) ]
    # Used to offset the render of the cave
    mm_y = (min(y_vals), max(y_vals))
    mm_x = (min(x_vals), max(x_vals))

    for y in range(start[1], mm_y[1] + 2):
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
    rock_floor = '#' * (mm_x[1] - mm_x[0] + 1)
    print(f'\033[36m{rock_floor}\033[0m', end='')
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
    # try and use deque in place of list for its append/pop performance
    rocks = collections.deque()
    sand = collections.deque([start])
    for rock_scan in cave_scan:
        rock_range = [
            tuple(map(int, r.split(','))) for r in rock_scan.split(' -> ')
        ]
        rocks.extend(get_all_rocks(rock_range))


    cave_floor_y = max([ r[1] for r in rocks ]) + 2

    while True:
        grain = sand.pop()
        # Just so we know its still running...
        if grain == start and len(sand) % 1000 == 0:
            print(f"Sand: {len(sand)}")
            render_cave(rocks, sand, start=start)

        if render:
            render_cave(rocks, sand, start=start)
            input()

        # Settled on floor
        if grain[1] == cave_floor_y - 1:
            # Just so we know its still running...
            print(f"Landed on floor at x: {grain[0]}")
            sand.append(grain)
            sand.append(start)

        # Sand down
        elif (grain[0], grain[1] + 1) not in rocks and (grain[0], grain[1] + 1) not in sand:
            sand.append((grain[0], grain[1] + 1))

        # Sand Down left
        elif (grain[0] - 1, grain[1] + 1) not in rocks and (grain[0] - 1, grain[1] + 1) not in sand:
            sand.append((grain[0] - 1, grain[1] + 1))

        # Sand Down right
        elif (grain[0] + 1, grain[1] + 1) not in rocks and (grain[0] + 1, grain[1] + 1) not in sand:
            sand.append((grain[0] + 1, grain[1] + 1))

        # Settled
        else:
            sand.append(grain)
            if grain == start:
                # Sand blocking source
                break
            sand.append(start)

    render_cave(rocks, sand, start=start)
    return len(sand)


test_ans = run(load_input('test_input.txt'), render=False)
print(test_ans)
assert test_ans == 93

ans = run(load_input('input.txt'), render=False)
# assert ans == 862
print(ans)
