import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        report = f.read().splitlines()
    return report


def process_boarding_pass(bp):
    rows = list(range(0, 128))
    columns = list(range(0, 8))
    for letter in bp:
        row_middle = int(len(rows)/2)
        col_middle = int(len(columns)/2)
        if letter == 'F':
            rows = rows[:row_middle]
        elif letter == 'B':
            rows = rows[row_middle:]
        elif letter == 'R':
            columns = columns[col_middle:]
        elif letter == 'L':
            columns = columns[:col_middle]

    return rows[0] * 8 + columns[0]


def run(boarding_passes):
    seats = []
    for bp in boarding_passes:
        seats.append(process_boarding_pass(bp))

    seats.sort()

    for seat in range(seats[0], seats[-1]):
        if seat not in seats:
            if seat + 1 in seats and seat - 1 in seats:
                return seat


ans = run(load_input('input.txt'))
assert ans == 557

print(ans)
