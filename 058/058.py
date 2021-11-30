from rikaitools import is_prime

side_len = 3
num = 1
primes = 0
total_nums = 0
max_side_len = 1000001

while side_len <= max_side_len:
    for i in range(4):
        num += side_len - 1
        if is_prime(num):
            primes += 1
        total_nums += 1
        if primes * 100 / total_nums < 10:
            print(side_len - 2)
            side_len = max_side_len + 1
            break

    side_len += 2
# print(f'Total: {primes * 100 / total_nums}\nSide length: {side_len}')
