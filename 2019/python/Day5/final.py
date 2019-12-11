import os
os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Day2.final import IntCodeComputer  # noqa: E402


def load_input():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_file) as f:
        inputs = f.read().split(',')
    return list(map(int, inputs))


if __name__ == '__main__':
    print("Day 5:")

    p1 = IntCodeComputer(load_input(), 1)
    p1.run()
    print("\tPart 1:", p1.outputs[-1])

    p2 = IntCodeComputer(load_input(), 5)
    p2.run()
    print("\tPart 2:", p2.outputs[-1])
