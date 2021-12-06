import os
import sys
from collections import defaultdict
from pprint import pprint


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        ages = f.read().split(',')
    return list(map(int, ages))


def run(ages, days):

    fish_ages = {}
    # Get starting fish counts
    for i in range(9):
        fish_ages[i] = ages.count(i)

    # pprint(fish_ages)

    # Age the fish each day
    for day in range(1, days + 1):
        tmp_fish_ages = defaultdict(int)
        for i in range(9):
            match i:
                case 0:
                    tmp_fish_ages[6] += fish_ages[i]
                    tmp_fish_ages[8] += fish_ages[i]
                case _:
                    tmp_fish_ages[i - 1] += fish_ages[i]
        fish_ages = tmp_fish_ages.copy()
        # print(f"Day: {day}")
        # pprint(tmp_fish_ages)
        # input('...')
    return sum(fish_ages.values())


test_ans = run(load_input('test_input.txt'), 18)
# print(18, test_ans)
assert test_ans == 26

test_ans = run(load_input('test_input.txt'), 80)
# print(80, test_ans)
assert test_ans == 5934

test_ans = run(load_input('test_input.txt'), 256)
# print(256, test_ans)
assert test_ans == 26984457539


ans = run(load_input('input.txt'), 256)
assert ans == 1705008653296
print(ans)
