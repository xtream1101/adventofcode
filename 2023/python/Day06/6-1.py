import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(data):
    total_val = 1
    times = list(map(int, data[0].split(":")[1].strip().split()))
    dist = list(map(int, data[1].split(":")[1].strip().split()))

    for i in range(len(times)):
        total_wins = 0
        for ms in range(times[i]):
            distance = (times[i] - ms) * ms
            if distance > dist[i]:
                total_wins += 1
        total_val *= total_wins

    return total_val


test_ans = run(load_input("test_input.txt"))
print(test_ans)
assert test_ans == 288

ans = run(load_input("input.txt"))
assert ans == 440000
print(ans)
