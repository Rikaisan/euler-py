primes = []
for number in range(1, 2000000):
    if not number % 2 == 0:
        is_prime = True
        for divisor in range(3, int(number ** 0.5) + 1, 2):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)

print(sum(primes) + 1)
