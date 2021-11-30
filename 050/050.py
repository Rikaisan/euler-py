from rikaitools import get_primes, is_prime
limit = 1000000

primes = [*get_primes(limit)]
a = 0
max_match = (0, 0)

while a < len(primes):
    b = a + 1
    total = primes[a]

    while total < limit and b < len(primes):
        total += primes[b]
        b += 1

    if b == len(primes):
        a = len(primes)
        break

    while not is_prime(total):
        b -= 1
        total -= primes[b]

    if b - a + 1 > max_match[1]:
        max_match = (total, b - a + 1)
        print(max_match)
    a += 1
