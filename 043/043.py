from itertools import permutations as perm

digits = '1234567890'
primes = (2, 3, 5, 7, 11, 13, 17)
permutations = [''.join(num) for num in perm(digits) if num[0] != '0']
total = 0

for num in permutations:
    idx = 1
    while idx < 8:
        strip = num[idx:idx + 3]
        if int(strip) % primes[idx - 1] != 0:
            break
        idx += 1
    if idx == 8:
        total += int(num)

print(total)
