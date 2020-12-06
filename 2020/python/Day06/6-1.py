import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        report = f.read().splitlines()
    return report


def run(answers):
    output = 0

    group = set()
    for idx, answer in enumerate(answers):
        if answer != '':
            for data in answer:
                group.add(data)
            # If not the last line
            if len(answers) != idx + 1:
                continue

        output += len(group)
        group = set()

    return output


test_ans = run(load_input('test_input.txt'))
assert test_ans == 11

ans = run(load_input('input.txt'))
assert ans == 6565

print(ans)
