all_numbers = []
num1 = 1
num2 = 1
num3 = 1

while num3 < 4000000:
    if num3 % 2 == 0:
        all_numbers.append(num3)
    num3 = num1 + num2
    num1 = num2
    num2 = num3

print(sum(all_numbers))
