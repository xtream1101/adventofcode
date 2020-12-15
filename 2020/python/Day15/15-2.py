

def run(numbers):
    numbers = list(map(int, numbers.split(',')))
    idx = len(numbers)
    last_num = numbers[-1]
    seen_numbers = {}

    for i, num in enumerate(numbers):
        seen_numbers[num] = i

    while idx != 30000000:
        if last_num not in seen_numbers:
            current_num = 0
        else:
            current_num = idx - seen_numbers[last_num] - 1

        seen_numbers[last_num] = idx - 1
        last_num = current_num
        idx += 1

        if idx % 1000 == 0:
            print(idx, end='\r')

    print()
    return last_num


test_ans = run('0,3,6')
# print(test_ans)
assert test_ans == 175594

ans = run('11,18,0,20,1,7,16')
print(ans)
assert ans == 266

try:
    from aocd import submit
    submit(ans, part="b", day=15, year=2020)
except ModuleNotFoundError:
    print("Answer did not auto submit")
