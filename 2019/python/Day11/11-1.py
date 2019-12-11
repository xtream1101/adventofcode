import os
os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Day2.final import IntCodeComputer  # noqa: E402


def load_input():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_file) as f:
        inputs = f.read().split(',')
    return list(map(int, inputs))



def get_direction(prev_direction, output=None):
    directions = '<^>v'
    if output is None:
        return '^'

    prev_idx = directions.index(prev_direction)
    if output == 1:
        new_idx = 0 if prev_idx + 1 >= len(directions) else prev_idx + 1
        return directions[new_idx]

    elif output == 0:
        return directions[prev_idx - 1]


# Clockwise
assert get_direction(None) == '^'
assert get_direction('^', 1) == '>'
assert get_direction('>', 1) == 'v'
assert get_direction('v', 1) == '<'
assert get_direction('<', 1) == '^'
# Counter-clockwise
assert get_direction('^', 0) == '<'
assert get_direction('<', 0) == 'v'
assert get_direction('v', 0) == '>'
assert get_direction('>', 0) == '^'


def move_robot(current_pos, direction):
    shift = {
        # (x, y)
        '^': (0, -1),
        '>': (1, 0),
        'v': (0, 1),
        '<': (-1, 0),
    }
    # (x, y)
    return (current_pos[0] + shift[direction][0], current_pos[1] + shift[direction][1])


assert move_robot((2, 2), '^') == (2, 1)
assert move_robot((2, 2), '>') == (3, 2)
assert move_robot((2, 2), 'v') == (2, 3)
assert move_robot((2, 2), '<') == (1, 2)

panels = {}
robot_pos = (0, 0)
robot_dir = get_direction(None)
process = IntCodeComputer(load_input())
while process.last_optcode != 99:
    camera_input = 1 if panels.get(robot_pos) == '#' else 0
    process.run(camera_input)
    paint, dir_output = process.outputs[-2:]
    # print(panels)
    # _ = input('...')
    # Paint panel
    panels[robot_pos] = '.' if paint == 0 else '#'
    # Turn
    robot_dir = get_direction(robot_dir, dir_output)
    # And move
    robot_pos = move_robot(robot_pos, robot_dir)



print(len(panels))
