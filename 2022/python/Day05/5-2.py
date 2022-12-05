import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(data):
    crate_stacks = {}
    raw_crates = []
    for crate_setup in data:
        if crate_setup == '':
            # Moves start next loop
            break
        raw_crates.append(crate_setup)

    # Transforms crates to horz layout, ie Lists
    crate_columns = raw_crates.pop()
    raw_crates.reverse()

    for crate_col in crate_columns.split():
        crate_stacks[crate_col] = []
        crate_col_idx = crate_columns.index(crate_col)
        for crate_row in raw_crates:
            if len(crate_row) >= crate_col_idx and crate_row[crate_col_idx] != ' ':
                crate_stacks[crate_col].append(crate_row[crate_col_idx])

    # Start move commands
    for move in data[len(raw_crates)+2:]:
        _, crate_count, _ , stack_from, _, stack_to = move.split()
        move_crates = []
        for i in range(int(crate_count)):
            move_crates.insert(0, crate_stacks[stack_from].pop())

        crate_stacks[stack_to].extend(move_crates)

    top_crates = ''
    for col in crate_columns.split():
        top_crates += crate_stacks[col][-1]

    return top_crates




test_ans = run(load_input('test_input.txt'))
print(test_ans)
assert test_ans == 'MCD'

ans = run(load_input('input.txt'))
assert ans == 'JSDHQMZGF'
print(ans)
