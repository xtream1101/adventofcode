import os
import re
import sys


claims = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    claims = f.read().splitlines()

claim_pattern = re.compile(r'(\d+),(\d+):\s(\d+)x(\d+)')
already_claimed_cells = set()
fabric_claims = set()
for claim in claims:
    m = claim_pattern.search(claim)
    x, y, width, height = map(int, m.groups())
    for col in range(width):
        for row in range(height):
            cell = (x + col, y + row)
            if cell in fabric_claims:
                already_claimed_cells.add(cell)
            else:
                fabric_claims.add(cell)

print(f"Part 1: {len(already_claimed_cells)}")
