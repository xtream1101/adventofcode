import os


def load_input():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_file) as f:
        inputs = f.read().split(',')
    return list(map(int, inputs))


def int_code_computer(program, inputs=[]):
    if not isinstance(inputs, list):
        inputs = [inputs]

    program = program.copy()
    relative_base = 0
    outputs = []
    idx = 0

    def parse_instruction(val):
        val = str(val)
        val = '0' * (5 - len(val)) + val
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
            return program, outputs

        else:
            raise ValueError


def part1(program):
    program[1] = 12
    program[2] = 2
    return int_code_computer(program)[0][0]


def part2(program):
    looking_for = 19690720
    for noun in range(0, 99 + 1):
        for verb in range(0, 99 + 1):
            program_copy = program.copy()
            program_copy[1] = noun
            program_copy[2] = verb
            if int_code_computer(program_copy)[0][0] == looking_for:
                return 100 * noun + verb


if __name__ == '__main__':
    print("Day 2:")

    part1_ans = part1(load_input())
    print("\tPart 1:", part1_ans)

    part2_ans = part2(load_input())
    print("\tPart 2:", part2_ans)
