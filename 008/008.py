from math import prod
with open('data.txt') as file:
    data = file.read()
data_length = len(data)
number_of_adjacent_numbers = 13

max_product = 0
for idx, digit in enumerate(data):
    if idx <= data_length - number_of_adjacent_numbers:
        adjacent_numbers = [(int(n)) for n in data[idx:idx + number_of_adjacent_numbers]]
        current_product = prod(adjacent_numbers)
        print(adjacent_numbers, current_product)
        max_product = current_product if current_product > max_product else max_product

print(max_product)
