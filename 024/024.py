from itertools import permutations

data = permutations('0123456789')

for idx, num in enumerate(data):
    if idx == 1000000 - 1:
        print(''.join(num))