import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        ages = f.read().split(',')
    return list(map(int, ages))


def run(ages, days):

    for i in range(1, days + 1):
        for idx, age in enumerate(ages.copy()):
            if age == 0:
                ages[idx] = 6
                ages.append(8)
            else:
                ages[idx] -= 1

        # print(f"Day {i}: {ages}")

    return len(ages)


test_ans = run(load_input('test_input.txt'), 18)
# print(test_ans)
assert test_ans == 26

test_ans = run(load_input('test_input.txt'), 80)
# print(test_ans)
assert test_ans == 5934

ans = run(load_input('input.txt'), 80)
assert ans == 379414
print(ans)
