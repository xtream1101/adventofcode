import os
import sys
from rich import print
from collections import Counter


def load_input(file_name):
    input_file = os.path.join(os.path.dirname(sys.argv[0]), file_name)
    with open(input_file) as f:
        lines = f.read().splitlines()
    return lines


def get_hand_type(hand):
    char_count = Counter(hand)
    j_count = char_count["J"]
    del char_count["J"]

    if (
        5 in char_count.values()
        or (4 in char_count.values() and j_count == 1)
        or (3 in char_count.values() and j_count == 2)
        or (2 in char_count.values() and j_count == 3)
        or (1 in char_count.values() and j_count == 4)
        or j_count == 5
    ):
        return "5k"

    elif (
        4 in char_count.values()
        or (3 in char_count.values() and j_count == 1)
        or (2 in char_count.values() and j_count == 2)
        or (1 in char_count.values() and j_count == 3)
    ):
        return "4k"

    elif (
        (3 in char_count.values() and 2 in char_count.values())
        or (3 in char_count.values() and (1 in char_count.values() and j_count == 1))
        or (
            (list(char_count.values()).count(2) == 2 and j_count == 1)
            and 2 in char_count.values()
        )
        or ((1 in char_count.values() and j_count == 2) and 2 in char_count.values())
    ):
        return "fh"

    elif (
        3 in char_count.values()
        or (2 in char_count.values() and j_count == 1)
        or (1 in char_count.values() and j_count == 2)
    ):
        return "3k"

    elif (
        list(char_count.values()).count(2) == 2
        or (2 in char_count.values() and j_count == 1)
        or (1 in char_count.values() and j_count == 2)
    ):
        return "2p"

    elif (
        2 in char_count.values()
        or (1 in char_count.values() and j_count == 1)
        or (j_count == 2)
    ):
        return "1p"

    else:
        return "hc"


def run(data):
    total_val = 0
    # low -> high
    card_order = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

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

        hand_type = get_hand_type(hand)
        played_hands[hand_type].append(hand)

    for hand_type, hands in played_hands.items():
        played_hands[hand_type].sort(key=lambda s: [card_order.index(ch) for ch in s])

    # Order hand from low to high in the list
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


assert get_hand_type("32T3K") == "1p"
assert get_hand_type("KK677") == "2p"
assert get_hand_type("KTJJT") == "4k"
assert get_hand_type("T55J5") == "4k"
assert get_hand_type("QQQJA") == "4k"
assert get_hand_type("JJJ8J") == "5k"
assert get_hand_type("JJJJJ") == "5k"
assert get_hand_type("4J2JT") == "3k"
assert get_hand_type("4558J") == "3k"
assert get_hand_type("K8J8K") == "fh"
assert get_hand_type("KJJ8K") == "4k"

test_ans = run(load_input("test_input.txt"))
print(test_ans)
assert test_ans == 5905

ans = run(load_input("input.txt"))
assert ans == 253907829
print(ans)
