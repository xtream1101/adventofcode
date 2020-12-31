import os
import sys
from pprint import pprint


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        data = f.read().splitlines()
    # return list(map(int, data))
    return data



def expand_rule(rules, r_id):
    # print(r_id, rules)
    compiled_rules = set()

    if len(rules[r_id]) == 1:
        # print("sadasdas", rules[r_id])
        return [rules[r_id][0]]

    for option in rules[r_id].split(' | '):
        compiled_rule = ['']
        for rule in option.split(' '):
            # print("rule", rule, compiled_rule)
            rule_options = expand_rule(rules, rule)
            current_compiled_rules = compiled_rule.copy()
            compiled_rule = []
            for c_rule in current_compiled_rules:
                rule_orig = c_rule
                for r_opt in rule_options:
                    compiled_rule.append(rule_orig + r_opt)


            # print("asdsd", abc)
            # compiled_rule += abc

        compiled_rules.update(compiled_rule)

    return compiled_rules


def run(messages):
    rules = {}
    is_rule = True
    total = 0
    for message in messages:
        if message == '':
            # pprint(rules)
            is_rule = False
            compiled_rules = expand_rule(rules, '0')
            # pprint(compiled_rules)
            continue

        if is_rule is True:
            num, rule = message.split(': ')
            rules[num] = rule.replace('"', '')
            # rules[num] = rule.split(' | ')
        else:
            # print(message)
            if message in compiled_rules:
                total += 1
            # input()

    return total

test_ans = run(load_input('test_input.txt'))
assert test_ans == 2, test_ans

ans = run(load_input('input.txt'))
print(ans)
# assert ans == 19087

try:
    from aocd import submit
    submit(ans, part="a", day=19, year=2020)
except ModuleNotFoundError:
    print("Answer did not auto submit")
