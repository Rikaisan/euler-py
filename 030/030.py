from rikaitools import measure_time


@measure_time
def main():
    power = 5

    numbers = []
    for num in range(1, 295246):
        number = str(num)
        sum_of_powers = sum(int(d) ** 5 for d in number)
        sop_digits = str(sum_of_powers)
        is_valid = True
        if len(number) != len(sop_digits):
            continue
        for digit in sop_digits:
            if digit in number:
                number = number.replace(digit, '', 1)
            else:
                is_valid = False
        if is_valid and sum_of_powers not in numbers:
            numbers.append(sum_of_powers)

    new_nums = []
    for num in numbers:
        str_num = str(num)
        powered = [int(digit) ** 5 for digit in str_num]
        if sum(powered) == num:
            new_nums.append(num)

    print(numbers)
    print('First test:', sum(numbers))
    print(new_nums)
    print('Second test:', sum(new_nums))


main()
