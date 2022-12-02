import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return list(lines)


def run(calories):
    total_cal_counts = [0]
    for cal_item in calories:
        if cal_item == "":
            total_cal_counts.append(0)
            continue
        total_cal_counts[-1] += int(cal_item)

    total_cal_counts.sort()
    return sum(total_cal_counts[-3:])


test_ans = run(load_input('test_input.txt'))
print(test_ans)
assert test_ans == 45000

ans = run(load_input('input.txt'))
assert ans == 206104

print(ans)
