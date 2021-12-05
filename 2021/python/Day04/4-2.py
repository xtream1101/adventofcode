import os
import sys
from collections import defaultdict


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def parse_game_data(game_data):
    game_input = None
    game_boards = defaultdict(list)
    board_idx = -1
    for line in game_data:
        if game_input is None:
            game_input = list(map(int, line.split(',')))
            continue

        if line == '':
            board_idx += 1
            continue

        game_boards[board_idx].append(list(map(int, line.split())))

    return game_input, game_boards


def check_board(board, num):
    for index, row in enumerate(board):
        if num in row:
            return index, row.index(num)
    return None, None


def run(game_data):
    game_input, game_boards = parse_game_data(game_data)
    # pprint(game_input)
    # pprint(game_boards)
    boards_won = set()
    total_boards = len(game_boards)
    for num in game_input:
        for board_idx, board in game_boards.items():
            row, col = check_board(board, num)
            if row is None:
                continue
            board[row][col] = None

            # Check col count
            if board[row].count(None) == 5 or sum([1 for b_row in game_boards[board_idx] if b_row[col] is None ]) == 5:
                boards_won.add(board_idx)
                if len(boards_won) == total_boards:
                    return sum([sum(filter(None, vals)) for vals in board]) * num


test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 1924

ans = run(load_input('input.txt'))
assert ans == 11377
print(ans)
