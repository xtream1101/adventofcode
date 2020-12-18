import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        data = f.read().splitlines()
    # return list(map(int, data))
    return data


def find_idx(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def do_eq(eq):
    # print("eq", eq)
    a, op, b = eq.split()
    ops = {
        '+': lambda a, b: a + b,
        '*': lambda a, b: a * b,
    }
    return ops[op](int(a), int(b))


def process_eq(full_eq):
    # print(f"process: {full_eq}")
    for op in ('+', '*'):
        while op in full_eq:
            full_eq = ' ' + full_eq + ' '
            # print("\nfull eq", full_eq)
            plus_idx = find_idx(full_eq, op)
            start = max(plus_idx[0]-2, 0)
            end = min(plus_idx[0]+3, len(full_eq))
            # get num until next space
            while full_eq[start] != ' ':
                start -= 1
            while full_eq[end] != ' ':
                end += 1

            start += 1
            ans = do_eq(full_eq[start:end])
            # print(f"{full_eq[start:end]} = {ans}")
            full_eq = full_eq.replace(full_eq[start:end], str(ans), 1).strip()

    return int(full_eq)


def run(exprs):
    total = 0
    for line_no, expr in enumerate(exprs):
        while '(' in expr:
            start_pren = find_idx(expr, '(')[-1]
            for i in find_idx(expr, ')'):
                if i > start_pren:
                    end_pren = i
                    break
            ans = process_eq(expr[start_pren+1:end_pren])
            # print(ans, expr[start_pren:end_pren+1])
            expr = expr.replace(expr[start_pren:end_pren+1], str(ans), 1)

        expr = process_eq(expr)
        total += int(expr)

    return total


test_ans = run(['1 + 2 * 3 + 4 * 5 + 6'])
# print(test_ans)
assert test_ans == 231

test_ans = run(['1 + (2 * 3) + (4 * (5 + 6))'])
# print(test_ans)
assert test_ans == 51

test_ans = run(['2 * 3 + (4 * 5)'])
# print(test_ans)
assert test_ans == 46

test_ans = run(['5 + (8 * 3 + 9 + 3 * 4 * 3)'])
# print(test_ans)
assert test_ans == 1445

test_ans = run(['5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'])
# print(test_ans)
assert test_ans == 669060

test_ans = run(['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'])
# print(test_ans)
assert test_ans == 23340


ans = run(load_input('input.txt'))
print(ans)
assert ans == 20394514442037

try:
    from aocd import submit
    submit(ans, part="b", day=18, year=2020)
except ModuleNotFoundError:
    print("Answer did not auto submit")
