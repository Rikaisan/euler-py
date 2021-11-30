def generate_pentagonals(limit):
    pentagonal_list = []
    counter = 1
    number = 0
    while number < limit:
        temp = counter * (3 * counter - 1) // 2
        number = temp
        pentagonal_list.append(number)
        counter += 1
    return pentagonal_list


pentagonals = generate_pentagonals(10000000)
min_difference = 10000000
pair = ()

for idx, a in enumerate(pentagonals):
    for b in pentagonals[idx + 1:]:
        # print(a, b)
        if a + b in pentagonals and (c := b - a) in pentagonals:
            if c < min_difference:
                pair = (a, b)
                min_difference = c

print(pair, min_difference)
