from math import comb

def sum_Of_product(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += comb(n, i) * comb(n, (i - 1))
    return total_sum
