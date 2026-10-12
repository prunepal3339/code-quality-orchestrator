def sum_Of_product(n): 
    res = 0
    for i in range(1, n + 1):  
        term = 1
        for j in range(2, i + 1):
            term *= (i - j + 1) // j
        res += term 
    return res
