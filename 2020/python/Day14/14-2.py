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

        mem = action[4:-1]
        mem_value = list(f"{int(mem):b}".zfill(36))

        for i in range(36):
            if mask[i] != '0':
                mem_value[i] = mask[i]

        x = '1' * mem_value.count('X')
        for i in range(int(x, 2)+1):
            new_val = mem_value.copy()
            floats = f"{int(i):b}".zfill(mem_value.count('X'))
            for f in floats:
                new_val[new_val.index('X')] = f
            memory[int(''.join(new_val), 2)] = int(value)

    return sum(memory.values())


test_ans = run(load_input('test_input_2.txt'))
# print(test_ans)
assert test_ans == 208

ans = run(load_input('input.txt'))
assert ans == 4466434626828
print(ans)

try:
    from aocd import submit
    submit(ans, part="b", day=14, year=2020)
except ModuleNotFoundError:
    print("Answer did not auto submit")
