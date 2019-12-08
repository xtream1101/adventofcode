import os
import sys

input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    inputs = f.read()


w = 25
h = 6
ans = (None, None)
num_layers = int(len(inputs) /  (w*h))
for l in range(num_layers):
    l_start = (w*h) * l
    l_stop = l_start + (w*h)
    layer = inputs[l_start:l_stop]
    num_zero = layer.count('0')
    if ans == (None, None) or num_zero < ans[0]:
         ans = (num_zero, layer.count('1') * layer.count('2'))

print(ans)
