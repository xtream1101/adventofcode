import os
import sys

# inputs = []
input_file = os.path.join(os.path.dirname(sys.argv[0]), 'input.txt')
with open(input_file) as f:
    inputs = f.read()


w = 25
h = 6
num_layers = int(len(inputs) /  (w*h))
layers = []
for l in range(num_layers):
    l_start = (w*h) * l
    l_stop = ((w*h) * l + (w*h))
    layer = inputs[l_start:l_stop]
    layers.append(layer)

# Generate image
final_image_raw = ''
for col in range(w*h):
    for l in layers:
        if l[col] != '2':
            final_image_raw += l[col]
            break

# Render image
num_rows = int(len(final_image_raw) /  w)
for r in range(num_rows):
    r_start = w * r
    r_stop = r_start + w
    print(final_image_raw[r_start:r_stop].replace('0', ' ').replace('1', '#'))
