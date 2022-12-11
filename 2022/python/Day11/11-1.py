import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def lambda_operation(action):
    if action[1] == '+':
        if action[0] == 'old':
            if action[2] == 'old':
                return lambda x: x + x
            return lambda x: x + int(action[2])

    elif action[1] == '*':
        if action[0] == 'old':
            if action[2] == 'old':
                return lambda x: x * x
            return lambda x: x * int(action[2])


def run(data):
    monkeys = []
    curr_monkey = None
    for line in data:
        if 'Monkey' in line:
            curr_monkey = int(line.split(' ')[-1][:-1])
            monkeys.append({'inspect_count': 0})
        elif 'Starting items' in line:
            monkeys[curr_monkey]['items'] = list(map(int, line.split(':')[-1].split(', ')))
        elif 'Operation' in line:
            monkeys[curr_monkey]['inspect'] = lambda_operation(line.split('=')[-1].split())
        elif 'Test:' in line:
            monkeys[curr_monkey]['test'] = int(line.split()[-1])
        elif 'true' in line:
            monkeys[curr_monkey][True] = int(line.split()[-1])
        elif 'false' in line:
            monkeys[curr_monkey][False] = int(line.split()[-1])

    for r in range(20):
        for m_idx in range(len(monkeys)):
            monkey = monkeys[m_idx]
            while monkey['items']:
                item = monkey['items'].pop(0)
                worry_level = int(monkey['inspect'](item) / 3)
                monkey['inspect_count'] += 1
                test_outcome = not bool(worry_level % monkey['test'])
                pass_to = monkey[test_outcome]
                monkeys[pass_to]['items'].append(worry_level)
                # print(f"M{m_idx} - I:{item} - WL:{worry_level} - {test_outcome} - PT:")
                # input()

        # print("Round:", r)
        # for monkey in monkeys:
        #     print(monkey['items'])
        # input()

    inspect_counts = sorted([m['inspect_count'] for m in monkeys])
    return inspect_counts[-1] * inspect_counts[-2]



test_ans = run(load_input('test_input.txt'))
print(test_ans)
assert test_ans == 10605

ans = run(load_input('input.txt'))
assert ans == 56350
print(ans)
