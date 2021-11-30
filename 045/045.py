starting_limit = 40755  # 285


def triangles(limit):
    counter = 1
    num = 0
    while num < limit:
        num = counter * (counter + 1) // 2
        counter += 1
        yield num


def pentagonals(limit):
    counter = 1
    num = 0
    while num < limit:
        num = counter * (counter * 3 - 1) // 2
        counter += 1
        yield num


def hexagonals(limit):
    counter = 1
    num = 0
    while num < limit:
        num = counter * (counter * 2 - 1)
        counter += 1
        yield num


for hexagonal in hexagonals(starting_limit * 1000000):
    if hexagonal in pentagonals(hexagonal):
        print(hexagonal)


