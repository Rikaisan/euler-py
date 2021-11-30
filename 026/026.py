# def find_pattern(num):
#     num = str(num)[2:]
#     if len(num) == 1:
#         return num
#     p1 = 0
#     p2 = 0
#     current_sequence = ''
#     found_pattern = False
#     while not found_pattern:
#         a = num[p1]
#         b = num[p2]
#         if a == b:
#             p2 += 1
#             b = num[p2]
#         if a != b:
#             p2 += 1
#         print(num[p1:p1+3])
#         print(num[p2:p2+3])
#
#
#
#
# counter = 1
# while counter < 1000:
#     x = 1 / counter
#     print(find_pattern(x))
#     counter += 1
#
