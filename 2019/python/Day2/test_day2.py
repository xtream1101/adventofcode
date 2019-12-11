import os
os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Day2.final import int_code_computer, load_input, part1, part2


def test_small_program_1():
    assert int_code_computer([1, 0, 0, 0, 99])[0] == [2, 0, 0, 0, 99]


def test_small_program_2():
    assert int_code_computer([2, 3, 0, 3, 99])[0] == [2, 3, 0, 6, 99]


def test_small_program_3():
    assert int_code_computer([2, 4, 4, 5, 99, 0])[0] == [2, 4, 4, 5, 99, 9801]


def test_small_program_4():
    assert int_code_computer([1, 1, 1, 4, 99, 5, 6, 0, 99])[0] == [30, 1, 1, 4, 2, 5, 6, 0, 99]


def test_answer_part_1():
    assert part1(load_input()) == 3101878


def test_answer_part_2():
    assert part2(load_input()) == 8444
