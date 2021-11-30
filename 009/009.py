def search_numbers():
    a = 1
    while a:
        for b in range(1, 1000 - a):
            c = 1000 - a - b
            if a + b + c == 1000 and (a ** 2 + b ** 2) == c ** 2:
                return a * b * c
        a += 1


print(search_numbers())
