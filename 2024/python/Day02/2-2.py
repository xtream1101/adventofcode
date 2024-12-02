import os
import sys
from rich import print


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def check_safe_levels(levels):
    is_increasing = levels[0] < levels[1]
    for i in range(len(levels) - 1):
        if is_increasing is not (levels[i] < levels[i + 1]):
            return False

        level_delta = abs(levels[i] - levels[i + 1])
        if level_delta < 1 or level_delta > 3:
            return False

    return True


def run(data):
    total_safe = 0
    for report in data:
        levels = list(map(int, report.split()))
        level_check = check_safe_levels(levels)
        if level_check is not True:
            for i in range(len(levels)):
                new_levels = levels.copy()
                new_levels.pop(i)
                level_check = check_safe_levels(new_levels)
                if level_check is True:
                    break

        if level_check is True:
            total_safe += 1

    return total_safe


test_ans = run(load_input("test_input.txt"))
print(test_ans)
assert test_ans == 4

ans = run(load_input("input.txt"))
assert ans == 328
print(ans)
