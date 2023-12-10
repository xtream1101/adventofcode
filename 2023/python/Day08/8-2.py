import os
import sys
import re
from math import gcd
from rich import print


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(data):
    directions = data[0]

    nodes = {}
    for line in data[2:]:
        # print(line)
        key_node, _, left_node, right_node, _ = re.split(r" =|\(|, |\)", line)
        # print(key_node, left_node, right_node)
        nodes[key_node] = (left_node, right_node)

    # dict of start nodes and values fo the current node for that iteration
    node_paths = {}
    for node in nodes.keys():
        if node.endswith("A"):
            node_paths[node] = {"first_z": None, "current_node": node}

    step = 0
    while any([node["first_z"] is None for node in node_paths.values()]):
        direction = directions[step % len(directions)]
        step += 1
        for start_node, node in node_paths.items():
            if direction == "L":
                node_paths[start_node]["current_node"] = nodes[node["current_node"]][0]
            else:
                node_paths[start_node]["current_node"] = nodes[node["current_node"]][1]

            if node_paths[start_node]["first_z"] is None and node_paths[start_node][
                "current_node"
            ].endswith("Z"):
                node_paths[start_node]["first_z"] = step

        # print(node_paths)
        # input()

        # check if all current nodes ends in a "Z"
        if all([node["current_node"].endswith("Z") for node in node_paths.values()]):
            break

    # print(node_paths)
    lcm = 1
    for node in node_paths.values():
        lcm = lcm * node["first_z"] // gcd(lcm, node["first_z"])

    return lcm


test_ans = run(load_input("test_input_3.txt"))
print(test_ans)
assert test_ans == 6

ans = run(load_input("input.txt"))
assert ans == 9606140307013
print(ans)
