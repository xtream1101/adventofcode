import os
import sys
import re
from rich import print


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read()
    return lines


def run(data):
    total_val = 0

    actions = {}
    for m in re.finditer(r"do\(\)", data):
        actions[m.start()] = "do"

    for m in re.finditer(r"don't\(\)", data):
        actions[m.start()] = "dont"

    matches = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", data)
    for m in matches:
        check_loc = actions.copy()

        mul_idx = m.start()

        check_loc[mul_idx] = "mul"
        # Sort the list of actions to see where our mul command lands
        ordered_actions = sorted(check_loc)
        # Check if the mul is not in front of a dont command
        mul_loc = ordered_actions.index(mul_idx)
        if mul_loc == 0 or check_loc[ordered_actions[mul_loc - 1]] != "dont":
            m1 = int(m.group(1))
            m2 = int(m.group(2))
            total_val += m1 * m2

    return total_val


test_ans = run(load_input("test_input_2.txt"))
print(test_ans)
assert test_ans == 48

ans = run(load_input("input.txt"))
assert ans == 97529391
print(ans)
