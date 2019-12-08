import os
import sys


def load_input():
    input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
    with open(input_file) as f:
        inputs = f.read().split(',')
    return list(map(int, inputs))


def int_code_computer(program):
    pointer = 0
    while True:
        optcode = program[pointer]
        if optcode == 99:
            # Done
            break

        params = program[pointer + 1:pointer + 4]

        if optcode == 1:
            # Add
            program[params[2]] = program[params[0]] + program[params[1]]

        elif optcode == 2:
            # Multiply
            program[params[2]] = program[params[0]] * program[params[1]]

        else:
            raise ValueError

        pointer += 4

    return program


def part1(program):
    program[1] = 12
    program[2] = 2
    return int_code_computer(program)[0]


def part2(program):
    looking_for = 19690720
    for noun in range(0, 99 + 1):
        for verb in range(0, 99 + 1):
            program_copy = program.copy()
            program_copy[1] = noun
            program_copy[2] = verb
            if int_code_computer(program_copy)[0] == looking_for:
                return 100 * noun + verb


def tests_part1():
    assert int_code_computer([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert int_code_computer([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert int_code_computer([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert int_code_computer([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]
    print("\tPart 1: tests passed")


if __name__ == '__main__':
    print("Day 2:")
    tests_part1()

    part1_ans = part1(load_input())
    print("\tPart 1:", part1_ans)
    assert part1_ans == 3101878

    part2_ans = part2(load_input())
    print("\n\tPart 2:", part2_ans)
    assert part2_ans == 8444
