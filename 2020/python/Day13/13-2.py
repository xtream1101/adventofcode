import os
import sys
from sympy.ntheory.modular import crt


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        data = f.read().splitlines()
    return data


def run(b_ids_raw):
    b_ids = b_ids_raw.split(',')
    m = []
    v = []
    for idx, b_id in enumerate(b_ids):
        if b_id == 'x':
            continue
        b_id = int(b_id)
        m.append(b_id)
        v.append(idx)

    ans = crt(m, v)
    return abs(ans[0] - ans[1])


test_ans = run(load_input('test_input.txt')[1])
# print(test_ans)
assert test_ans == 1068781

test_ans = run('17,x,13,19')
# print(test_ans)
assert test_ans == 3417

test_ans = run('67,7,59,61')
# print(test_ans)
assert test_ans == 754018

test_ans = run('67,x,7,59,61')
# print(test_ans)
assert test_ans == 779210

test_ans = run('67,7,x,59,61')
# print(test_ans)
assert test_ans == 1261476

test_ans = run('1789,37,47,1889')
# print(test_ans)
assert test_ans == 1202161486

ans = run(load_input('input.txt')[1])
assert ans == 800177252346225
print(ans)

try:
    from aocd import submit
    submit(ans, part="b", day=13, year=2020)
except ModuleNotFoundError:
    print("Answer did not auto submit")
