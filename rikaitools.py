from time import time
from colorize import colorize


def measure_time(func):
    """Prints the time in seconds that a function takes execute from start to finish"""
    def inner1(*args):
        t1 = time()
        x = func(*args)
        t2 = time()
        print(colorize(f"{(t2-t1)}s", 'red'))
        return x
    return inner1


def get_primes(n):
    # Create a boolean array
    # "prime[0..n]" and initialize
    #  all entries it as true.
    # A value in prime[i] will
    # finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:

        # If prime[p] is not
        # changed, then it is a prime
        if prime[p]:

            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Yield all prime numbers
    for p in range(2, n + 1):
        if prime[p]:
            yield p


def is_prime(n):
    """Checks if a number is prime"""
    if n == 2:
        return True
    elif n <= 1 or n % 2 == 0:
        return False
    else:
        for i in range(3, (int(n ** 0.5)) + 1, 2):
            if n % i == 0:
                return False
    return True


def get_divisors(number):
    """Returns a list with all the divisors of a given number"""
    divisors = []
    for divisor in range(1, (number // 2) + 1):
        if number % divisor == 0:
            divisors.append(divisor)
    return divisors


def rotations(n):
    if type(n) == list or type(n) == tuple:
        n = ''.join(n)
    rotations = [n]
    times = len(n) - 1
    if times != 0:
        for i in range(times):
            n = n[1:] + n[0]
            rotations.append(n)
    return rotations


def change_base(n, base=2, mode='string'):
    """

    :param n: int
    :param base: int
    :param mode: str
    :return: str or int
    """
    if n == 0:
        return '0' if mode == 'string' else 0
    digits = []
    while n:
        digits.append(str(n % base))
        n = n//base
    return ''.join(digits[::-1]) if mode == 'string' else int(''.join(digits[::-1]))


def truncate(item, mode='all'):
    if type(item) == int:
        item = str(item)
    if len(item) == 0:
        return ''

    truncations = [item]
    times = len(item) - 1

    if mode == 'all' or mode == 'left':
        left = item
        for i in range(times):
            left = left[1:]
            truncations.append(left)
    if mode == 'all' or mode == 'right':
        right = item
        for i in range(times):
            right = right[:-1]
            truncations.append(right)
    return truncations
