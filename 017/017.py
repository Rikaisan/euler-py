from colorize import colorize


def writen(number, mode='return'):
    units = {
        9: 'nine',
        8: 'eight',
        7: 'seven',
        6: 'six',
        5: 'five',
        4: 'four',
        3: 'three',
        2: 'two',
        1: 'one',
    }
    tens = {
        9: 'ninety',
        8: 'eighty',
        7: 'seventy',
        6: 'sixty',
        5: 'fifty',
        4: 'forty',
        3: 'thirty',
        2: 'twenty'
    }
    tens_ten = {
        19: 'nineteen',
        18: 'eighteen',
        17: 'seventeen',
        16: 'sixteen',
        15: 'fifteen',
        14: 'fourteen',
        13: 'thirteen',
        12: 'twelve',
        11: 'eleven',
        10: 'ten'
    }
    hundred_constant = ' hundred '
    hundred_conditional = 'and '
    thousand_constant = ' thousand '
    digits = [int(num) for num in str(number)]
    written = ''

    if len(digits) == 1:
        written = 'zero' if number == 0 else units[number]
    if len(digits) > 1:
        if digits[-2] != 0:
            if digits[-2] == 1:
                last_two_digits = int(''.join(str(i) for i in digits[-2::]))
                written = tens_ten[last_two_digits] + written
            else:
                if digits[-1] != 0:
                    written = tens[digits[-2]] + units[digits[-1]]
                else:
                    written = tens[digits[-2]]
        if digits[-2] == 0 and digits[-1] != 0:
            written = units[digits[-1]]
        if len(digits) != 2 and (digits[-2] != 0 or digits[-1] != 0):
            written = hundred_conditional + written

    if len(digits) > 2:
        if digits[-3] != 0:
            written = units[digits[-3]] + hundred_constant + written
    if len(digits) > 3:
        written = units[digits[-4]] + thousand_constant + written

    if mode == 'print':
        print(colorize(number, 'magenta'), colorize(written, 'cyan'), sep=': ')
    else:
        return written


numbers = []
for x in range(1, 1001):
    written_number = writen(x)
    written_number = written_number.replace(' ', '')
    numbers.append(written_number)

unified_string = ''.join(numbers)
print(len(unified_string))
