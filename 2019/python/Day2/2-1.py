import os
import sys


inputs = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    inputs = f.read().split(',')

inputs = list(map(int, inputs))
inputs[1] = 12
inputs[2] = 2
idx = 0
while True:
    val = inputs[idx]
    idx_1 = inputs[idx + 1]
    idx_2 = inputs[idx + 2]

    if val == 1:
        # add
        store_at_idx = inputs[idx + 3]
        inputs[store_at_idx] = inputs[idx_1] + inputs[idx_2]
        idx += 4
        continue
    elif val == 2:
        store_at_idx = inputs[idx + 3]
        inputs[store_at_idx] = inputs[idx_1] * inputs[idx_2]
        idx += 4
        continue
    # either 99 or we do not care about it
    break


print(inputs)
