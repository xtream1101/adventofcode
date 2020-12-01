import os
import sys

input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    report = f.read().splitlines()
report = list(map(int, report))

test_report = [1721, 979, 366, 299, 675, 1456]


def run(expected_sum, report):
    for idx, entry in enumerate(report):
        for sub_entry in report[idx+1:]:
            if sub_entry + entry == expected_sum:
                # print(entry, sub_entry)
                return entry * sub_entry


test_ans = run(2020, test_report)
assert test_ans == 514579

ans = run(2020, report)
assert ans == 902451

print(ans)
