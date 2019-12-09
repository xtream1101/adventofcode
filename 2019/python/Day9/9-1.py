import os
import sys

input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    program = f.read().split(',')
program = list(map(int, program))


def run_program(program, inputs):
    program = program.copy()
    relative_base = 0
    outputs = []
    idx = 0

    def parse_instruction(val):
        val = str(val)
        val = '0'*(5-len(val)) + val
        optcode = int(val[-2:])
        modes = val[:3]
        return optcode, modes

    def get_idx(modes, i):
        idx_mode = {
            '0': program[idx + i],
            '1': idx + i,
            '2': program[idx + i] + relative_base,
        }
        new_idx = idx_mode[modes[-i]]
        increase_mem(program, new_idx)
        return new_idx

    def increase_mem(program, new_idx):
        if len(program) > new_idx:
            return program
        for _ in range(new_idx - len(program) + 1):
            program.append(0)
        return program

    while True:
        optcode, modes = parse_instruction(program[idx])
        if optcode == 1:
            a = program[get_idx(modes, 1)]
            b = program[get_idx(modes, 2)]
            program[get_idx(modes, 3)] = a + b
            idx += 4

        elif optcode == 2:
            a = program[get_idx(modes, 1)]
            b = program[get_idx(modes, 2)]
            program[get_idx(modes, 3)] = a * b
            idx += 4

        elif optcode == 3:
            program[get_idx(modes, 1)] = inputs.pop(0)
            idx += 2

        elif optcode == 4:
            output = program[get_idx(modes, 1)]
            outputs.append(output)
            idx += 2

        elif optcode == 5:
            a = program[get_idx(modes, 1)]
            b = program[get_idx(modes, 2)]
            idx = b if a != 0 else idx + 3

        elif optcode == 6:
            a = program[get_idx(modes, 1)]
            b = program[get_idx(modes, 2)]
            idx = b if a == 0 else idx + 3

        elif optcode == 7:
            a = program[get_idx(modes, 1)]
            b = program[get_idx(modes, 2)]
            program[get_idx(modes, 3)] = 1 if a < b else 0
            idx += 4

        elif optcode == 8:
            a = program[get_idx(modes, 1)]
            b = program[get_idx(modes, 2)]
            program[get_idx(modes, 3)] = 1 if a == b else 0
            idx += 4

        elif optcode == 9:
            relative_base += program[get_idx(modes, 1)]
            idx += 2

        elif optcode == 99:
            return outputs

        else:
            raise ValueError


i0 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
i1 = [1102,34915192,34915192,7,4,7,99,0]
i2 = [104,1125899906842624,99]

# print(run_program(i0, []))
# print(run_program(i1, []))
# print(run_program(i2, []))
print(run_program(program, [1]))


