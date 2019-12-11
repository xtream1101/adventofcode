import os
os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Day2.final import int_code_computer  # noqa: E402


def load_input():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_file) as f:
        inputs = f.read().split(',')
    return list(map(int, inputs))


if __name__ == '__main__':
    print("Day 5:")

    part1_ans = int_code_computer(load_input(), 1)[1][-1]
    print("\tPart 1:", part1_ans)

    part2_ans = int_code_computer(load_input(), 5)[1][-1]
    print("\tPart 2:", part2_ans)
