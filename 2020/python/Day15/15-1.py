
def run(numbers):
    numbers = numbers.split(',')
    while len(numbers) != 2020:
        last_num = numbers[-1]
        if last_num not in numbers[:-1]:
            numbers.append('0')
        else:
            next_num = str(numbers[::-1][1:].index(last_num)+1)
            numbers.append(next_num)

    return numbers[-1]


test_ans = run('0,3,6')
# print(test_ans)
assert test_ans == '436'

ans = run('11,18,0,20,1,7,16')
print(ans)
assert ans == '639'

try:
    from aocd import submit
    submit(ans, part="a", day=15, year=2020)
except ModuleNotFoundError:
    print("Answer did not auto submit")
