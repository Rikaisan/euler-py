palindromes = []
for n in range(100, 1000):
    for i in range(100, 1000):
        product = str(n*i)
        if product == product[::-1]:
            palindromes.append(int(product))
print(max(palindromes))
