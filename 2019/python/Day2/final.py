import os


def load_input():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_file) as f:
        inputs = f.read().split(',')
    return list(map(int, inputs))


class IntCodeComputer:

    def __init__(self, program, input_val=()):
        self.program = program.copy()
        self.inputs = self._input_to_list(input_val)
        self.outputs = []
        self.current_idx = 0
        self.relative_base = 0

    def _parse_instruction(self, val):
        val = str(val)
        val = '0' * (5 - len(val)) + val
        optcode = int(val[-2:])
        modes = val[:3]
        return optcode, modes

    def _get_instruction(self):
        return self._parse_instruction(self.program[self.current_idx])

    def _increase_mem(self, new_idx):
        if len(self.program) < new_idx:
            for _ in range(new_idx - len(self.program) + 1):
                self.program.append(0)

    def _input_to_list(self, input_val):
        if isinstance(input_val, (list, tuple, set)):
            return list(input_val)
        return [input_val]

    def _get_params(self, num, modes):
        params = []
        for i in range(1, num + 1):
            idx_mode = {
                '0': self.program[self.current_idx + i],
                '1': self.current_idx + i,
                '2': self.program[self.current_idx + i] + self.relative_base,
            }
            new_idx = idx_mode[modes[-i]]
            params.append(new_idx)
            self._increase_mem(new_idx)
        return params

    def run(self, input_val=()):
        self.inputs.extend(self._input_to_list(input_val))

        while True:
            optcode, modes = self._get_instruction()
            self.last_optcode = optcode
            if optcode == 1:
                params = self._get_params(3, modes)
                self.program[params[2]] = self.program[params[0]] + self.program[params[1]]
                self.current_idx += 4

            elif optcode == 2:
                params = self._get_params(3, modes)
                self.program[params[2]] = self.program[params[0]] * self.program[params[1]]
                self.current_idx += 4

            elif optcode == 3:
                try:
                    next_input = self.inputs.pop(0)
                except IndexError:
                    # No more inputs left
                    return
                params = self._get_params(1, modes)
                self.program[params[0]] = next_input
                self.current_idx += 2

            elif optcode == 4:
                params = self._get_params(1, modes)
                self.outputs.append(self.program[params[0]])
                self.current_idx += 2

            elif optcode == 5:
                params = self._get_params(2, modes)
                self.current_idx = self.program[params[1]] if self.program[params[0]] != 0 else self.current_idx + 3

            elif optcode == 6:
                params = self._get_params(2, modes)
                self.current_idx = self.program[params[1]] if self.program[params[0]] == 0 else self.current_idx + 3

            elif optcode == 7:
                params = self._get_params(3, modes)
                self.program[params[2]] = 1 if self.program[params[0]] < self.program[params[1]] else 0
                self.current_idx += 4

            elif optcode == 8:
                params = self._get_params(3, modes)
                self.program[params[2]] = 1 if self.program[params[0]] == self.program[params[1]] else 0
                self.current_idx += 4

            elif optcode == 9:
                params = self._get_params(1, modes)
                self.relative_base += self.program[params[0]]
                self.current_idx += 2

            elif optcode == 99:
                return

            else:
                raise ValueError


def part1(program):
    program[1] = 12
    program[2] = 2
    process = IntCodeComputer(program)
    process.run()
    return process.program[0]


def part2(program):
    looking_for = 19690720
    for noun in range(0, 99 + 1):
        for verb in range(0, 99 + 1):
            program_copy = program.copy()
            program_copy[1] = noun
            program_copy[2] = verb
            process = IntCodeComputer(program_copy)
            process.run()
            if process.program[0] == looking_for:
                return 100 * noun + verb


if __name__ == '__main__':
    print("Day 2:")

    part1_ans = part1(load_input())
    print("\tPart 1:", part1_ans)

    part2_ans = part2(load_input())
    print("\tPart 2:", part2_ans)
