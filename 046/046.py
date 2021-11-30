from rikaitools import is_prime, get_primes

limit = 10000000000


for num in range(2, limit):
    if not num % 2 == 0 and not is_prime(num):
        matches = False
        primes = [*get_primes(num)]
        while primes:
            prime = primes[-1]
            x = 1
            while (result := prime + 2 * (x ** 2)) <= num:
                if result == num:
                    matches = True
                    break
                else:
                    x += 1
            del primes[-1]
        if not matches:
            print(num)
            break

