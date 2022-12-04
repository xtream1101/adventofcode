import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def get_assignment_values(assignment):
    a1, a2 = assignment.split(',')
    a1sections = tuple(map(int, a1.split('-')))
    a2sections = tuple(map(int, a2.split('-')))
    return (set(range(a1sections[0], a1sections[1] + 1)), set(range(a2sections[0], a2sections[1] + 1)))

def run(assignments):
    overlapping_sets  = 0
    for assignment in assignments:
        s = get_assignment_values(assignment)
        if s[0].issubset(s[1]) or s[1].issubset(s[0]):
            overlapping_sets += 1

    return overlapping_sets


test_ans = run(load_input('test_input.txt'))
print(test_ans)
assert test_ans == 2

ans = run(load_input('input.txt'))
assert ans == 532
print(ans)
