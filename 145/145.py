from tqdm import tqdm
from rikaitools import measure_time
from colorize import colorize


@measure_time
def program():
    limit = 1000

    same_digits = 0
    counter = 0
    # for i in tqdm(range(1, limit), desc="Loading..."):
    for i in range(1, limit):
        num_string = str(i)
        if num_string[-1] == '0':
            continue
        reversed_str = num_string[::-1]
        reversed_num = int(reversed_str)

        x = i + reversed_num
        x_digits = [int(digit) for digit in str(x)]

        is_reversible = True
        for digit in x_digits:
            if digit % 2 == 0:
                is_reversible = False
                break

        if is_reversible:
            counter += 1
        if is_reversible:
            if all(digit == x_digits[0] for digit in x_digits):
                same_digits += 1
                print(i, reversed_num, colorize(x_digits, 'red'), sep=': ')
            else:
                print(i, reversed_num, colorize(x_digits, 'yellow'), sep=': ')

    print(counter)
    print(same_digits)
program()