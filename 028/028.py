side_len = 3
num = 1
total = 1
max_side_len = 1001

while side_len <= max_side_len:
    for i in range(4):
        num += side_len - 1
        total += num
    side_len += 2
print(f'Total: {total}\nSide length: {max_side_len}')
