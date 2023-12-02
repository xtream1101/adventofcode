import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(data):
    total_val = 0

    for line in data:
        game_num = int(line.split(": ")[0].replace("Game ", "").strip())
        game_failed = False
        for game_set in line.split(": ")[1].split("; "):
            for game in game_set.split(", "):
                num, color = game.split(" ")

                if (
                    (color == "red" and int(num) > 12)
                    or (color == "green" and int(num) > 13)
                    or (color == "blue" and int(num) > 14)
                ):
                    game_failed = True
                    break
            if game_failed:
                break

        if not game_failed:
            total_val += game_num

    return total_val


test_ans = run(load_input("test_input.txt"))
print(test_ans)
assert test_ans == 8

ans = run(load_input("input.txt"))
assert ans == 2593
print(ans)
