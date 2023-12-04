import os
import sys
from collections import defaultdict


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(data):
    card_copies = defaultdict(int)

    for card in data:
        card_num = int(card.split(":")[0].split()[-1].strip())
        your_nums, win_nums = card.split(":")[1].split("|")

        your_nums = your_nums.strip().split()
        win_nums = win_nums.strip().split()

        shared_nums = set(your_nums).intersection(win_nums)

        card_copies[card_num] += 1

        for i in range(1, len(shared_nums) + 1):
            card_copies[card_num + i] += card_copies[card_num]

    return sum(card_copies.values())


test_ans = run(load_input("test_input.txt"))
print(test_ans)
assert test_ans == 30

ans = run(load_input("input.txt"))
assert ans == 9924412
print(ans)
