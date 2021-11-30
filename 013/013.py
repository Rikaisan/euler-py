with open('data.txt') as file:
    data = (int(line) for line in file.read().splitlines())
    print(sum(data))