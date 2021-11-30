num = 0
match = False

while not match:
    num += 1
    digits = [digit for digit in str(num)]

    for x in range(2, 7):
        new = str(num * x)
        if len(new) > len(digits):
            break
        in_new = all(digit in new for digit in digits)
        if not in_new:
            break
        if in_new and x == 6:
            match = True

print(num)
