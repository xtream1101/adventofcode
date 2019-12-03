import os
import sys


inputs = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    inputs = f.read().splitlines()

wire1 = inputs[0].split(',')
wire2 = inputs[1].split(',')

# Tests
# wire1 = ['R8','U5','L5','D3']
# wire2 = ['U7','R6','D4','L4']

def gen_path(wire):
    wire_path = [(0, 0)]
    for val in wire:
        d = val[0]
        dist = int(val[1:])

        for i in range(1, dist + 1):
            last_pos = wire_path[-1]
            if d == 'R':
                wire_path.append((last_pos[0] + 1, last_pos[1]))
            elif d == 'L':
                wire_path.append((last_pos[0] - 1, last_pos[1]))
            elif d == 'U':
                wire_path.append((last_pos[0], last_pos[1] - 1))
            elif d == 'D':
                wire_path.append((last_pos[0], last_pos[1] + 1))
    return wire_path[1:]  # Do not care about 0,0


wire1_path = gen_path(wire1)
wire2_path = gen_path(wire2)


cross_at = set(wire1_path) & set(wire2_path)
min_dist = None
for c in cross_at:
    total = 0
    for path in [wire1_path, wire2_path]:
        path_dist = 0
        prev_cell = (0, 0)
        for node in path:
            if prev_cell[0] == node[0]:
                path_dist += abs(abs(prev_cell[1]) - abs(node[1]))
            else:
                path_dist += abs(abs(prev_cell[0]) - abs(node[0]))
            prev_cell = node
            if node == c:
                break
        total += path_dist

    if min_dist is None or min_dist > total:
        min_dist = total

print(min_dist)
