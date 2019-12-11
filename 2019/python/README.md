# 2019 Advent of Code

https://adventofcode.com/2019/

Each day will have the following files:
- `input.txt`: The inputs given to solve the problem
- `n-1.py`: `n` is the day. This is part1's answer. This code may not be the most efficient or clean, but it was the state of the code when I first got the answer
- `n-2.py`: Save as above, but for part 2
- `final.py`: This is the cleaned up code and will run parts 1 & 2 for that day. When I get around to it I like to have a proper version that has clean and documented code. 
- `test_day_n_.py`: If tests are needed they are added in here. Uses the code from `final.py`. Run with `pytest -vv tests.py`


# Tests
Each Day has a `test_day_n_.py` file in it.  
To run all tests:  
`pytest -vv`  
From this directory


# Linting
Only the `final.py` files are linted.  
Run `flake8 */final.py` from this directory.


# Code that is re used

## Int Code Computer
First seen in Day2. Final Int Code Computer is in `Day2/finial.py` and has been updated as needed and imported into other days.  
Run tests:  
`pytest -vv Day2/tests.py`
`pytest -vv Day5/tests.py`
`pytest -vv Day7/tests.py`
`pytest -vv Day9/tests.py`
