import os
import sys
from collections import defaultdict

def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(terminal):
    current_dir = []
    dir_sizes = defaultdict(lambda:0)
    for line in terminal:
        match line.split():
            case ['$', 'cd', folder]:
                if folder == '..':
                    current_dir = current_dir[:-1]
                else:
                    slash = '' if folder == '/' else '/'
                    current_dir.append(f"{folder}{slash}")
            case ['$', 'ls']:
                pass
            case ['dir', folder]:
                pass
            case [file_size, file_name]:
                dir_sizes[''.join(current_dir)] += int(file_size)
                # Add size to parent dirs
                for i in reversed(range(1, len(current_dir))):
                    dir_sizes[''.join(current_dir[:i])] += int(file_size)
            case _:
                print('Command not recognized')

    total_size = 0
    for path, size in dir_sizes.items():
        if size <= 100000:
            total_size += size
    return total_size

test_ans = run(load_input('test_input.txt'))
print(test_ans)
assert test_ans == 95437

ans = run(load_input('input.txt'))
assert ans == 1086293
print(ans)
