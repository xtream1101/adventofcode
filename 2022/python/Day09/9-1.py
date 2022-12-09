import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def print_field(field):
    for y in reversed(field):
        for x in y:
            print(x, end='')
        print()


def run(motion, debug=False):
    total_val = 0

    head_moves = [(0,0)]
    t_moves = [(0,0)]

    for action in motion:
        match action.split():
            case ["R", amount]:
                move = (0, int(int(amount)))
                move_dir = 1
            case ["L", amount]:
                move = (0, int(amount))
                move_dir = -1
            case ["D", amount]:
                move = (int(amount), 0)
                move_dir = -1
            case ["U", amount]:
                move = (int(amount), 0)
                move_dir = 1

        for i in range(max(move)):
            if debug:
                field_size = (5,6)
                field = [['.' for col in range(field_size[1])] for row in range(field_size[0])]
                field[0][0] = 's'  # Starting point

            if move[0]:  # y axis
                new_pos = (head_moves[-1][0] + 1* move_dir, head_moves[-1][1])
            elif move[1]:  # x axis
                new_pos = (head_moves[-1][0], head_moves[-1][1] + 1* move_dir)

            # If H is at least 1 block away, then move T to previous H
            if (abs(new_pos[0] - t_moves[-1][0]) > 1 or abs(new_pos[1] - t_moves[-1][1]) > 1):
                t_moves.append(head_moves[-1])
            head_moves.append(new_pos)

            if debug:
                field[new_pos[0]][new_pos[1]] = 'H'
                field[t_moves[-1][0]][t_moves[-1][1]] = 'T'
                print_field(field)
                input()


    if debug:
        field = [['.' for col in range(field_size[1])] for row in range(field_size[0])]
        for pos in set(t_moves):
            field[pos[0]][pos[1]] = '#'
        print_field(field)

    return len(set(t_moves))


test_ans = run(load_input('test_input.txt'), debug=True)
print(test_ans)
assert test_ans == 13

ans = run(load_input('input.txt'))
assert ans == 6236
print(ans)
