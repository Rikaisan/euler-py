from time import time
from itertools import permutations as pr


def find_prime(lower, upper):
    prime_numbers = []
    for num in range(lower, upper + 1):
        if esPrimoV4(num):
            prime_numbers.append(num)
    return prime_numbers


def esPrimoV4(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        for i in range(3, (int(n ** 0.5)) + 1, 2):
            if n % i == 0:
                return False
    return True


def permutation_finder(number_list):
    total_permutation = []
    for number in number_list:
        number_permutations = set("".join(item) for item in pr(str(number)))
        permutations = []
        for n in number_permutations:
            if (num := int(n)) in number_list:
                permutations.append(num)
                number_list.remove(num)
        if len(permutations) >= 3:
            total_permutation.append(sorted(permutations))
    return total_permutation


def candidate(number_list):
    for item in number_list:
        if number_list.count(item) >= 2:
            return True
    return False


def candidate2(lista):
    for idx, item in enumerate(lista):
        index = (idx + 1) % len(lista)-1
        lista.pop(idx)
        if item == lista[index]:
            return True
    return False


def same_space(number_list):
    candidates = []
    for item in number_list:
        difference = []
        counter = 0
        for number in range(0, len(item) - 1):
            space = item[1 + counter] - item[counter]
            counter += 1
            difference.append(space)
        if candidate2(difference):
            candidates.append(item)
    return candidates


t1 = time()
numbers = find_prime(1000, 9999)
permutation = permutation_finder(numbers)

print(same_space(permutation))
t2 = time()
print(t2-t1)

