from math import prod

with open("grid.txt") as file:
    raw_data = file.read().splitlines()
    data = [[int(num) for num in line.split(" ")] for line in raw_data]
    for row in data:
        formatted_row = ' '.join(f'{num:02d}' for num in row)
        print(formatted_row)

cursor = [0, 0]
current_max = 0
total_rows = len(data)
total_columns = len(data[0])


def calculate_horizontal(coordinates, mode='product'):
    values = data[coordinates[0]][coordinates[1]:coordinates[1] + 4]
    return prod(values) if mode == 'product' else values


def calculate_vertical(coordinates, mode='product'):
    values = []
    for n in range(0, 4):
        value = data[coordinates[0] + n][coordinates[1]]
        values.append(value)
    return prod(values) if mode == 'product' else values


def calculate_diagonal(coordinates, direction='right', mode='product'):
    values = []
    for n in range(0, 4):
        value = data[coordinates[0] + n][coordinates[1] - n] if direction == 'left' \
            else data[coordinates[0] + n][coordinates[1] + n]
        values.append(value)
    return prod(values) if mode == 'product' else values


def calculate_product(coordinates):
    if data[coordinates[0]][coordinates[1]] != 0:
        raw_products = []
        if coordinates[1] <= total_columns - 4:
            raw_products += [calculate_horizontal(coordinates)]
        if coordinates[0] < total_rows - 4:
            raw_products = [calculate_vertical(coordinates)]
            if coordinates[1] <= total_columns - 4:
                raw_products += [calculate_diagonal(coordinates)]
            if coordinates[1] >= 3:
                raw_products += [calculate_diagonal(coordinates, 'left')]
        max_product = max(raw_products) if raw_products else 0
        # print(f"Found {max_product:,} from {', '.join(str(f'{num:,}') for num in raw_products)}")
        return max_product
    else:
        # print("Found 0, skipping...")
        return 0


for row in range(total_rows):
    for column in range(total_columns):
        if (x := calculate_product((row, column))) > current_max:
            current_max = x
print(f"{current_max:,}")
