# 232792560
from time import time
n = 20
result = 0
print(f"Testing...")
t1 = time()
while result == 0:
    for i in range(1, 21):
        if n % i != 0:
            break
        if i == 20 and n % i == 0:
            result = n
    n += 20
t2 = time()
print(f"Found match at: {result}")
print(f"Time elapsed: {round(t2 - t1, 2)}s")