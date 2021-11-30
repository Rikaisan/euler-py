import math

num = math.factorial(100)
sum_of_digits = sum(int(digit) for digit in str(num))

print(sum_of_digits)
