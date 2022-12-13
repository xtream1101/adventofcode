import ast
import os
import sys


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


def run(packets):
    packet_pair = []
    pair_idx = 0
    correct_pairs = []
    for line in packets:
        if line != '':
            packet_pair.append(ast.literal_eval(line))
            continue

        pair_idx += 1

        is_in_order = compare(packet_pair[0], packet_pair[1])
        # print(f"\nPair #{pair_idx}: {is_in_order}\n")
        if is_in_order is True:
            correct_pairs.append(pair_idx)

        packet_pair = []
        # input()

    return sum(correct_pairs)


test_ans = run(load_input('test_input.txt'))
print(test_ans)
assert test_ans == 13

ans = run(load_input('input.txt'))
assert ans == 5625
print(ans)
