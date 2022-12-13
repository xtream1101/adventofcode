import ast
import os
import sys
import functools


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def compare(left_packet, right_packet):
    # print(f"Test {left_packet} <= {right_packet}")

    if isinstance(left_packet, int) and isinstance(right_packet, int):
        # print("r1", None if left_packet == right_packet else left_packet <= right_packet)
        return None if left_packet == right_packet else left_packet <= right_packet

    if isinstance(left_packet, list) and isinstance(right_packet, list):
        for i, lp in enumerate(left_packet):
            try:
                rp = right_packet[i]
            except IndexError:
                return False
            cv = compare(lp, rp)
            if cv is not None:
                return cv
        if len(left_packet) < len(right_packet):
            return True

    if type(left_packet) != type(right_packet):
        if isinstance(left_packet, int):
            left_packet = [left_packet]
        else:
            right_packet = [right_packet]

        return compare(left_packet, right_packet)


def fix_compare(v):
    # functools.cmp_to_key needs a -1,0,1
    # Rather then changing the output of compare(), convert the values here
    if v is False:
        return 1
    elif v is True:
        return -1
    else:
        return 0


def run(packets):
    all_packets = []
    for line in packets:
        if line != '':
            all_packets.append(ast.literal_eval(line))
            continue

    all_packets.append([[2]])
    all_packets.append([[6]])

    ap_sorted = sorted(all_packets, key=functools.cmp_to_key(lambda l, r: fix_compare(compare(l, r))))

    return (ap_sorted.index([[2]]) + 1) * (ap_sorted.index([[6]]) + 1)



test_ans = run(load_input('test_input.txt'))
print(test_ans)
assert test_ans == 140

ans = run(load_input('input.txt'))
assert ans == 23111
print(ans)
