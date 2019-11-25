import os
import sys


frequencies = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    frequencies = f.read().splitlines()

result = sum(map(int, frequencies))

print(f"Part 1: {result}")
