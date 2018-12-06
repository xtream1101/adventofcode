import os
import sys
from collections import defaultdict


coords_input = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    coords_input = f.read().strip().splitlines()

# coords_input = [
# '1, 1',
# '1, 6',
# '8, 3',
# '3, 4',
# '5, 5',
# '8, 9',
# ]

# Find the max grid size
max_x = 0
max_y = 0
coords = set()
for idx, coord in enumerate(coords_input):
    x, y = map(int, coord.split(', '))
    coords.add((x, y))
    max_x = max(max_x, x)
    max_y = max(max_y, y)


# Find the distance of each coord from each cell
region_sizes = defaultdict(int)
edge_coords = set()
cell_dists = {}
for x in range(max_x + 1):
    for y in range(max_y + 1):
        # Get the distance each coord is away from the cell
        dists = []
        for a, b in coords:
            coord_id = (a, b)
            dist = abs(a - x) + abs(b - y)
            dists.append(dist)

        cell_dists[(x,y)] = sum(dists)

# 32 for test, 10000 for input.txt
cells_under_limit = {k: v for k, v in cell_dists.items() if v < 10000}
print(len(cells_under_limit))
