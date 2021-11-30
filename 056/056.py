limit = 100
max_sum = 0

for a in range(1, limit):
    for b in range(1, limit):
        c = str(a ** b)
        total = sum(int(digit) for digit in c)
        if total > max_sum:
            max_sum = total
print(max_sum)
