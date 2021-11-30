import string
letters = string.ascii_uppercase

with open("words.txt") as file:
    data = eval(file.read())

triangles = [1]
matches = 0


def generate_triangles(limit):
    triangle_list = []
    counter = 1
    number = 0
    while number < limit:
        temp = counter / 2 * (counter + 1)
        number = temp
        triangle_list.append(number)
        counter += 1
    return triangle_list


for word in data:
    decomposed_word = [c for c in word]
    value = 0
    for letter in decomposed_word:
        value += letters.index(letter) + 1
    # -----
    if value > triangles[-1]:
        triangles = generate_triangles(value)
    if value in triangles:
        matches += 1

print(matches)
