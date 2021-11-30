import math

limit = 5000000

matches = []
for n in range(limit):
    digits = [int(x) for x in str(n)]
    sum = 0
    for digit in digits:
        sum += math.factorial(digit)
    if sum == n:
        matches.append(n)

print(matches)
