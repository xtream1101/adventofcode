import os
import re
import sys
from pprint import pprint
from collections import defaultdict

steps_input = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')  # ans 1265
# input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input2.txt')  # ans 828
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
# ]  # ans = 15


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
workers = []
for _ in range(5):  # test: 2, input: 5
    workers.append({'node': '', 'time_done': None})

step_duration = 60  # test: 0, input: 60
current_time = 0  # First action can happen on the 0 second
while True:
    for worker in workers:
        if worker['time_done'] and worker['time_done'] <= current_time:
            chain += worker['node']
            # Unlock other nodes now
            new_nodes = list(set(step_tree[worker['node']]) - set(nodes))
            nodes = sorted(new_nodes + nodes)
            worker['node'] = ''
            worker['time_done'] = None

    # This 2nd loop of the workers is needed for input2.txt, not for input.txt
    # Just the single line below, all other code can stay under the first for loop
    # This is because in input2.txt there is a case where a worker gets released,
    #   but has nothing to pick up at that time
    # Then the next worker releases and adds more nodes that can be worked on,
    #   but the first worker will not pick it up since it already did its check.
    # Solution is to release all workers first, then have them check for tasks
    for worker in workers:
        if not worker['node']:
            for node in nodes:
                depends_on = {k for k, v in step_tree.items() if node in v}
                still_needs = {v for v in depends_on if v not in chain}
                if still_needs:
                    continue

                worker['node'] = node
                break
                # Give the worker a node if it has no depends
            if worker['node']:
                nodes.remove(worker['node'])
                worker['time_done'] = step_duration + current_time + ord(worker['node']) - 64

    # print(current_time, [(w['node'], w['time_done']) for w in workers], nodes)
    # print(chain)

    if not [d['node'] for d in workers if d['node']]:
        break

    current_time += 1


print(current_time)
