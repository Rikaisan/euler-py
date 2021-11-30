with open("67.txt", mode="r") as file:
    # Reads the text file and imports it into a data variable as a list of lists
    data = [[int(number) for number in line.split(" ")] for line in file.read().splitlines()]


def select_biggest_number(row, index):
    # Returns the biggest number from the two adjacent numbers of the row below it
    left_number = data[row + 1][index]
    right_number = data[row + 1][index + 1]
    return max(left_number, right_number)


def replace_values(row):
    # Replaces the values in the current row for the maximum sum of the two adjacent numbers from the row below it
    row_len = len(data[row])
    for index in range(row_len):
        data[row][index] += select_biggest_number(row, index)


current_row = len(data) - 2
while current_row > -1:
    # Main loop, used to loop through the data from the bottom to the top
    replace_values(current_row)
    current_row -= 1
print(data[0][0])

# with open("67.txt", mode="r") as file:
#     data = [[int(number) for number in line.split(" ")] for line in file.read().splitlines()]
#
# current_row = len(data) - 2
# while current_row > -1:
#     row_len = len(data[current_row])
#     for index in range(row_len):
#         data[current_row][index] = max(data[current_row + 1][index], data[current_row + 1][index + 1]) + data[current_row][index]
#     current_row -= 1
# print(data[0][0])
