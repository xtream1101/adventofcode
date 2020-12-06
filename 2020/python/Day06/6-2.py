import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        report = f.read().splitlines()
    return report


def run(answers):
    output = 0

    group = []
    for idx, answer in enumerate(answers):
        if answer != '':
            group.append(answer)
            # If not the last line
            if len(answers) != idx + 1:
                continue

        all_ans = ''.join(group)
        for a in set(all_ans):
            if all_ans.count(a) == len(group):
                output += 1

        group = []

    return output


test_ans = run(load_input('test_input.txt'))
assert test_ans == 6

ans = run(load_input('input.txt'))
assert ans == 3137

print(ans)
