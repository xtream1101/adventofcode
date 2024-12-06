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


def run_map(floor_map):
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
            guard_pos.append(((row.index(guard_direction), row_idx), guard_direction))
            # Set the guards starting direction
            while turn_order[0] != guard_direction:
                turn_order.rotate(-1)
            break  # there is only a single guard, so we can stop looking

    while True:
        # Used to step through the code
        # print_map(floor_map)
        # input()

        current_guard_pos = guard_pos[-1][0]
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
            return guard_pos, "off"

        if (next_pos, turn_order[0]) in guard_pos:
            return guard_pos, "loop"

        # Check if the block in front of the guard is blocked
        if floor_map[next_pos[1]][next_pos[0]] == "#":
            # Rotate the guard to the right
            turn_order.rotate(-1)
            floor_map[current_guard_pos[1]][current_guard_pos[0]] = turn_order[0]
            continue
        else:
            # Move the guard forward
            guard_pos.append((next_pos, turn_order[0]))
            # Update the map tiles
            floor_map[current_guard_pos[1]][current_guard_pos[0]] = "x"
            floor_map[next_pos[1]][next_pos[0]] = turn_order[0]


def run(data):
    # First run is to get all the guard positions
    floor_map = [list(row) for row in data]
    guard_pos, _ = run_map(floor_map)

    # Now loop over the postions in reverse order and add obstacles
    # Track which ones result in the guard getting stuck in a loop
    looped_obstacles = []

    srating_pos = guard_pos.pop(0)
    num_tries = 0
    for pos, _ in reversed(guard_pos):
        print(f"{num_tries}/{len(guard_pos)}")
        num_tries += 1
        floor_map = [list(row) for row in data]

        if pos == srating_pos[0]:
            # Not allowed to block the starting position
            continue
        floor_map[pos[1]][pos[0]] = "#"
        _, result = run_map(floor_map)
        if result == "loop":
            looped_obstacles.append(pos)
        #     # print_map(floor_map)
        #     print("Guard got stuck in a loop")
        # else:
        #     print("Guard was able to move")
        #     # print_map(floor_map)

    return len(set(looped_obstacles))


test_ans = run(load_input("test_input.txt"))
print(test_ans)
assert test_ans == 6

print("This will take about 20 minutes to finish")
ans = run(load_input("input.txt"))
assert ans == 1976
print(ans)
