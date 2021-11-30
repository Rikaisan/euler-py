number = 2 ** 1000
number_separated = (int(digit) for digit in str(number))
print(sum(number_separated))
