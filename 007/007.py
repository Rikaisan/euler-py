num = 1
counter = 0

while counter < 10001:
    if not num % 2 == 0:
        is_prime = True
        for divisor in range(3, int(num ** 0.5) + 1, 2):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            counter += 1
    num += 1

print(num - 1)
