from itertools import permutations
from time import time
t1 = time()
primes = []


def es_primo(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
    return True


for number in range(1000, 9999):
    if not number % 2 == 0:
        is_prime = True
        for divisor in range(3, int(number ** 0.5) + 1, 2):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)

# for number in range(1000, 9999):
#     if es_primo(number):
#         primes.append(number)


# print(f"Found {len(primes)} primes: {primes}")

usable_numbers = []
for idx, prime in enumerate(primes):
    number_permutations = set(x for n in permutations(str(primes[idx]), 4) if (x := int(''.join(n))) > 1000)
    appearances = []
    for number in number_permutations:
        if number in primes:
            primes.remove(number)
            appearances.append(number)
    if len(appearances) > 3:
        usable_numbers.append(sorted(appearances))

second_stage = []
for numbers in usable_numbers:
    for idx, item in enumerate(numbers):
        if idx < len(numbers) - 2:
            for i in range(idx + 1, len(numbers)):
                matches = []
                offset = numbers[i] - item
                for t in range(i + 1, len(numbers)):
                    second_offset = numbers[t] - numbers[i]
                    if second_offset > offset:
                        break
                    elif second_offset == offset:
                        matches += [item, numbers[i], numbers[t]]
                if len(matches) == 3:
                    second_stage.append(matches)

print(second_stage)
t2 = time()
print(f"{t2-t1} seconds elapsed.")
