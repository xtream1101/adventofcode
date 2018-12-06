import os
import sys


polymers = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    polymers = f.read().strip()




print(f"Part 2: {non_overlapping_claims}")
