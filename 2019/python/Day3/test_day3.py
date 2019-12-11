import os
os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Day3.final import part1, part2, load_input


def test_part_1_example_1():
    assert part1('R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(','),
                 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')) == 159


def test_part_1_example_2():
    assert part1('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(','),
                 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(',')) == 135


def test_part_2_example_1():
    assert part2('R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(','),
                 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')) == 610


def test_part_2_example_2():
    assert part2('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(','),
                 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(',')) == 410


def test_answer_part_1():
    assert part1(*load_input()) == 489


def test_answer_part_2():
    assert part2(*load_input()) == 93654


