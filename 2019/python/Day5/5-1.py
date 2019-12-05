import os
import sys


inputs = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    inputs = f.read().split(',')



def parse_instruction(val):
    val = str(val)
    val = '0'*(5-len(val)) + val
    optcode = int(val[-2:])
    modes = val[:3]
    return optcode, modes


inputs = list(map(int, inputs))
# inputs[1] = 12
# inputs[2] = 2
# inputs = [1002,4,3,4,33,99]
input_val = 1
idx = 0
for _ in range(len(inputs)):
    optcode, modes = parse_instruction(inputs[idx])
    if optcode == 1:
        # add
        a = inputs[inputs[idx + 1]] if modes[-1] == '0' else inputs[idx + 1]
        b = inputs[inputs[idx + 2]] if modes[-2] == '0' else inputs[idx + 2]
        store_at_idx = inputs[idx + 3] if modes[-3] == '0' else idx + 3

        inputs[store_at_idx] = a + b
        idx += 4
        continue

    elif optcode == 2:
        a = inputs[inputs[idx + 1]] if modes[-1] == '0' else inputs[idx + 1]
        b = inputs[inputs[idx + 2]] if modes[-2] == '0' else inputs[idx + 2]
        store_at_idx = inputs[idx + 3] if modes[-3] == '0' else idx + 3

        inputs[store_at_idx] = a * b
        idx += 4
        continue

    elif optcode == 3:
        store_at_idx = inputs[idx + 1] if modes[-1] == '0' else idx + 1
        inputs[store_at_idx] = input_val
        idx += 2
        continue

    elif optcode == 4:
        output = inputs[inputs[idx + 1]] if modes[-1] == '0' else inputs[idx + 1]
        print("\t4:", output)
        idx += 2
        continue

    elif optcode == 99:
        print("halt")
        break
