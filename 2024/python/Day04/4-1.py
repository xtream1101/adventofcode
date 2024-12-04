import os
import sys
from rich import print


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(data):
    word_search = []
    for row in data:
        word_search.append(row)

    word = "XMAS"
    # Find the word in the wordsearch grid
    rows = len(word_search)
    cols = len(word_search[0])

    # All 8 possible directions
    directions = [
        (-1, -1),  # Up-left
        (-1, 0),  # Up
        (-1, 1),  # Up-right
        (0, -1),  # Left
        (0, 1),  # Right
        (1, -1),  # Down-left
        (1, 0),  # Down
        (1, 1),  # Down-right
    ]

    def check_direction(row, col, d_row, d_col):
        """Check if word exists starting at (row, col) going in direction (d_row, d_col)"""

        # Check if we are out of bounds in the grid
        if (
            row + d_row * (len(word) - 1) < 0
            or row + d_row * (len(word) - 1) >= rows
            or col + d_col * (len(word) - 1) < 0
            or col + d_col * (len(word) - 1) >= cols
        ):
            return False

        for i in range(len(word)):
            if word_search[row + d_row * i][col + d_col * i] != word[i]:
                return False
        return True

    results = []

    # Check each starting position
    for row in range(rows):
        for col in range(cols):
            # Try each direction
            for d_row, d_col in directions:
                if check_direction(row, col, d_row, d_col):
                    results.append(((row, col), (d_row, d_col)))

    return len(results)


test_ans = run(load_input("test_input.txt"))
print(test_ans)
assert test_ans == 18

ans = run(load_input("input.txt"))
assert ans == 2462
print(ans)
