limit = 100

results = set()
for a in range(2, limit + 1):
    for b in range(2, limit + 1):
        results.add(a**b)

print(len(results))
