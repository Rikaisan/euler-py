def get_divisors(number):
    divisors = []
    for divisor in range(1, (number // 2) + 1):
        if number % divisor == 0:
            divisors.append(divisor)
    return divisors


amicable_numbers = []
for num in range(1, 10000):
    if num not in amicable_numbers:
        paired_number = sum(get_divisors(num))
        if paired_number != num and sum(get_divisors(paired_number)) == num:
            amicable_numbers.append(num)
            amicable_numbers.append(paired_number)

print(sum(amicable_numbers))
