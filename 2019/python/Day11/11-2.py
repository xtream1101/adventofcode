import os
import copy
os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Day2.final import IntCodeComputer  # noqa: E402


BLACK = ' '
WHITE = '#'


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


def move_robot(hull, current_pos, direction):
    hull = copy.deepcopy(hull)
    shift = {
        # (x, y)
        '^': (0, -1),
        '>': (1, 0),
        'v': (0, 1),
        '<': (-1, 0),
    }
    new_pos_x = current_pos[0] + shift[direction][0]
    new_pos_y = current_pos[1] + shift[direction][1]
    # Check if out of bounds
    if new_pos_y < 0:
        # Hit top wall, add new row to the top and set pos to that edge
        new_pos_y = 0
        hull.insert(0, [BLACK] * len(hull[0]))

    elif new_pos_y >= len(hull):
        # Hit bottom, add new row to the bottom
        hull.append([BLACK] * len(hull[0]))

    elif new_pos_x < 0:
        # Hit left wall, add new col on the left and set pos to that edge
        new_pos_x = 0
        for idx, row in enumerate(hull.copy()):
            hull[idx].insert(0, BLACK)

    elif new_pos_x >= len(hull[0]):
        # Hit right wall, add new col on the right
        for idx, row in enumerate(hull.copy()):
            hull[idx].append(BLACK)

    # print(hull, (new_pos_x, new_pos_y))
    return hull, (new_pos_x, new_pos_y)


test_hull = [
    [BLACK, BLACK],
    [BLACK, BLACK],
]
# Move top edge
assert move_robot(test_hull, (0, 0), '^') == ([[BLACK, BLACK], [BLACK, BLACK], [BLACK, BLACK]], (0, 0))
# Move up
assert move_robot(test_hull, (1, 1), '^') == ([[BLACK, BLACK], [BLACK, BLACK]], (1, 0))
# Move right edge
assert move_robot(test_hull, (1, 1), '>') == ([[BLACK, BLACK, BLACK], [BLACK, BLACK, BLACK]], (2, 1))
# Move right
assert move_robot(test_hull, (0, 0), '>') == ([[BLACK, BLACK], [BLACK, BLACK]], (1, 0))
# Move bottom edge
assert move_robot(test_hull, (0, 1), 'v') == ([[BLACK, BLACK], [BLACK, BLACK], [BLACK, BLACK]], (0, 2))
# Move down
assert move_robot(test_hull, (0, 0), 'v') == ([[BLACK, BLACK], [BLACK, BLACK]], (0, 1))
# Move left edge
assert move_robot(test_hull, (0, 0), '<') == ([[BLACK, BLACK, BLACK], [BLACK, BLACK, BLACK]], (0, 0))
# Move left
assert move_robot(test_hull, (1, 1), '<') == ([[BLACK, BLACK], [BLACK, BLACK]], (0, 1))


def get_panel_color(hull, pos):
    return 1 if hull[pos[1]][pos[0]] == WHITE else 0


def paint_panel(hull, color, panel):
    hull[panel[1]][panel[0]] = BLACK if paint == 0 else WHITE
    return hull


hull = [
    [WHITE]
]
robot_pos = (0, 0)
robot_dir = get_direction(None)
process = IntCodeComputer(load_input())
camera_input = 1  # Start on white panel this time
while process.last_optcode != 99:
    # Get color of panel
    camera_input = get_panel_color(hull, robot_pos)
    process.run(camera_input)
    paint, dir_output = process.outputs[-2:]
    # Paint panel
    hull = paint_panel(hull, paint, robot_pos)
    # Turn
    robot_dir = get_direction(robot_dir, dir_output)
    # And move
    hull, robot_pos = move_robot(hull, robot_pos, robot_dir)


for row in hull:
    print(''.join(row))
