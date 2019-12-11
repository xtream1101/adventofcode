import os
import math


def load_input():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_file) as f:
        inputs = f.read().splitlines()
    return inputs


def mass_to_fuel(mass):
    """Get the amount of fuel required for the given mass

    Args:
        mass (int): Mass that the fuel is needed for

    Returns:
        int: The amount of fuel needed
    """
    return math.floor(int(mass) / 3) - 2


def part1(module_masses):
    """
    What is the sum of the fuel requirements for all of the modules on your spacecraft

    Args:
        module_masses (list): Masses of all modules

    Returns:
        int: Total amount of fuel needed
    """
    total = 0
    for mass in module_masses:
        total += mass_to_fuel(mass)
    return total


def part2(module_masses):
    """
    What is the sum of the fuel requirements for all of the modules on your spacecraft
    when also taking into account the mass of the added fuel?

    Args:
        module_masses (list): Masses of all modules

    Returns:
        int: Total amount of fuel needed
    """
    total = 0
    for mass in module_masses:
        module_total = 0
        val = mass_to_fuel(mass)
        while val > 0:
            module_total += val
            val = mass_to_fuel(val)
        total += module_total
    return total


if __name__ == '__main__':
    print("Day 1:")

    part1_ans = part1(load_input())
    print("\tPart 1:", part1_ans)

    part2_ans = part2(load_input())
    print("\tPart 2:", part2_ans)
