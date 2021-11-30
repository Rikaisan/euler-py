from math import prod
n = 1
digits = '0123456789'
num = digits

obtain = (1, 10, 100, 1000, 10000, 100000, 1000000)

while len(num) < obtain[-1]:
    for digit in digits:
        num += str(n) + digit
    n += 1

numbers = [int(num[x]) for x in obtain]
print(prod(numbers))
