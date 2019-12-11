import os
os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Day5.final import load_input
from Day2.final import IntCodeComputer


def run_int_code_computer(program, input_val):
    process = IntCodeComputer(program, input_val)
    process.run()
    return process


def test_example_1():
    # input == 8
    process = run_int_code_computer([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 8)
    assert process.outputs == [1]


def test_example_2():
    # input < 8
    process = run_int_code_computer([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 6)
    assert process.outputs == [1]


def test_example_3():
    # input == 8
    process = run_int_code_computer([3, 3, 1108, -1, 8, 3, 4, 3, 99], 8)
    assert process.outputs == [1]


def test_example_4():
    # input < 8
    process = run_int_code_computer([3, 3, 1107, -1, 8, 3, 4, 3, 99], 4)
    assert process.outputs == [1]


def test_answer_part_1():
    process = run_int_code_computer(load_input(), 1)
    assert process.outputs[-1] == 13547311


def test_answer_part_2():
    process = run_int_code_computer(load_input(), 5)
    assert process.outputs[-1] == 236453
