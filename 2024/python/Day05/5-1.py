from collections import defaultdict
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

    page_rules = defaultdict(list)
    updates = []
    for line in data:
        if "|" in line:
            r1, r2 = line.split("|")
            page_rules[r1].append(r2)
        elif "," in line:
            updates.append(line.split(","))

    for update in updates:
        is_update_valid = True
        for p_idx, page in enumerate(update):
            if page in page_rules:
                for p_value in page_rules[page]:
                    if p_value not in update:
                        continue
                    p2_idx = update.index(p_value)
                    if p_idx > p2_idx:
                        is_update_valid = False
                        break

        if is_update_valid:
            middle = update[len(update) // 2]
            total_val += int(middle)

    return total_val


test_ans = run(load_input("test_input.txt"))
print(test_ans)
assert test_ans == 143

ans = run(load_input("input.txt"))
assert ans == 6051
print(ans)
