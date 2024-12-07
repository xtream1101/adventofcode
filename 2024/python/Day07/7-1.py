import os
import sys
from rich import print
import itertools


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(data):
    total_val = 0

    for eq in data:
        output, inputs = eq.split(": ")
        output = int(output)
        inputs = list(map(int, inputs.split(" ")))

        combos_to_test = [
            i for i in itertools.product(["+", "*"], repeat=len(inputs) - 1)
        ]
        for combo in combos_to_test:
            result = [None] * (len(inputs) + len(combo))
            result[::2] = inputs
            result[1::2] = combo

            total = result[0]
            for i in range(1, len(result), 2):
                if result[i] == "+":
                    total += result[i + 1]
                elif result[i] == "*":
                    total *= result[i + 1]

            if total == output:
                total_val += output
                break

    return total_val


test_ans = run(load_input("test_input.txt"))
print(test_ans)
assert test_ans == 3749

ans = run(load_input("input.txt"))
assert ans == 1153997401072
print(ans)
