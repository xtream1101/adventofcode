import os
import sys
from rich import print

def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines

def print_pipes(map, path):
    for r_idx, r in enumerate(map):
        for c_idx, c in enumerate(r):
            if (r_idx, c_idx) == path[-1]:
                print(f'[blue]{c}[/blue]', end='')
            elif (r_idx, c_idx) in path:
                print(f'[red]{c}[/red]', end='')
            else:
                print(c, end='')
        print()

def run(data):
    total_val = 0

    check_dirs = {
        # (y, x) == (r, c)
        '|': ((-1, 0), (1, 0)),  # N, S
        '-': ((0, 1), (0, -1)),  # E, W
        'L': ((-1, 0), (0, 1)),   # N, E
        'J': ((-1, 0), (0, -1)),  # N, W
        '7': ((1, 0), (0, -1)), # S, W
        'F': ((1, 0), (0, 1)),  # S, E
    }
    start_loc = None
    for r_idx, r in enumerate(data):
        if 'S' in r:
            start_loc = (r_idx, r.index('S'))
            # find what pipe piece S is
            start_dir = None
            if r_idx != 0 and data[r_idx - 1][start_loc[1]] in ('|', '7', 'F'):
                # Checks North for south facing pipes
                start_dir = (r_idx - 1, start_loc[1])
            elif r_idx != len(data) - 1 and data[r_idx + 1][start_loc[1]] in ('|', 'L', 'J'):
                # Checks South for North facing pipes
                start_dir = (r_idx + 1, start_loc[1])
            elif start_loc[1] != 0 and data[r_idx][start_loc[1] - 1] in ('-', 'L', '7'):
                # Checks West for East facing pipes
                start_dir = (r_idx, start_loc[1] - 1)
            elif start_loc[1] != len(r) - 1 and data[r_idx][start_loc[1] + 1] in ('-', 'J', 'F'):
                # Checks East for West facing pipes
                start_dir = (r_idx, start_loc[1] + 1)
            break

    pipe_path = [start_loc, start_dir]

    # print_pipes(data, pipe_path)
    while pipe_path[0] != pipe_path[-1]:
        # input()
        y, x = pipe_path[-1]
        current_pipe = check_dirs[data[y][x]]
        # Only 1 way to go, because we came from the other direction
        if (current_pipe[0][0] + y, current_pipe[0][1] + x) == pipe_path[-2]:
            pipe_path.append((current_pipe[1][0] + y, current_pipe[1][1] + x))
        else:
            pipe_path.append((current_pipe[0][0] + y, current_pipe[0][1] + x))

        # print(pipe_path)
        # print_pipes(data, pipe_path)

    # print(pipe_path)

    return int((len(pipe_path)-1)/2)


test_ans = run(load_input('test_input.txt'))
print(test_ans)
assert test_ans == 4

test_ans = run(load_input('test_input_2.txt'))
print(test_ans)
assert test_ans == 8

ans = run(load_input('input.txt'))
assert ans == 6907
print(ans)
