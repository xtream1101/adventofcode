import os
import sys
import math
from fractions import Fraction

asteroid_field = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    asteroid_field = f.read().splitlines()


asteroid_field1 = [
    '.#..#',
    '.....',
    '#####',
    '....#',
    '...##',
]

asteroid_field2 = [
    '......#.#.',
    '#..#.#....',
    '..#######.',
    '.#.#.###..',
    '.#..#.....',
    '..#....#.#',
    '#..#....#.',
    '.##.#..###',
    '##...#..#.',
    '.#....####',
]

asteroid_field3 = [
    '#.#...#.#.',
    '.###....#.',
    '.#....#...',
    '##.#.#.#.#',
    '....#.#.#.',
    '.##..###.#',
    '..#...##..',
    '..##....##',
    '......#...',
    '.####.###.',
]
asteroid_field4 = [
    '.#..#..###',
    '####.###.#',
    '....###.#.',
    '..###.##.#',
    '##.##.#.#.',
    '....###..#',
    '..#.#..#.#',
    '#..#.#.###',
    '.##...##.#',
    '.....#.#..',
]

asteroid_field5 = [
    '.#..##.###...#######',
    '##.############..##.',
    '.#.######.########.#',
    '.###.#######.####.#.',
    '#####.##.#.##.###.##',
    '..#####..#.#########',
    '####################',
    '#.####....###.#.#.##',
    '##.#################',
    '#####.##.###..####..',
    '..######..##.#######',
    '####.##.####...##..#',
    '.#####..#.######.###',
    '##...#.##########...',
    '#.##########.#######',
    '.####.#.###.###.#.##',
    '....##.##.###..#####',
    '.#.#.###########.###',
    '#.#.#.#####.####.###',
    '###.##.####.##.#..##',
]

def get_asteroid_locations(asteroid_field):
    asteroids = set()
    for y, row in enumerate(asteroid_field):
        for x, spot in enumerate(row):
            if spot == '#':
                asteroids.add((x, y))
    return asteroids


def slope(p1, p2):
    y = p2[1] - p1[1]
    x = p2[0] - p1[0]
    x_dir = -1 if x < 0 else 1
    y_dir = -1 if y < 0 else 1
    if x == 0:
        if y < 0:
            y = -1
        if y > 0:
            y = 1
        return 0, y
    if y == 0:
        if x < 0:
            x = -1
        if x > 0:
            x = 1
        return x, 0

    sf = Fraction(x, y)
    dir_adjust = -1 if x < 0 and y < 0 else 1
    a = abs(sf.numerator) * x_dir, abs(sf.denominator) * y_dir
    # print(a)
    return a


def get_path(base, target):
    field_min = (0, 0)
    path = [base]
    s = slope(base, target)
    while path[-1] != target:
        path.append((path[-1][0] + s[0], path[-1][1] + s[1]))

    return path



assert slope((3, 4), (4, 0)) == (1, -4)
assert slope((3, 4), (1, 0)) == (-1, -2)
assert slope((1, 2), (4, 4)) == (3, 2)
assert slope((1, 2), (1, 0)) == (0, -1)
assert slope((1, 2), (0, 2)) == (-1, 0)
assert slope((4, 3), (3, 4)) == (-1, 1)
assert slope((2, 2), (4, 0)) == (1, -1)
assert slope((1, 7), (9, 5)) == (4, -1)



def get_best_base(asteroid_field):
    base_stats = {}
    asteroids = get_asteroid_locations(asteroid_field)
    for base in asteroids:
        base_stats[base] = 0
        for asteroid in asteroids:
            if base == asteroid:
                continue

            path = get_path(base, asteroid)
            if not set(path[1:-1]) & asteroids:
                base_stats[base] += 1

    # Get largest count
    largets_count = (None, None)
    for base, total_seen in base_stats.items():
        if largets_count == (None, None) or total_seen > largets_count[1]:
            largets_count = (base, total_seen)

    return largets_count

assert get_best_base(asteroid_field1) == ((3, 4), 8)
assert get_best_base(asteroid_field2) == ((5, 8), 33)
assert get_best_base(asteroid_field3) == ((1, 2), 35)
assert get_best_base(asteroid_field4) == ((6, 3), 41)
assert get_best_base(asteroid_field5) == ((11, 13), 210)

print(get_best_base(asteroid_field))
