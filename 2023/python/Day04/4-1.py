import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(data):
    total_val = 0
    for card in data:
        card_val = 0
        card_num = int(card.split(":")[0].split()[-1])
        your_nums, win_nums = card.split(":")[1].split("|")

        your_nums = your_nums.strip().split()
        win_nums = win_nums.strip().split()

        shared_nums = set(your_nums).intersection(win_nums)

        if shared_nums:
            card_val = 1

        for i in range(len(shared_nums) - 1):
            card_val *= 2

        total_val += card_val

    return total_val


test_ans = run(load_input("test_input.txt"))
print(test_ans)
assert test_ans == 13

ans = run(load_input("input.txt"))
assert ans == 25010
print(ans)
