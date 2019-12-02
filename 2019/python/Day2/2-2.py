import os
import sys


orig_inputs = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    orig_inputs = f.read().split(',')

orig_inputs = list(map(int, orig_inputs))

for i in range(0, 99 + 1):
    for j in range(0, 99 + 1):
        inputs = orig_inputs.copy()
        inputs[1] = i
        inputs[2] = j
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

        if inputs[0] == 19690720:
            print("ans", 100 * i + j)
            break
