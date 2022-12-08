import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def print_forest(tree_map, color1, color2):
    for y in range(len(tree_map)):
        for x in range(len(tree_map[0])):
            if (y,x) == tuple(color1):
                print(f"\033[91m{tree_map[y][x]}\033[0m", end='')
            elif (y,x) == tuple(color2):
                print(f"\033[93m{tree_map[y][x]}\033[0m", end='')
            else:
                print(tree_map[y][x], end='')
        print()


def run(tree_map):
    forest_width = len(tree_map[0])
    forest_height = len(tree_map)
    visible_trees = set()
    for x in range(forest_width):
        for y in range(forest_height):
            if x in (0, forest_width-1) or y in (0, forest_height-1):
                visible_trees.add((y, x))
                continue
            current_height = tree_map[y][x]

            is_visible = False
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                check_loc = [y, x]
                while True:
                    try:
                        check_loc[0] = check_loc[0] + direction[0]
                        check_loc[1] = check_loc[1] + direction[1]
                        if -1 in check_loc:
                            raise IndexError

                        # print((y,x), current_height, check_loc, tree_map[check_loc[0]][check_loc[1]])
                        # print_forest(tree_map, color1=(y,x), color2=check_loc)
                        # input()

                        if current_height > tree_map[check_loc[0]][check_loc[1]]:
                            continue
                        else:
                            break
                    except IndexError:
                        # Nothing larger or the same size were found
                        visible_trees.add((y, x))
                        is_visible = True
                        break
                if is_visible is True:
                    # No need to check other directions
                    break

    # Print colored map of seen trees
    # for y in range(len(tree_map)):
    #     for x in range(len(tree_map[0])):
    #         if (y,x) in visible_trees or x in (0, forest_width-1) or y in (0, forest_height-1):
    #             print(f"\033[91m{tree_map[y][x]}\033[0m", end='')
    #         else:
    #             print(tree_map[y][x], end='')
    #     print()

    return len(visible_trees)


test_ans = run(load_input('test_input.txt'))
print(test_ans)
assert test_ans == 21

ans = run(load_input('input.txt'))
assert ans == 1870
print(ans)
