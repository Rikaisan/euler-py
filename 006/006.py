squares_sum = sum(i**2 for i in range(1, 101))
squared_sum = sum(i for i in range(1, 101)) ** 2
print(abs(squares_sum-squared_sum))
