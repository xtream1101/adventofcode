import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        report = f.read().splitlines()
    return list(map(int, report))


def run(expected_sum, report):
    for idx, entry in enumerate(report):
        for sub_idx, sub_entry in enumerate(report[idx+1:]):
            for sub2_idx, sub2_entry in enumerate(report[sub_idx+1:]):
                if sub_entry + sub2_entry + entry == expected_sum:
                    # print(entry, sub_entry, sub2_entry)
                    return entry * sub_entry * sub2_entry


test_ans = run(2020, load_input('test_input.txt'))
assert test_ans == 241861950

ans = run(2020, load_input('input.txt'))
assert ans == 85555470

print(ans)
