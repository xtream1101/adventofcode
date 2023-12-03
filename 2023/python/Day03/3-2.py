import os
import sys
from collections import defaultdict

def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines

# has bug where it will not care about the last number in the column in the very last row, but input does not have that so not an issue
def run(data):
    total_val = 0
    curr_num = ''
    is_part_num = False
    seen_gears = set()

    # store the gear location as key and a list of parts it was found near
    gears = defaultdict(list)

    for r_idx, r in enumerate(data):
        for c_idx, c in enumerate(r):
            print(f"r_idx: {r_idx}, c_idx: {c_idx}, c: {c}, curr_num: {curr_num}")
            if c_idx == 0 or not c.isdigit():
                # print(c, curr_num, c_idx)
                if curr_num:

                    # Check if its a part number
                    if is_part_num:
                        print('Part number: ', curr_num)
                        # input()
                        # total_val += int(curr_num)
                        is_part_num = False
                        for g in seen_gears:
                            gears[g].append(int(curr_num))

                    else:
                        print('NO: ', curr_num)
                    curr_num = ''
                    seen_gears = set()


            if c.isdigit():
                curr_num += c

            if not c.isdigit():
                continue

            if r_idx > 0:
                # check up
                if data[r_idx - 1][c_idx] != '.' and not data[r_idx - 1][c_idx].isdigit():
                    is_part_num = True
                    if data[r_idx - 1][c_idx] == '*':
                        seen_gears.add((r_idx - 1, c_idx))
                    continue

                # check up left
                if c_idx > 0 and data[r_idx - 1][c_idx - 1] != '.' and not data[r_idx - 1][c_idx - 1].isdigit():
                    is_part_num = True
                    if data[r_idx - 1][c_idx - 1] == '*':
                        seen_gears.add((r_idx - 1, c_idx - 1))
                    continue

                # check up right
                if c_idx < len(r) - 1 and data[r_idx - 1][c_idx + 1] != '.' and not data[r_idx - 1][c_idx + 1].isdigit():
                    is_part_num = True
                    if data[r_idx - 1][c_idx + 1] == '*':
                        seen_gears.add((r_idx - 1, c_idx + 1))
                    continue


            if r_idx < len(data) - 1:
                # check down
                if data[r_idx + 1][c_idx] != '.' and not data[r_idx + 1][c_idx].isdigit():
                    is_part_num = True
                    if data[r_idx + 1][c_idx] == '*':
                        seen_gears.add((r_idx + 1, c_idx))
                    continue

                # check down left
                if c_idx > 0 and data[r_idx + 1][c_idx - 1] != '.' and not data[r_idx + 1][c_idx - 1].isdigit():
                    is_part_num = True
                    if data[r_idx + 1][c_idx - 1] == '*':
                        seen_gears.add((r_idx + 1, c_idx - 1))
                    continue

                # check down right
                if c_idx < len(r) - 1 and data[r_idx + 1][c_idx + 1] != '.' and not data[r_idx + 1][c_idx + 1].isdigit():
                    is_part_num = True
                    if data[r_idx + 1][c_idx + 1] == '*':
                        seen_gears.add((r_idx + 1, c_idx + 1))
                    continue

            # check left
            if c_idx > 0 and data[r_idx][c_idx - 1] != '.' and not data[r_idx][c_idx - 1].isdigit():
                is_part_num = True
                if data[r_idx][c_idx - 1] == '*':
                    seen_gears.add((r_idx, c_idx - 1))
                continue

            # check right
            if c_idx < len(r) - 1 and data[r_idx][c_idx + 1] != '.' and not data[r_idx][c_idx + 1].isdigit():
                is_part_num = True
                if data[r_idx][c_idx + 1] == '*':
                    seen_gears.add((r_idx, c_idx + 1))
                continue

    print(gears)
    for g in gears:
        if len(gears[g]) == 2:
            total_val += gears[g][0] * gears[g][1]

    return total_val


test_ans = run(load_input('test_input.txt'))
print(test_ans)
assert test_ans == 467835

ans = run(load_input('input.txt'))
assert ans == 84900879
print(ans)
