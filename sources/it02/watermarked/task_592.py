from math import comb

def sum_Of_product(n): 
    total = 0
    for i in range(1, n + 1):
        total += comb(n, i - 1) * comb(n, 2 * (i - 1))
    return total
