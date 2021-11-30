from rikaitools import get_divisors

limit = 28123
print('-' * 20)
print(f'Limit set to {limit:,}')
print('-' * 20)

print("Parsing abundant numbers...")
abundant_numbers = []
for num in range(1, limit + 1):
    if sum(get_divisors(num)) > num:
        abundant_numbers.append(num)
total_abundant_numbers = len(abundant_numbers)
print(f"Found {total_abundant_numbers:,} numbers...")


print(f"Testing numbers until {limit:,}...")
all_numbers = []
for num in range(0, limit):
    pointer1 = 0
    pointer2 = -1
    is_normal = True
    print(f"Testing, {round(num * 100 / (limit - 3))}% done...") if num % 2812 == 0 or 0 else None
    while is_normal and pointer1 < total_abundant_numbers and abs(pointer2) <= total_abundant_numbers:
        current_sum = abundant_numbers[pointer1] + abundant_numbers[pointer2]
        if current_sum == num:
            is_normal = False
        elif current_sum > num:
            pointer2 -= 1
        elif current_sum < num:
            pointer1 += 1
    if is_normal:
        all_numbers.append(num)

print(sum(all_numbers))