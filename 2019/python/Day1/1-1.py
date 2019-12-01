import os
import sys
import math

masses = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    masses = f.read().splitlines()



def mass_to_fuel(mass):
    return math.floor(int(mass)/3) - 2

total = 0
for mass in masses:
    total += mass_to_fuel(mass)

print(total)
