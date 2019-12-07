import os
import sys
import itertools

inputs = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    inputs = f.read().split(',')

inputs = list(map(int, inputs))

inputs1 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
inputs2 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

def run_program(program, signal, last_output=None, idx=0):
    program = program.copy()
    def parse_instruction(val):
        val = str(val)
        val = '0'*(5-len(val)) + val
        optcode = int(val[-2:])
        modes = val[:3]

        return optcode, modes

    for _ in range(len(program)):
        optcode, modes = parse_instruction(program[idx])
        # print("optcode", optcode, "idx", idx)
        if optcode == 1:
            # add
            a = program[program[idx + 1]] if modes[-1] == '0' else program[idx + 1]
            b = program[program[idx + 2]] if modes[-2] == '0' else program[idx + 2]
            store_at_idx = program[idx + 3] if modes[-3] == '0' else idx + 3

            program[store_at_idx] = a + b
            idx += 4

        elif optcode == 2:
            a = program[program[idx + 1]] if modes[-1] == '0' else program[idx + 1]
            b = program[program[idx + 2]] if modes[-2] == '0' else program[idx + 2]
            store_at_idx = program[idx + 3] if modes[-3] == '0' else idx + 3

            program[store_at_idx] = a * b
            idx += 4

        elif optcode == 3:
            store_at_idx = program[idx + 1] if modes[-3] == '0' else idx + 1
            program[store_at_idx] = signal.pop(0)
            idx += 2

        elif optcode == 4:
            output = program[program[idx + 1]] if modes[-1] == '0' else program[idx + 1]
            idx += 2
            return program, output, idx, 'output'

        elif optcode == 5:
            a = program[program[idx + 1]] if modes[-1] == '0' else program[idx + 1]
            b = program[program[idx + 2]] if modes[-2] == '0' else program[idx + 2]

            if a != 0:
                idx = b
            else:
                idx += 3

        elif optcode == 6:
            a = program[program[idx + 1]] if modes[-1] == '0' else program[idx + 1]
            b = program[program[idx + 2]] if modes[-2] == '0' else program[idx + 2]

            if a == 0:
                idx = b
            else:
                idx += 3

        elif optcode == 7:
            a = program[program[idx + 1]] if modes[-1] == '0' else program[idx + 1]
            b = program[program[idx + 2]] if modes[-2] == '0' else program[idx + 2]
            store_at_idx = program[idx + 3] if modes[-3] == '0' else idx + 3

            if a < b:
                program[store_at_idx] = 1
            else:
                program[store_at_idx] = 0

            idx += 4

        elif optcode == 8:
            a = program[program[idx + 1]] if modes[-1] == '0' else program[idx + 1]
            b = program[program[idx + 2]] if modes[-2] == '0' else program[idx + 2]
            store_at_idx = program[idx + 3] if modes[-3] == '0' else idx + 3

            if a == b:
                program[store_at_idx] = 1
            else:
                program[store_at_idx] = 0

            idx += 4

        elif optcode == 99:
            return program, last_output, idx, 'halt'

        else:
            raise ValueError



def run_sequence(seq, orig_program):
    output = 0
    status = None
    feedback_loop_idx = 0
    amp_state = {}
    amp_status = {}
    while set(amp_status.values()) != {'halt'}:
        for amp, phase in enumerate(seq, start=65):
            amp = chr(amp)

            if amp in amp_state:
                program = amp_state[amp]['program']
                idx = amp_state[amp]['idx']
                last_output = amp_state[amp]['last_output']
            else:
                program = orig_program.copy()
                idx = 0
                last_output = None

            signals = [phase, output] if feedback_loop_idx == 0 else [output]

            # print("amp", amp)
            # print('phase',phase)
            # print('feedback_loop_idx', feedback_loop_idx)
            # print('signals', signals)
            # print('program_idx', idx)

            new_program, output, new_idx, status = run_program(program, signals, last_output=last_output, idx=idx)
            amp_state[amp] = {
                'program': new_program.copy(),
                'idx': new_idx,
                'last_output': output
            }
            # print(amp_state[amp])
            # _ = input("hit enter")
            if status == 'halt':
                amp_status[amp] = 'halt'

        feedback_loop_idx += 1

    return output


# print(run_sequence([9,8,7,6,5], inputs1))
# print(run_sequence([9,7,8,5,6], inputs2))
largest_thrust = (None, None)
for seq in list(itertools.permutations([5, 6, 7, 8, 9])):
    thrust_output = run_sequence(seq, inputs)
    if largest_thrust == (None, None) or thrust_output > largest_thrust[1]:
        largest_thrust = (seq, thrust_output)

print(largest_thrust)
