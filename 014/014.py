limit = 1000000
longest_chain = (1, 1)  # (num, chain_length)
for n in range(1, limit + 1):
    current_number = n
    current_terms = 1
    while current_number != 1:
        current_number = current_number // 2 if current_number % 2 == 0 else current_number * 3 + 1
        current_terms += 1
    if current_terms > longest_chain[1]:
        longest_chain = (n, current_terms)
print(longest_chain)