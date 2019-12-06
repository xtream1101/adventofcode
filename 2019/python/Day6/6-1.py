import os
import sys
from anytree import Node, RenderTree, PreOrderIter
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
    else:
        orbit_map[in_orbit] = Node(in_orbit, parent=orbit_map[obj])


total_orbits = 0

seen_orbits = set()
# print(RenderTree(orbit_map['COM']))
for node in PreOrderIter(orbit_map['COM']):
    ca = commonancestors(node)
    # print(node.name, ca)
    total_orbits += len(ca)

print(total_orbits)
