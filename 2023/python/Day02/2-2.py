import os
import sys
from collections import defaultdict


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(data):
    total_val = 0

    for line in data:
        game_cubes = defaultdict(int)
        for game_set in line.split(": ")[1].split("; "):
            for game in game_set.split(", "):
                num, color = game.split(" ")
                game_cubes[color] = max(game_cubes[color], int(num))

        power = game_cubes["red"] * game_cubes["green"] * game_cubes["blue"]
        total_val += power

    return total_val


test_ans = run(load_input("test_input.txt"))
print(test_ans)
assert test_ans == 2286

ans = run(load_input("input.txt"))
assert ans == 54699
print(ans)
