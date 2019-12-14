import os
import time
from collections import Counter
os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Day2.final import IntCodeComputer  # noqa: E402
import sys,tty,termios


def load_input():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_file) as f:
        inputs = f.read().split(',')
    return list(map(int, inputs))


def manual_joystick():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(3)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    key_codes = {
        '\x1b[D': -1,
        '\x1b[C': 1,
        '\x1b[B': 0,
    }
    return key_codes[ch]


player_score = None

TILES = {
    0: ' ',
    1: '#',
    2: '*',
    3: '^',
    4: 'o',
}


def find_tile_pos(screen, tile_id):
    for y, row in enumerate(screen):
        for x, col in enumerate(row):
            if col == TILES[tile_id]:
                return (x, y)


def auto_joystick(last_ball_pos, last_paddle_pos):
    if last_ball_pos is None or last_paddle_pos is None:
        return 0

    if last_ball_pos[0] > last_paddle_pos[0]:
        return 1
    else:
        return -1


# Found size from part 1 using max x and max y value
cols = 39
rows = 23
screen = [[' '] * (cols + 1) for i in range(rows + 1)]
last_ball_pos = None
last_paddle_pos = None
program = load_input()
program[0] = 2
process = IntCodeComputer(program)
while process.last_optcode != 99:
    # joystick = manual_joystick()  # Use arrow keys to move, down to stay still, any other key to quit
    joystick = auto_joystick(last_ball_pos, last_paddle_pos)  # Game will play itself
    process.run(joystick)
    while process.outputs:
        x = process.outputs.pop(0)
        y = process.outputs.pop(0)
        tile_id = process.outputs.pop(0)

        if x == -1 and y == 0:
            player_score = tile_id
        else:
            if tile_id == 4:
                last_ball_pos = (x, y)
            if tile_id == 3:
                last_paddle_pos = (x, y)
            screen[y][x] = TILES[tile_id]
    time.sleep(.025)

    # Render game screen
    print(chr(27) + "[2J")  # clear terminal
    for row in screen:
        print(''.join(row))

    print("Score:", player_score)
