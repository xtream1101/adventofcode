import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(tree_map):
    forest_width = len(tree_map[0])
    forest_height = len(tree_map)
    scenic_scores = {}
    for x in range(forest_width):
        for y in range(forest_height):

            if x in (0, forest_width-1) or y in (0, forest_height-1):
                # Edges always have a view distance of 0
                scenic_scores[(y, x)] = 0
                continue

            current_height = tree_map[y][x]
            scenic_score = 1  # Start at 1 since we are multiplying values
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                check_loc = [y, x]
                view_dist = 0
                while True:
                    try:
                        check_loc[0] = check_loc[0] + direction[0]
                        check_loc[1] = check_loc[1] + direction[1]
                        # Test index within range
                        check_tree = tree_map[check_loc[0]][check_loc[1]]
                        if -1 in check_loc:
                            break

                        view_dist += 1
                        if current_height <= check_tree:
                            break

                    except IndexError:
                        break

                scenic_score *= view_dist

            scenic_scores[(y, x)] = scenic_score

    return max(scenic_scores.values())


test_ans = run(load_input('test_input.txt'))
print(test_ans)
assert test_ans == 8

ans = run(load_input('input.txt'))
assert ans == 517440
print(ans)
