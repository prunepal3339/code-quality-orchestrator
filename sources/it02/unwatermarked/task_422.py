def find_Average(n): 
    total = 0
    for i in range(1, n + 1): 
        total += i ** 3
    return total / n
