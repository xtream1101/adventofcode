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


def run(motion, debug=False, field_size=(0,0), start_offset=(0,0)):
    total_val = 0

    knots = 10
    # idx 0 is the head
    moves = [[(start_offset[0], start_offset[1])] for row in range(knots)]

    for action in motion:
        match action.split():
            case ["R", amount]:
                move = (0, int(amount))
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
                field = [['.' for col in range(field_size[1])] for row in range(field_size[0])]
                field[start_offset[0]][start_offset[1]] = 's'  # Starting point

            if move[0]:  # y axis
                new_pos = (moves[0][-1][0] + 1* move_dir, moves[0][-1][1])
            elif move[1]:  # x axis
                new_pos = (moves[0][-1][0], moves[0][-1][1] + 1* move_dir)

            moves[0].append(new_pos)

            # Have rope follow
            for i in range(1,knots):
                dk_y = moves[i-1][-1][0] - moves[i][-1][0]
                dk_x = moves[i-1][-1][1] - moves[i][-1][1]

                if abs(dk_y) > 1 or abs(dk_x) > 1:
                    ck_y, ck_x = moves[i][-1]

                    if abs(dk_x) > 0:
                        ck_x += 1 if dk_x > 0 else -1

                    if abs(dk_y) > 0:
                        ck_y += 1 if dk_y > 0 else -1

                    moves[i].append((ck_y, ck_x))

            if debug:
                field[moves[0][-1][0]][moves[0][-1][1]] = 'H'
                for i in reversed(range(1,knots)):
                    field[moves[i][-1][0]][moves[i][-1][1]] = i
                print_field(field)
                input()


    if debug:
        field = [['.' for col in range(field_size[1])] for row in range(field_size[0])]
        for pos in set(moves[-1]):
            field[pos[0]][pos[1]] = '#'
        print_field(field)

    return len(set(moves[-1]))


test_ans = run(load_input('test_input.txt'), debug=True, field_size=(5,6), start_offset=(0,0))
print(test_ans)
assert test_ans == 1

test_ans = run(load_input('test_input_2.txt'), debug=False, field_size=(22,27), start_offset=(6,12))
print(test_ans)
assert test_ans == 36

ans = run(load_input('input.txt'))
assert ans == 2449
print(ans)
