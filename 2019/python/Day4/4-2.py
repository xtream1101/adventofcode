import os
import sys


def check_code(code_str):
    code = int(code_str)
    if code > 284639 and code < 748759 and len(set(code_str)) < 6:
        current_dup_len = 0
        current_c = None
        dups = []
        for c in code_str:
            if current_c is None:
                current_c = c
                current_dup_len += 1
            else:
                if current_c == c:
                    current_dup_len += 1
                else:
                    dups.append(current_dup_len)
                    current_c = c
                    current_dup_len = 1

        # Get the last char checked
        dups.append(current_dup_len)
        if 2 in dups:
            return True

    return False

count = 0
for a in range(10):
    for b in range(a, 10):
        for c in range(b, 10):
            for d in range(c, 10):
                for e in range(d, 10):
                    for f in range(e, 10):
                        code_str = f"{a}{b}{c}{d}{e}{f}"

                        if check_code(code_str):
                            print(code_str)
                            count += 1

print(count)
