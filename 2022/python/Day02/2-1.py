import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return list(lines)


def run(guide):
    """
    A = Rock
    B = Paper
    C = Scissor

    X = Rock
    Y = Paper
    Z = Scissor

    Lose = 0
    Draw/tie = 3
    Win = 6

    Rock = 1
    Paper = 2
    Scissor = 3
    """
    total_score = 0

    move_points = {
        "A X": 3 + 1,
        "A Y": 6 + 2,
        "A Z": 0 + 3,
        "B X": 0 + 1,
        "B Y": 3 + 2,
        "B Z": 6 + 3,
        "C X": 6 + 1,
        "C Y": 0 + 2,
        "C Z": 3 + 3,
    }

    for game in guide:
        total_score += move_points[game]

    return total_score




test_ans = run(load_input('test_input.txt'))
print(test_ans)
assert test_ans == 15

ans = run(load_input('input.txt'))
assert ans == 12586

print(ans)
