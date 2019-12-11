import os
from anytree.util import commonancestors
from anytree import Node, RenderTree, PreOrderIter


def load_input():
    inputs = []
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_file) as f:
        inputs = f.read().splitlines()
    return inputs


def generate_orbit_map(raw_orbits, print_tree=False):
    orbit_map = {}
    for orbit in raw_orbits:
        obj, obj_in_orbit = orbit.split(')')
        if obj not in orbit_map:
            orbit_map[obj] = Node(obj)

        if obj_in_orbit in orbit_map:
            orbit_map[obj_in_orbit].parent = orbit_map[obj]
        else:
            orbit_map[obj_in_orbit] = Node(obj_in_orbit, parent=orbit_map[obj])

    if print_tree is True:
        # Only print small maps
        for pre, fill, node in RenderTree(orbit_map['COM']):
            print("%s%s" % (pre, node.name))

    return orbit_map


def part1(raw_orbits, print_tree=False):
    orbit_map = generate_orbit_map(raw_orbits, print_tree=print_tree)
    total_orbits = 0
    for node in PreOrderIter(orbit_map['COM']):
        ca = commonancestors(node)
        total_orbits += len(ca)

    return total_orbits


def part2(raw_orbits, node1_name, node2_name, print_tree=False):
    orbit_map = generate_orbit_map(raw_orbits, print_tree=print_tree)
    node1 = orbit_map[node1_name]
    node2 = orbit_map[node2_name]
    ca = commonancestors(node1, node2)[-1]

    orbital_transfers = 0
    for node in (node1, node2):
        a = commonancestors(node.parent)
        orbital_transfers += len(a[a.index(ca):])

    return orbital_transfers


if __name__ == '__main__':
    print("Day 6:")

    part1_ans = part1(load_input())
    print("\tPart 1:", part1_ans)

    part2_ans = part2(load_input(), 'YOU', 'SAN')
    print("\tPart 2:", part2_ans)
