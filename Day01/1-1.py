import os
import sys


frequencies = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    frequencies = f.read().splitlines()


result = 0
for freq in frequencies:
    operation = freq[0]
    value = int(freq[1:])
    if operation == '+':
        result += value
    else:
        result -= value

print(f"Part 1: {result}")
