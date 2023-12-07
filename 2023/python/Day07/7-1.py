import os
import sys
from rich import print
from collections import Counter


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def run(data):
    total_val = 0
    card_order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    hand_bids = {}
    played_hands = {
        "5k": [],
        "4k": [],
        "fh": [],
        "3k": [],
        "2p": [],
        "1p": [],
        "hc": [],
    }
    for line in data:
        hand, bid = line.split()
        bid = int(bid)
        hand_bids[hand] = bid

        char_count = Counter(hand)

        if 5 in char_count.values():
            played_hands["5k"].append(hand)
        elif 4 in char_count.values():
            played_hands["4k"].append(hand)
        elif 3 in char_count.values() and 2 in char_count.values():
            played_hands["fh"].append(hand)
        elif 3 in char_count.values():
            played_hands["3k"].append(hand)
        elif list(char_count.values()).count(2) == 2:
            played_hands["2p"].append(hand)
        elif 2 in char_count.values():
            played_hands["1p"].append(hand)
        else:
            played_hands["hc"].append(hand)

    for hand_type, hands in played_hands.items():
        played_hands[hand_type].sort(key=lambda s: [card_order.index(ch) for ch in s])

    winning_hand_order = []
    winning_hand_order.extend(played_hands["hc"])
    winning_hand_order.extend(played_hands["1p"])
    winning_hand_order.extend(played_hands["2p"])
    winning_hand_order.extend(played_hands["3k"])
    winning_hand_order.extend(played_hands["fh"])
    winning_hand_order.extend(played_hands["4k"])
    winning_hand_order.extend(played_hands["5k"])

    # Get totals
    for idx, hand in enumerate(winning_hand_order):
        # print(hand, hand_bids[hand], idx+1)
        total_val += hand_bids[hand] * (idx + 1)

    # print(played_hands)
    # print(winning_hand_order)

    return total_val


test_ans = run(load_input("test_input.txt"))
print(test_ans)
assert test_ans == 6440

ans = run(load_input("input.txt"))
assert ans == 253205868
print(ans)
