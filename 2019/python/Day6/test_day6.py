import os
os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Day6.final import load_input, part1, part2

part_1_example_1_input = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']
part_1_example_2_input = ['B)C', 'COM)B', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']
part_1_example_3_input = ['B)C', 'COM)B', 'C)D', 'E)F', 'B)G', 'D)E', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']

part_2_example_1_input = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']


def test_part_1_example_1():
    # Given test
    assert part1(part_1_example_1_input) == 42


def test_part_1_example_2():
    # Custom test
    # COM is not first
    assert part1(part_1_example_2_input) == 42


def test_part_1_example_3():
    # Custom test
    # COM is not first, and another node is out of order
    assert part1(part_1_example_3_input) == 42


def test_part_2_example_1():
    # Given test
    assert part2(part_2_example_1_input, 'YOU', 'SAN') == 4


def test_answer_part_1():
    assert part1(load_input()) == 308790


def test_answer_part_2():
    assert part2(load_input(), 'YOU', 'SAN') == 472
