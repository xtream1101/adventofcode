from collections import Counter


def load_input():
    return 254032, 789860


def gen_codes():
    for a in range(10):
        for b in range(a, 10):
            for c in range(b, 10):
                for d in range(c, 10):
                    for e in range(d, 10):
                        for f in range(e, 10):
                            yield f"{a}{b}{c}{d}{e}{f}"


def check_dup_chars(code_str):
    return 2 in Counter(code_str).values()


def part1(min_num, max_num):
    count = 0
    for code_str in gen_codes():
        code = int(code_str)
        if code > min_num and code < max_num and len(set(code_str)) < 6:
            count += 1

    return count


def part2(min_num, max_num):
    count = 0
    for code_str in gen_codes():
        code = int(code_str)
        if code > min_num and code < max_num and len(set(code_str)) < 6:
            if check_dup_chars(code_str):
                count += 1

    return count


if __name__ == '__main__':
    print("Day 4:")

    part1_ans = part1(*load_input())
    print("\tPart 1:", part1_ans)
    assert part1_ans == 1033

    part2_ans = part2(*load_input())
    print("\n\tPart 2:", part2_ans)
    assert part2_ans == 670
