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


def part2(raw_orbits, print_tree=False):
    orbit_map = generate_orbit_map(raw_orbits, print_tree=print_tree)

    ca = commonancestors(orbit_map['YOU'], orbit_map['SAN'])[-1]
    you_a = commonancestors(orbit_map['YOU'].parent)
    you_dist = len(you_a[you_a.index(ca):])
    san_a = commonancestors(orbit_map['SAN'].parent)
    san_dist = len(san_a[san_a.index(ca):])

    return you_dist + san_dist


if __name__ == '__main__':
    print("Day 6:")

    part1_ans = part1(load_input())
    print("\tPart 1:", part1_ans)

    part2_ans = part2(load_input())
    print("\tPart 2:", part2_ans)
