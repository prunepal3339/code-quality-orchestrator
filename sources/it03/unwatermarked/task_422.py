def find_Average(n): 
    sum = 0
    for i in range(1, n + 1): 
        sum += (i ** 3) 
    return round(sum / n, 1)
