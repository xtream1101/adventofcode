import os
import sys


frequencies = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    frequencies = f.read().splitlines()


freq_seen_list = [0]
result = 0
found_duplicate = None
while found_duplicate is None:
    for freq in frequencies:
        operation = freq[0]
        value = int(freq[1:])
        if operation == '+':
            result += value
        else:
            result -= value

        if result in freq_seen_list:
            found_duplicate = result
            break

        freq_seen_list.append(result)

print(f"Part 2: {found_duplicate}")
