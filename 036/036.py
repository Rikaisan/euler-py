from rikaitools import change_base as base2

limit = 1000000

palindromes = []

for num in range(limit):
    if str(num)[-1] == '0':
        continue
    if str(num) == str(num)[::-1]:
        converted = base2(num)
        if converted[0] == '0':
            continue
        if converted == converted[::-1]:
            palindromes.append(num)

print(sum(palindromes), palindromes)
