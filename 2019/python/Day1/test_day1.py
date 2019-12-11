import os
os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Day1.final import load_input, part1, part2


def test_answer_part_1():
    assert part1(load_input()) == 3454026


def test_answer_part_2():
    assert part2(load_input()) == 5178170
