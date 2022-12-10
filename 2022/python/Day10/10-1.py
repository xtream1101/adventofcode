import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(program):
    queue = [1]
    for cmd in program:
        match cmd.split():
            case ['addx', amount]:
                queue.extend([0, int(amount)])
            case ['noop']:
                queue.append(0)

    signal_strength = 0
    for cycle_value in [20, 60, 100, 140, 180, 220]:
        register = sum(queue[:cycle_value])
        signal_strength += register * cycle_value
        # print(cycle_value, register)

    return signal_strength


test_ans = run(load_input('test_input.txt'))
print(test_ans)
assert test_ans == 13140

ans = run(load_input('input.txt'))
assert ans == 15680
print(ans)
