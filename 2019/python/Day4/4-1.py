import os
import sys


count = 0
for a in range(10):
    for b in range(a, 10):
        for c in range(b, 10):
            for d in range(c, 10):
                for e in range(d, 10):
                    for f in range(e, 10):
                        code_str = f"{a}{b}{c}{d}{e}{f}"
                        code = int(code_str)
                        if code > 254032 and code < 789860 and len(set(code_str)) < 6:
                            count += 1
print(count)
