data = set([int(x.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1'), base=2)
            for x in open('input.txt').read().split()])

print('Part 1', max(data))
for x in range(min(data), max(data)):
    if x not in data:
        print('Part 2', x)
        break
