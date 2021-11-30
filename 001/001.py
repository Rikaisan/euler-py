all_numbers = []
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        all_numbers.append(n)
print(sum(all_numbers))
