from rikaitools import get_primes, is_prime, rotations

counter = 0
for prime in get_primes(1000000):
    is_circular = True
    for number in '245680':
        if number in str(prime):
            is_circular = False
            break
    if not is_circular:
        continue
    is_circular = [is_prime(int(rot)) for rot in rotations(str(prime))]
    if all(is_circular):
        counter += 1

print(counter + 2)
