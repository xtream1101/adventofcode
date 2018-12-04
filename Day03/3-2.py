import os
import re
import sys
from collections import defaultdict


claims = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    claims = f.read().splitlines()

claim_pattern = re.compile(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)')
fabric_claims = defaultdict(set)
for claim in claims:
    m = claim_pattern.search(claim)
    claim_id, x, y, width, height = map(int, m.groups())
    for col in range(width):
        for row in range(height):
            cell = (x + col, y + row)
            fabric_claims[cell].add(claim_id)

# Also a way to answer part 1
# count = 0
# for c in fabric_claims.values():
#     if len(c) > 1:
#         count += 1
# print(count)

seen_claims = set()
non_overlapping_claims = set()
for claims in fabric_claims.values():
    if len(claims) == 1:
        claim_id = next(iter(claims))
        if claim_id not in seen_claims:
            non_overlapping_claims.add(claim_id)
    else:
        non_overlapping_claims = non_overlapping_claims - claims

    seen_claims = seen_claims.union(claims)

print(f"Part 2: {non_overlapping_claims}")
