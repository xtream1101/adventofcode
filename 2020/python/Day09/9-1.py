import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        data = f.read().splitlines()
    return list(map(int, data))


def run(data, preamble_len):

    for idx, num in enumerate(data):
        if idx < preamble_len:
            continue

        found_match = False
        for i, j in enumerate(data[idx-preamble_len:idx], start=1):
            for k in data[idx-preamble_len+i:idx]:
                if j+k == num:
                    found_match = True
                    break
            if found_match is True:
                break
        if found_match is False:
            return num


test_ans = run(load_input('test_input.txt'), 5)
# print(test_ans)
assert test_ans == 127

ans = run(load_input('input.txt'), 25)
assert ans == 776203571

print(ans)
