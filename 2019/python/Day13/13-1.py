import os
from collections import Counter
os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Day2.final import IntCodeComputer  # noqa: E402


def load_input():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_file) as f:
        inputs = f.read().split(',')
    return list(map(int, inputs))


process = IntCodeComputer(load_input())
process.run()
screen = {}
while process.outputs:
    x = process.outputs.pop(0)
    y = process.outputs.pop(0)
    tile_id = process.outputs.pop(0)
    screen[(x, y)] = tile_id


print(Counter(screen.values())[2])
