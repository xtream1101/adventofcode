import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        data = f.read().splitlines()
    # return list(map(int, data))
    return data


def run(program):
    memory = {}
    mask = None
    for line in program:
        action, value = line.split(' = ')
        if action == 'mask':
            mask = list(value)
            continue

        value = list(f"{int(value):b}".zfill(36))
        mem = action[4:-1]

        new_value = []
        for i in range(36):
            if mask[i] != 'X':
                new_value.append(mask[i])
            else:
                new_value.append(value[i])
        memory[mem] = int(''.join(new_value), 2)

    return sum(memory.values())


test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 165

ans = run(load_input('input.txt'))
assert ans == 12408060320841
print(ans)

try:
    from aocd import submit
    submit(ans, part="a", day=14, year=2020)
except ModuleNotFoundError:
    print("Answer did not auto submit")
