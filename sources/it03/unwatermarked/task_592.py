def sum_Of_product(n):
    if n < 2:
        return 0
    result = 0
for i in range(1, n + 1):
result += (binom(i - 1, 1) * binom(i, 1))
return result
