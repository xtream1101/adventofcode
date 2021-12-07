import os
import sys
import statistics


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        pos = f.read().split(',')
    return list(map(int, pos))


def run(positions):
    current_lowest = None
    current_pos = int(statistics.mean(positions))
    starting_pos = current_pos
    for h_dir in [-1, 1]:
        while True:
            fuel_used = 0
            for pos in positions:
                fuel_used += abs(pos - current_pos)

            if current_lowest is None or fuel_used <= current_lowest:
                current_lowest = fuel_used
            else:
                current_pos = starting_pos + 1
                break
            current_pos += h_dir

    return current_lowest


test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 37

ans = run(load_input('input.txt'))
assert ans == 355989
print(ans)
