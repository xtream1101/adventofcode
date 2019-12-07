import os
import sys
import itertools

inputs = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    inputs = f.read().split(',')

inputs = list(map(int, inputs))

inputs1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
inputs2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
# inputs3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

def run_program(signal, inputs):
    signal = signal.copy()
    def parse_instruction(val):
        val = str(val)
        val = '0'*(5-len(val)) + val
        optcode = int(val[-2:])
        modes = val[:3]

        return optcode, modes

    last_output = None
    idx = 0
    for _ in range(len(signal)):
        optcode, modes = parse_instruction(signal[idx])
        if optcode == 1:
            # add
            a = signal[signal[idx + 1]] if modes[-1] == '0' else signal[idx + 1]
            b = signal[signal[idx + 2]] if modes[-2] == '0' else signal[idx + 2]
            store_at_idx = signal[idx + 3] if modes[-3] == '0' else idx + 3

            signal[store_at_idx] = a + b
            idx += 4

        elif optcode == 2:
            a = signal[signal[idx + 1]] if modes[-1] == '0' else signal[idx + 1]
            b = signal[signal[idx + 2]] if modes[-2] == '0' else signal[idx + 2]
            store_at_idx = signal[idx + 3] if modes[-3] == '0' else idx + 3

            signal[store_at_idx] = a * b
            idx += 4

        elif optcode == 3:
            store_at_idx = signal[idx + 1] if modes[-1] == '0' else idx + 1
            signal[store_at_idx] = inputs.pop(0)

            idx += 2

        elif optcode == 4:
            output = signal[signal[idx + 1]] if modes[-1] == '0' else signal[idx + 1]
            last_output = output
            idx += 2

        elif optcode == 5:
            a = signal[signal[idx + 1]] if modes[-1] == '0' else signal[idx + 1]
            b = signal[signal[idx + 2]] if modes[-2] == '0' else signal[idx + 2]

            if a != 0:
                idx = b
            else:
                idx += 3

        elif optcode == 6:
            a = signal[signal[idx + 1]] if modes[-1] == '0' else signal[idx + 1]
            b = signal[signal[idx + 2]] if modes[-2] == '0' else signal[idx + 2]

            if a == 0:
                idx = b
            else:
                idx += 3


        elif optcode == 7:
            a = signal[signal[idx + 1]] if modes[-1] == '0' else signal[idx + 1]
            b = signal[signal[idx + 2]] if modes[-2] == '0' else signal[idx + 2]
            store_at_idx = signal[idx + 3] if modes[-3] == '0' else idx + 3

            if a < b:
                signal[store_at_idx] = 1
            else:
                signal[store_at_idx] = 0

            idx += 4

        elif optcode == 8:
            a = signal[signal[idx + 1]] if modes[-1] == '0' else signal[idx + 1]
            b = signal[signal[idx + 2]] if modes[-2] == '0' else signal[idx + 2]
            store_at_idx = signal[idx + 3] if modes[-3] == '0' else idx + 3

            if a == b:
                signal[store_at_idx] = 1
            else:
                signal[store_at_idx] = 0

            idx += 4

        elif optcode == 99:
            return last_output



def run_sequence(seq, inputs):
    signal = inputs.copy()
    output = 0
    for amp, phase in enumerate(seq, start=65):
        amp = chr(amp)
        in_val = [phase, output]
        output = run_program(signal, in_val)

    return output

# run_sequence([4,3,2,1,0], inputs1)
# run_sequence([0,1,2,3,4], inputs2)
largest_thrust = (None, None)
for seq in list(itertools.permutations([0, 1, 2, 3, 4])):
    thrust_output = run_sequence(seq, inputs)
    if largest_thrust == (None, None) or thrust_output > largest_thrust[1]:
        largest_thrust = (seq, thrust_output)

print(largest_thrust)
