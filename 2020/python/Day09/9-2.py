import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        data = f.read().splitlines()
    return list(map(int, data))


def run(data, total):
    count_list = []
    for idx, num in enumerate(data):
        while sum(count_list) > total:
            count_list.pop(0)

        if sum(count_list) == total:
            return min(count_list) + max(count_list)

        count_list.append(num)


test_ans = run(load_input('test_input.txt'), 127)
# print(test_ans)
assert test_ans == 62

ans = run(load_input('input.txt'), 776203571)
assert ans == 104800569

print(ans)
