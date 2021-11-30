from rikaitools import truncate, get_primes, is_prime

limit = 739398
matches = []
for prime in get_primes(limit):
    if prime < 11:
        continue
    match = True
    for num in '4680':
        if num in str(prime):
            match = False
            break
    if not match:
        continue
    truncations = truncate(prime)
    for truncation in truncations[1:]:
        if not is_prime(int(truncation)):
            match = False
            break
    if not match:
        continue
    matches.append(prime)

print(sum(matches), matches)
