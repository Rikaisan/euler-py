from rikaitools import measure_time

# ----------------------------------------
# Version 1 - The most readable
# ----------------------------------------
# import string
# letters = string.ascii_uppercase
#
# with open("names.txt") as file:
#     data = sorted(eval(file.read()))
#
# for idx, name in enumerate(data):
#     value = 0
#     for letter in name:
#         value += letters.index(letter) + 1
#     value *= idx + 1
#     data[idx] = value
#
# print(sum(data))

# ----------------------------------------
# Version 2 - The middle ground
# ----------------------------------------


@measure_time
def rikai():
    import string
    letters = string.ascii_uppercase
    with open("names.txt") as file:
        data = sorted(eval(file.read()))

    for idx, name in enumerate(data):
        data[idx] = sum(letters.index(letter) + 1 for letter in name) * (idx + 1)
    print(sum(data))

# ----------------------------------------
# Version 3 - THE MAD MAN UNREADABILITY
# ----------------------------------------
#
# with open("names.txt") as file:
#     print(sum(sum(('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(letter) + 1) for letter in name) * (idx + 1) for idx, name in enumerate(sorted(eval(file.read())))))
