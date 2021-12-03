import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        report = f.read().splitlines()
    return report


def get_rating(report, most_common=True):
    index = 0
    num_list = report.copy()
    _0 = []
    _1 = []

    while len(num_list) > 1:

        for num in num_list:
            if num[index] == '1':
                _1.append(num)
            else:
                _0.append(num)

        if most_common and len(_0) > len(_1):
            num_list = _0.copy()
        elif not most_common and len(_0) <= len(_1):
            num_list = _0.copy()
        else:
            num_list = _1.copy()

        index += 1
        _0 = []
        _1 = []

    return num_list[0]


def run(report):
    o2_gen_rating = get_rating(report, most_common=True)
    co2_scrubber_rating = get_rating(report, most_common=False)
    return int(o2_gen_rating, 2) * int(co2_scrubber_rating, 2)


test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 230

ans = run(load_input('input.txt'))
assert ans == 793873

print(ans)
