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
for x in range(max_x + 1):
    for y in range(max_y + 1):
        # Get the distance each coord is away from the cell
        dists = defaultdict(list)
        for a, b in coords:
            coord_id = (a, b)
            dist = abs(a - x) + abs(b - y)
            dists[dist].append(coord_id)

        min_dist = dists[min(dists.keys())]

        # See if shortest distance belongs to just 1 coord
        if len(min_dist) == 1:
                coord_id = min_dist[0]
                region_sizes[coord_id] += 1

                # Make sure the cell is not on the edge (meaning infinte size)
                if x == 0 or x == max_x or y == 0 or y == max_y:
                    edge_coords.add(coord_id)

# Find the coord with the largest distance
max_size = (None, 0)
for coord_id, size in region_sizes.items():
    if coord_id not in edge_coords:
        if size >= max_size[1]:
            max_size = (coord_id, size)

print(f"Coord: {max_size[0]}")
print(f"Size: {max_size[1]}")
