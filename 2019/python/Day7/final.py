import os
import itertools
os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Day2.final import IntCodeComputer  # noqa: E402


def load_input():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_file) as f:
        inputs = f.read().split(',')
    return list(map(int, inputs))


def find_largest_thrust(program, phase_setting):
    largest_thrust = (None, None)
    for phase_setting_seq in list(itertools.permutations(phase_setting)):
        thrust_output = run_program_sequence(program, phase_setting_seq)
        if largest_thrust == (None, None) or thrust_output > largest_thrust[1]:
            largest_thrust = (phase_setting_seq, thrust_output)
    return largest_thrust[1]


def run_program_sequence(program, phase_setting_seq):
    amps = {}
    output = 0
    feedback_loop_idx = 0
    while amps.get('E', {}).get('status') != 'halt':
        for amp, phase in enumerate(phase_setting_seq, start=65):
            amp_name = chr(amp)

            if amp_name not in amps:
                amps[amp_name] = {
                    'status': 'running',
                    'computer': IntCodeComputer(program, [phase])
                }
            computer = amps[amp_name]['computer']
            computer.run([output])

            output = computer.outputs[-1]

            if computer.last_optcode == 99:
                amps[amp_name]['status'] = 'halt'

        feedback_loop_idx += 1

    return output


def part1(program):
    return find_largest_thrust(program, [0, 1, 2, 3, 4])


def part2(program):
    return find_largest_thrust(program, [5, 6, 7, 8, 9])


if __name__ == '__main__':
    print("Day 7:")

    part1_ans = part1(load_input())
    print("\tPart 1:", part1_ans)

    part2_ans = part2(load_input())
    print("\tPart 2:", part2_ans)
