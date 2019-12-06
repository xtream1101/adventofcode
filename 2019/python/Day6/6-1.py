import os
import sys
from anytree import Node, RenderTree
from anytree.util import commonancestors

inputs = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    inputs = f.read().splitlines()

# inputs = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']
# inputs = ['B)C', 'COM)B', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']
# inputs = ['B)C', 'COM)B', 'C)D', 'E)F', 'B)G', 'D)E', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']


orbit_map = {}

for i in inputs:
    obj, in_orbit = i.split(')')

    if obj not in orbit_map:
        orbit_map[obj] = Node(obj)

    if in_orbit in orbit_map:
        # update parent
        orbit_map[in_orbit].parent = orbit_map[obj]
        for child in orbit_map[in_orbit].children:
            orbit_map[child.name].parent = orbit_map[in_orbit]

    orbit_map[in_orbit] = Node(in_orbit, parent=orbit_map[obj])
    # print(i)
    # print(orbit_map)


total_orbits = 0

# Doing something wrong when updating nodes, so need to dedup when counting
seen_orbits = set()
for pre, fill, node in RenderTree(orbit_map['COM']):
    if node.name not in seen_orbits:
        ca = commonancestors(node)
        seen_orbits.add(node.name)
        # print(node.name, ca)
        total_orbits += len(ca)

print(total_orbits)
