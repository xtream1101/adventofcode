import os
import sys


polymers = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    polymers = f.read().strip()

# polymers = 'dabAcCaCBAcCcaDA'

idx = 0
while True:

    try:
        # print(polymers)
        # print(f"{' '*idx}^")
        if abs(ord(polymers[idx]) - ord(polymers[idx + 1])) == 32:
            # print(f"Remove {polymers[idx]} {polymers[idx + 1]} @ {idx},{idx+1}\n")
            polymers = polymers[:idx] + polymers[idx + 2:]
            # Now that chars shifted over, lets check the prev char to the new neighbour
            idx -= 1
        else:
            idx += 1  # Move on to the next char
    except IndexError:
        # Reached the end of the string
        break

print(f"Part 1: {len(polymers)}")
