import os
import sys
from anytree import Node, RenderTree
from anytree.util import commonancestors, leftsibling, rightsibling

inputs = []
input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input_file) as f:
    inputs = f.read().splitlines()

# inputs = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L','K)YOU','I)SAN',]

orbit_map = {}

for i in inputs:
    obj, in_orbit = i.split(')')

    if obj not in orbit_map:
        orbit_map[obj] = Node(obj)

    if in_orbit in orbit_map:
        # set parent
        orbit_map[in_orbit].parent = orbit_map[obj]
    else:
        orbit_map[in_orbit] = Node(in_orbit, parent=orbit_map[obj])


ca = commonancestors(orbit_map['YOU'], orbit_map['SAN'])[-1]
you_a = commonancestors(orbit_map['YOU'].parent)
you_dist = len(you_a[you_a.index(ca):])
san_a = commonancestors(orbit_map['SAN'].parent)
san_dist = len(san_a[san_a.index(ca):])

print(you_dist + san_dist)
