import os
import sys
from rich import print
from collections import deque


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def print_map(data):
    print()
    for row in data:
        print("".join(row))
    print()


def run(data):
    floor_map = [list(row) for row in data]
    # Pos will be defined as (x, y) where x is the column and y is the row starting in the top left corner
    directions = {
        "^": (0, -1),
        "v": (0, 1),
        ">": (1, 0),
        "<": (-1, 0),
    }
    turn_order = deque(["^", ">", "v", "<"])
    # List of all positions of guard walked, last val in the list is the current pos
    guard_pos = []

    # Find guard pos in floor map
    for row_idx, row in enumerate(floor_map):
        found_pos = set(row).intersection(set(directions.keys()))
        if found_pos:
            guard_direction = found_pos.pop()
            guard_pos.append((row.index(guard_direction), row_idx))
            # Set the guards starting direction
            while turn_order[0] != guard_direction:
                turn_order.rotate(-1)
            break  # there is only a single guard, so we can stop looking

    while True:
        # Used to step through the code
        # print_map(floor_map)
        # input()

        current_guard_pos = guard_pos[-1]
        next_pos = (
            current_guard_pos[0] + directions[turn_order[0]][0],
            current_guard_pos[1] + directions[turn_order[0]][1],
        )
        # Is the next pos off the map
        if (
            next_pos[1] < 0
            or next_pos[0] < 0
            or next_pos[1] >= len(floor_map)
            or next_pos[0] >= len(floor_map[0])
        ):
            break

        # Check if the block in front of the guard is blocked
        if floor_map[next_pos[1]][next_pos[0]] == "#":
            # Rotate the guard to the right
            turn_order.rotate(-1)
            floor_map[current_guard_pos[1]][current_guard_pos[0]] = turn_order[0]
            continue
        else:
            # Move the guard forward
            guard_pos.append(next_pos)
            # Update the map tiles
            floor_map[current_guard_pos[1]][current_guard_pos[0]] = "x"
            floor_map[next_pos[1]][next_pos[0]] = turn_order[0]

    # Display the final map
    # print_map(floor_map)

    return len(set(guard_pos))


test_ans = run(load_input("test_input.txt"))
print(test_ans)
assert test_ans == 41

ans = run(load_input("input.txt"))
assert ans == 5564
print(ans)
