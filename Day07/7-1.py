import os
import re
import sys
from pprint import pprint
from collections import defaultdict

steps_input = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    steps_input = f.read().strip().splitlines()

# steps_input = [
#     'Step C must be finished before step A can begin.',
#     'Step C must be finished before step F can begin.',
#     'Step A must be finished before step B can begin.',
#     'Step A must be finished before step D can begin.',
#     'Step B must be finished before step E can begin.',
#     'Step D must be finished before step E can begin.',
#     'Step F must be finished before step E can begin.',
# ]

step_tree = defaultdict(list)
step_pattern = re.compile(r'Step (\w).*step (\w)')
for step in steps_input:
    m = step_pattern.search(step)
    step_1, step_2 = m.groups()
    step_tree[step_1].append(step_2)


# pprint(step_tree)


step_keys = set(step_tree.keys())
step_values = set([item for sublist in step_tree.values() for item in sublist])
first_steps = sorted(list(step_keys - step_values))

chain = ''
nodes = first_steps
while nodes:
    current_node = nodes.pop(0)

    depends_on = {k for k, v in step_tree.items() if current_node in v}
    still_needs = {v for v in depends_on if v not in chain}
    if still_needs:
        continue

    chain += current_node

    new_nodes = list(set(step_tree[current_node]) - set(nodes))
    nodes = sorted(new_nodes + nodes)

    # print()
    # print(chain)
    # print(nodes, len(nodes))


print(chain)
