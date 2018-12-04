import os
import sys
from collections import Counter


box_ids = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    box_ids = f.read().splitlines()

two_times_count = 0
three_times_count = 0
for box_id in box_ids:
    counter = Counter(box_id)
    if 2 in counter.values():
        two_times_count += 1
    if 3 in counter.values():
        three_times_count += 1

print(f"Part 1: {two_times_count * three_times_count}")
