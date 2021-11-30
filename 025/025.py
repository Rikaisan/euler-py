def fib(times):
    n1, n2 = 1, 1
    for i in range(times):
        yield n1
        old_n1 = n1
        n1 = n2
        n2 = old_n1 + n2


for idx, i in enumerate(fib(10000000)):
    if len(str(i)) >= 1000:
        print(idx)
        break