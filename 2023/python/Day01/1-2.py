import os
import sys
import re


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


swap = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def run(data):
    total = 0
    for line in data:
        found_nums = {}
        for i in swap:
            n = [m.start() for m in re.finditer(i, line)]
            if n:
                for k in n:
                    found_nums[k] = swap[i]

        for idx, i in enumerate(line):
            if i.isdigit():
                found_nums[idx] = i

        found_num = int(
            found_nums[min(found_nums.keys())] + found_nums[max(found_nums.keys())]
        )

        # print( line , '--', found_num, '--', found_nums)
        total += found_num

    return total


test_ans = run(load_input("test_input_2.txt"))
print(test_ans)
assert test_ans == 281

ans = run(load_input("input.txt"))
assert ans == 55429
print(ans)
