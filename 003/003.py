number = 600851475143
squared_number = int((number ** 0.5) + 1)


def primes(max_range):
    for n in range(1, max_range):
        if not n % 2 == 0:
            is_prime = True
            for divisor in range(3, int(n ** 0.5) + 1, 2):
                if n % divisor == 0:
                    is_prime = False
                    break
            if is_prime:
                yield n


factors = []
for num in primes(squared_number):
    if number % num == 0:
        factors.append(num)

print(max(factors))
