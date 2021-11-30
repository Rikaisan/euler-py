from string import ascii_lowercase
from operator import xor


with open('cipher.txt') as file:
    raw_data = file.read().split(',')


def decode(data, key):
    decoded_list = []
    key_idx = 0
    for char in data:
        decoded_char = xor(int(char), key[key_idx])
        decoded_list.append(chr(decoded_char))
        key_idx = (key_idx + 1) % len(key)
    return ''.join(decoded_list)


def test_text(text):
    valid_words = (' and ', ' is ', ' the ', ' of ', ' that ')
    for word in valid_words:
        if word not in text:
            return False
    return True


def get_text(data):
    for a in ascii_lowercase:
        for b in ascii_lowercase:
            for c in ascii_lowercase:
                attempt = decode(data, [ord(a), ord(b), ord(c)])
                if test_text(attempt):
                    print(a, b, c, attempt, sep='; ')
                    return attempt


total = 0
for char in get_text(raw_data):
    total += ord(char)
print(total)
