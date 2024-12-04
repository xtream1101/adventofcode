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

    # Find the word in the wordsearch grid
    rows = len(word_search)
    cols = len(word_search[0])

    results = []

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if word_search[row][col] == "A":
                # Check if we have M's and S's in diagonal cross pattern

                ul = word_search[row - 1][col - 1]
                ur = word_search[row - 1][col + 1]
                dl = word_search[row + 1][col - 1]
                dr = word_search[row + 1][col + 1]

                d1 = (ul == "M" and dr == "S") or (ul == "S" and dr == "M")
                d2 = (ur == "M" and dl == "S") or (ur == "S" and dl == "M")

                if d1 is True and d2 is True:
                    results.append((row, col))

    return len(results)


test_ans = run(load_input("test_input.txt"))
print(test_ans)
assert test_ans == 9

ans = run(load_input("input.txt"))
assert ans == 1877
print(ans)
