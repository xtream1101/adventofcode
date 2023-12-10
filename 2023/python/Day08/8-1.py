import os
import sys
import re
from rich import print


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(data):
    total_val = 0

    directions = data[0]

    nodes = {}
    for line in data[2:]:
        # print(line)
        key_node, _, left_node, right_node, _ = re.split(r" =|\(|, |\)", line)
        # print(key_node, left_node, right_node)
        nodes[key_node] = (left_node, right_node)

    current_node = "AAA"
    step = 0
    while current_node != "ZZZ":
        direction = directions[step % len(directions)]
        step += 1
        total_val += 1
        current_node = (
            nodes[current_node][0] if direction == "L" else nodes[current_node][1]
        )
    return total_val


test_ans = run(load_input("test_input.txt"))
print(test_ans)
assert test_ans == 2

test_ans = run(load_input("test_input_2.txt"))
print(test_ans)
assert test_ans == 6

ans = run(load_input("input.txt"))
assert ans == 19241
print(ans)
