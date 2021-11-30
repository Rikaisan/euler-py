number = 1
max_pandigital = 192384576
pandigitals = []

for num in range(1, 9999):
    n = 1
    concatenated = ''
    while len(concatenated) < 9:
        concatenated += str(num * n)
        n += 1
    if len(concatenated) != 9 or len(set(concatenated)) != 9 or '0' in concatenated:
        continue
    pandigitals.append(int(concatenated))
    if int(concatenated) > max_pandigital:
        max_pandigital = int(concatenated)

print(max_pandigital)