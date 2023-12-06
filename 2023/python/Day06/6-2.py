import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(data):
    time = int(data[0].split(":")[1].strip().replace(" ", ""))
    dist = int(data[1].split(":")[1].strip().replace(" ", ""))

    total_wins = 0
    for ms in range(time):
        distance = (time - ms) * ms
        if distance > dist:
            total_wins += 1

    return total_wins


test_ans = run(load_input("test_input.txt"))
print(test_ans)
assert test_ans == 71503

ans = run(load_input("input.txt"))
assert ans == 26187338
print(ans)
