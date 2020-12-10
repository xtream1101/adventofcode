import os
import sys

from collections import defaultdict


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        data = f.read().splitlines()
    return list(map(int, data))

from pprint import pprint
import copy


def run(joltage):
    known_sets = {}

    def find_set_from(value):
        if value in known_sets:
            return known_sets[value]

        total_options = 0
        for i in (1, 2, 3):
            if value + i in joltage:
                total_options += find_set_from(value + i)
        # if 0 there are no other options, just the current path
        total_options = 1 if total_options == 0 else total_options
        known_sets[value] = total_options
        # print(known_sets)
        return known_sets[value]

    return find_set_from(0)


test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 8

test_ans = run(load_input('test_input_2.txt'))
# print(test_ans)
assert test_ans == 19208

ans = run(load_input('input.txt'))
assert ans == 56693912375296

print(ans)
