import os
import sys
from rich import print


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(data):
    total_val = 0

    for line in data:
        orig_history = list(map(int, line.split()))
        current_history = orig_history.copy()
        history_chain = [orig_history]
        while not all([val == 0 for val in current_history]):
            # print(current_history)
            next_history = []
            for idx in range(1, len(current_history)):
                prev_value = current_history[idx - 1]
                value = current_history[idx]
                next_history.append(value - prev_value)

            current_history = next_history
            history_chain.append(next_history.copy())

        add_val = 0
        for idx, link in reversed(list(enumerate(history_chain))):
            history_chain[idx].insert(0, link[0] - add_val)
            add_val = link[0]
        # print(history_chain)
        total_val += history_chain[0][0]

    return total_val


test_ans = run(load_input("test_input.txt"))
print(test_ans)
assert test_ans == 2

ans = run(load_input("input.txt"))
assert ans == 1057
print(ans)
