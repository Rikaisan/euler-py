from itertools import permutations as perms
from numpy import cbrt
n = 2175
match = 0

while not match:
    digits = ''.join(digit for digit in str(n ** 3))
    permutations = set(permutation for permutation in perms(digits) if len(permutation) == len(digits) and permutation[0] != '0')
    cubes = 0
    for permutation in permutations:
        num = int(''.join(permutation))
        if float(cbrt(num)).is_integer():
            cubes += 1
    if cubes == 5:
        match = (n, digits)
    print(n, cubes)
    n += 1
print(match)

