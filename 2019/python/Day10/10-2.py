import os
import sys
import math
from fractions import Fraction

asteroid_field = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    for row in f.read().splitlines():
        asteroid_field.append(list(row))



asteroid_field1 = [
    list('.#....#####...#..'),
    list('##...##.#####..##'),
    list('##...#...#.#####.'),
    list('..#.....#...###..'),
    list('..#.#.....#....##'),
]
asteroid_field2 = [
    list('.#..##.###...#######'),
    list('##.############..##.'),
    list('.#.######.########.#'),
    list('.###.#######.####.#.'),
    list('#####.##.#.##.###.##'),
    list('..#####..#.#########'),
    list('####################'),
    list('#.####....###.#.#.##'),
    list('##.#################'),
    list('#####.##.###..####..'),
    list('..######..##.#######'),
    list('####.##.####...##..#'),
    list('.#####..#.######.###'),
    list('##...#.##########...'),
    list('#.##########.#######'),
    list('.####.#.###.###.#.##'),
    list('....##.##.###..#####'),
    list('.#.#.###########.###'),
    list('#.#.#.#####.####.###'),
    list('###.##.####.##.#..##'),
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

    myradians = math.atan2(base[1]-target[1], base[0]-target[0])
    myradians -= math.pi/2
    deg = math.degrees(myradians)

    return deg, path



a = get_path((1, 2), (1, 1))
b = get_path((1, 2), (2, 2))
c = get_path((1, 2), (1, 4))
d = get_path((1, 2), (0, 2))

print(a[0], '\t', 0)
print(b[0], '\t', 90)
print(c[0], '\t', 180)  # -180 is the same value
print(d[0], '\t', -90)


def order_clockwise(data):
    """
    0->180->-180->0
    """
    data = data.copy()
    data.sort()
    for i, v in enumerate(data):
        if v[0] == 0:
           break

    data = data[i:] + data[:i]

    return data


def rotate_laser(base, asteroid_field):
    base_paths = []
    asteroids = get_asteroid_locations(asteroid_field)
    for asteroid in asteroids:
        if base != asteroid:
            deg, path = get_path(base, asteroid)
            # only have astroids in path
            path_asteroid = set(path)&asteroids
            for cord in path.copy():
                if cord not in path_asteroid:
                    path.remove(cord)

            base_paths.append((deg, path[1:]))

    print("Num paths", len(base_paths))

    # De dup paths
    for a_idx, a in enumerate(base_paths.copy()):
        for b_idx, b in enumerate(base_paths.copy()):
            if a[0] == b[0] and len(a[1]) < len(b[1]):
                base_paths.remove(a)
                break

    print("Num paths", len(base_paths))
    num_astroids_destroyed = 0
    base_paths = order_clockwise(base_paths)
    has_paths = True
    while has_paths:
        has_paths = False
        for base_path in base_paths:
            deg, path = base_path
            # print(deg)
            if path:
                has_paths = True
                astroid_destroyed = path.pop(0)
                num_astroids_destroyed += 1
                # asteroid_field[astroid_destroyed[1]][astroid_destroyed[0]] = str(num_astroids_destroyed)
                print("Destroy #" + str(num_astroids_destroyed), astroid_destroyed)
                if num_astroids_destroyed == 200:
                    # print field for debugging
                    # for field in asteroid_field:
                    #     print(' '.join(field))
                    return astroid_destroyed

    print(num_astroids_destroyed)



# print(rotate_laser((8, 3), asteroid_field1))
# print(rotate_laser((11, 13), asteroid_field2))
print(rotate_laser((31, 20), asteroid_field))



