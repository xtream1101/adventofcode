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
    a, op, b = eq.split()
    ops = {
        '+': lambda a, b: a + b,
        '*': lambda a, b: a * b,
    }
    return ops[op](int(a), int(b))


def process_eq(full_eq):
    # print(f"process: {full_eq}")
    while ' ' in full_eq:
        full_eq = ' ' + full_eq + ' '
        # print("\nfull eq", full_eq)
        try:
            end_eq = find_idx(full_eq, ' ')[3]
        except IndexError:
            end_eq = len(full_eq)
        ans = do_eq(full_eq[:end_eq])
        # print(f"{full_eq[:end_eq]} = {ans}")
        full_eq = full_eq.replace(full_eq[:end_eq], str(ans), 1).strip()

    return int(full_eq)


def run(exprs):
    total = 0
    for line_no, expr in enumerate(exprs):
        # print(f"Orig: {expr}")
        # Find inner most ()
        while '(' in expr:
            start_pren = find_idx(expr, '(')[-1]
            for i in find_idx(expr, ')'):
                if i > start_pren:
                    end_pren = i
                    break
            ans = process_eq(expr[start_pren+1:end_pren])
            # print(f"{expr[start_pren:end_pren+1]} = {ans}")
            expr = expr.replace(expr[start_pren:end_pren+1], str(ans), 1)

        expr = process_eq(expr)
        total += int(expr)

    return total


# Prod edge case
test_ans = run(['4 * 6 + 3 * 6 + (9 + 5 * 3 * 7) * 6'])
assert test_ans == 2736, test_ans

test_ans = run(['1 + 2 * 3 + 4 * 5 + 6'])
assert test_ans == 71, test_ans

test_ans = run(['1 + (2 * 3) + (4 * (5 + 6))'])
assert test_ans == 51, test_ans

test_ans = run(['2 * 3 + (4 * 5)'])
assert test_ans == 26, test_ans

test_ans = run(['5 + (8 * 3 + 9 + 3 * 4 * 3)'])
assert test_ans == 437, test_ans

test_ans = run(['5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'])
assert test_ans == 12240, test_ans

test_ans = run(['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'])
assert test_ans == 13632, test_ans


ans = run(load_input('input.txt'))
print(ans)
assert ans == 650217205854

try:
    from aocd import submit
    submit(ans, part="a", day=18, year=2020)
except ModuleNotFoundError:
    print("Answer did not auto submit")
