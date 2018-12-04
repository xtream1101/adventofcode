import os
import sys


box_ids = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    box_ids = f.read().splitlines()


def find_box_id():
    matched_box_id = ''
    for i, box_id in enumerate(box_ids):
        for other_box_id in box_ids[i+1:]:
            # Check against other box_ids after
            # since ids before have already been checked against this id
            num_changed = 0
            matched_box_id = ''
            for j, char in enumerate(box_id):
                if char == other_box_id[j]:
                    matched_box_id += char
                else:
                    num_changed += 1
                    if num_changed > 1:
                        # Move on since this is not a match
                        break

            if num_changed == 1:
                # We found it
                return matched_box_id


print(f"Part 2: {find_box_id()}")
