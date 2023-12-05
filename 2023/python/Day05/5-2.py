import os
import sys
from rich import print
from collections import defaultdict


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def get_next_val(source_item, source_map):
    for source_range, dest_range in source_map.items():
        if source_item in range(*source_range):
            return source_item - source_range[0] + dest_range[0]
    return source_item


def run(data):

    almanac = {
        'seeds': [],
        'maps': defaultdict(dict),
        'output': {},
    }

    curr_map = None
    for line in data:
        if line.strip() == '':
            continue

        if line.startswith('seeds:'):
            raw_seeds = list(map(int, line.split(':')[-1].split()))
            s_iter = iter(raw_seeds)
            for s in s_iter:
                almanac['seeds'].append((s, next(s_iter)))
            continue

        if line.endswith('map:'):
            curr_map = line.split(' map:')[0]
            continue

        if curr_map:
            dest_start, source_start, range_len = [int(x) for x in line.split()]
            source = (source_start, source_start + range_len)
            dest = (dest_start, dest_start + range_len)
            almanac['maps'][curr_map][source] = dest
            continue

    smallest_location = None
    for seed_range in almanac['seeds']:
        print("Current Range: ", seed_range)
        for seed in range(seed_range[0], seed_range[0] + seed_range[1]):
            if seed % 1000000 == 0:
                print("Seed: ", seed)
            soil = get_next_val(seed, almanac['maps']['seed-to-soil'])
            fertilizer = get_next_val(soil, almanac['maps']['soil-to-fertilizer'])
            water = get_next_val(fertilizer, almanac['maps']['fertilizer-to-water'])
            light = get_next_val(water, almanac['maps']['water-to-light'])
            temperature = get_next_val(light, almanac['maps']['light-to-temperature'])
            humidity = get_next_val(temperature, almanac['maps']['temperature-to-humidity'])
            location = get_next_val(humidity, almanac['maps']['humidity-to-location'])

            # print(seed, location)

            if smallest_location is None:
                smallest_location = location
            else:
                smallest_location = min(smallest_location, location)

    return smallest_location


test_ans = run(load_input('test_input.txt'))
print(test_ans)
assert test_ans == 46

ans = run(load_input('input.txt'))
# assert ans == 0000
print(ans)
