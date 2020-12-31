import os
import sys
import copy
import math
from pprint import pprint
from collections import defaultdict

def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        data = f.read().splitlines()
    # return list(map(int, data))
    return data


def load_tiles(tiles):
    parsed_tiles = {}
    for line in tiles:
        if line == '':
            continue

        if line.startswith('Tile'):
            tile_number = int(line.split(' ')[-1][:-1])
            parsed_tiles[tile_number] = []
        else:
            parsed_tiles[tile_number].append(list(line))

    return parsed_tiles


def get_edges(tiles):
    tile_edges = {}
    for tile_id, tile in tiles.items():
        tile_edges[tile_id] = {}
        # Top
        t = tile[0]
        tile_edges[tile_id]['t'] = tuple(t)
        # Top Flipped
        tf = t.copy()
        tf.reverse()
        tile_edges[tile_id]['tf'] = tuple(tf)

        # Right
        r = [r[-1] for r in tile]
        tile_edges[tile_id]['r'] = tuple(r)
        # Right Flipped
        rf = r.copy()
        rf.reverse()
        tile_edges[tile_id]['rf'] = tuple(rf)

        # Bottom
        b = tile[-1]
        tile_edges[tile_id]['b'] = tuple(b)
        # Bottom Flipped
        bf = b.copy()
        bf.reverse()
        tile_edges[tile_id]['bf'] = tuple(bf)

        # Left
        l = [r[0] for r in tile]
        tile_edges[tile_id]['l'] = tuple(l)
        # Left Flipped
        lf = l.copy()
        lf.reverse()
        tile_edges[tile_id]['lf'] = tuple(lf)

    return tile_edges


def run(tiles):
    tiles = load_tiles(tiles)
    tile_edges = get_edges(tiles)
    # check for edge overlaps
    idx = 0
    sides_match = defaultdict(lambda: 0)
    tile_ids = list(tile_edges.keys())
    for tile_id in tile_ids:
        for other_tile_id in tile_ids[idx + 1:]:
            print(tile_id, other_tile_id)
            if set(tuple(tile_edges[tile_id].values())).intersection(set(tuple(tile_edges[other_tile_id].values()))):
                # Count how many sides are matched
                sides_match[tile_id] += 1
                sides_match[other_tile_id] += 1
        idx += 1

    # the corners are the only ones with 2 matches
    return math.prod([key for (key, value) in sides_match.items() if value == 2])


test_ans = run(load_input('test_input.txt'))
assert test_ans == 20899048083289, test_ans

ans = run(load_input('input.txt'))
print(ans)
assert ans == 17148689442341

try:
    from aocd import submit
    submit(ans, part="a", day=20, year=2020)
except ModuleNotFoundError:
    print("Answer did not auto submit")
