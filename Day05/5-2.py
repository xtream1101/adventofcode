import os
import sys


orig_polymers = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    orig_polymers = f.read().strip()

# orig_polymers = 'dabAcCaCBAcCcaDA'

unique_units = set(orig_polymers.lower())

shortest_polymer = (None, None)
for unit in unique_units:
    polymers = orig_polymers.replace(unit, '').replace(unit.upper(), '')
    idx = 0
    while True:
        try:
            if abs(ord(polymers[idx]) - ord(polymers[idx + 1])) == 32:
                polymers = polymers[:idx] + polymers[idx + 2:]
                # Now that chars shifted over, lets check the prev char to the new neighbour
                idx -= 1
            else:
                idx += 1  # Move on to the next char
        except IndexError:
            # Reached the end of the string
            break
    polymer_size = len(polymers)
    if shortest_polymer[0] is None:
        shortest_polymer = (unit, polymer_size)
    elif shortest_polymer[1] > polymer_size:
        shortest_polymer = (unit, polymer_size)


print(f"Part 2: {shortest_polymer}")
