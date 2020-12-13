import os
import sys


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        data = f.read().splitlines()
    # return list(map(int, data))
    return data


def get_key(my_dict, val):
    for key, value in my_dict.items():
        if val == value:
            return key


def run(notes):
    my_ts = int(notes[0])
    b_ids = notes[1].split(',')

    bus_times = {}
    for b_id in b_ids:
        if b_id == 'x':
            continue
        b_id = int(b_id)
        next_time_diff = b_id - (my_ts % b_id)
        bus_times[b_id] = my_ts + next_time_diff

    return (min(bus_times.values()) - my_ts) * get_key(bus_times, min(bus_times.values()))


test_ans = run(load_input('test_input.txt'))
# print(test_ans)
assert test_ans == 295

ans = run(load_input('input.txt'))
assert ans == 3966
print(ans)

try:
    from aocd import submit
    submit(ans, part="a", day=13, year=2020)
except ModuleNotFoundError:
    print("Answer did not auto submit")
