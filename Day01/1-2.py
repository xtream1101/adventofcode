import os
import sys


frequencies = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    frequencies = f.read().splitlines()


freq_seen_list = {0: True}
result = 0
found_duplicate = None
while found_duplicate is None:
    for freq in frequencies:
        result += int(freq)

        if freq_seen_list.get(result) is not None:
            found_duplicate = result
            break

        freq_seen_list[result] = True

print(f"Part 2: {found_duplicate}")
