import os


def load_input():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_file) as f:
        inputs = f.read().splitlines()
    return inputs[0].split(','), inputs[1].split(',')


def gen_path(wire):
    wire_path = [(0, 0)]
    for val in wire:
        d = val[0]
        dist = int(val[1:])

        direction_action = {
            'R': lambda pos: (pos[0] + 1, pos[1]),
            'L': lambda pos: (pos[0] - 1, pos[1]),
            'U': lambda pos: (pos[0], pos[1] - 1),
            'D': lambda pos: (pos[0], pos[1] + 1),
        }
        for i in range(1, dist + 1):
            wire_path.append(direction_action[d](wire_path[-1]))

    return wire_path


def part1(wire1, wire2):
    wire1_path = gen_path(wire1)
    wire2_path = gen_path(wire2)

    min_dist = None
    # Check distance from each intersections
    # Ignore the start of 0,0 int he wire paths
    for intersect in set(wire1_path[1:]) & set(wire2_path[1:]):
        dist = abs(intersect[0]) + abs(intersect[1])
        min_dist = dist if min_dist is None else min(min_dist, dist)

    return min_dist


def calc_path_distance(wire, intersect):
    path_dist = 0
    for i, node in enumerate(wire[1:], start=1):
        prev_node = wire[i - 1]
        if prev_node[0] == node[0]:
            # Add vertical distance
            path_dist += abs(abs(prev_node[1]) - abs(node[1]))
        else:
            # Add horizontal distance
            path_dist += abs(abs(prev_node[0]) - abs(node[0]))

        if node == intersect:
            # We found the end of the path
            break

    return path_dist


def part2(wire1, wire2):
    wire1_path = gen_path(wire1)
    wire2_path = gen_path(wire2)

    min_dist = None
    # Check distance from each intersection, to the start (0,0)
    for intersect in set(wire1_path[1:]) & set(wire2_path[1:]):
        dist = calc_path_distance(wire1_path, intersect) + calc_path_distance(wire2_path, intersect)
        min_dist = dist if min_dist is None else min(min_dist, dist)

    return min_dist


if __name__ == '__main__':
    print("Day 3:")

    part1_ans = part1(*load_input())
    print("\tPart 1:", part1_ans)

    part2_ans = part2(*load_input())
    print("\tPart 2:", part2_ans)
