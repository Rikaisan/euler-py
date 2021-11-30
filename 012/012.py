def get_triangle(num):
    return sum(i for i in range(1, num + 1))


def get_total_divisors(num):
    number_of_divisors = 0
    for n in range(1, int(num ** 0.5) + 1):
        if num % n == 0:
            number_of_divisors += 1
    return number_of_divisors * 2 - 1


counter = 1
max_divisors = 0
while max_divisors <= 500:
    triangle = get_triangle(counter)
    total_divisors = get_total_divisors(triangle)

    if total_divisors > max_divisors:
        max_divisors = total_divisors
        print(counter, triangle, max_divisors, sep=': ')

    counter += 1
