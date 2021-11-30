from rikaitools import is_prime
from itertools import permutations
max_prime = 0

for n in range(7, 0, -1):  # Si la suma de los dígitos de un número es múltiplo de 3, entonces el número original es divisible por 3 también, por lo que sum(1:9) y sum(1:8) no se prueban
    number = ''
    for digit in range(n, 0, -1):
        number += str(digit)
    for permutation in permutations(number):
        permutation = int(''.join(permutation))
        if is_prime(permutation) and permutation > max_prime:
            max_prime = permutation
            print(max_prime)


