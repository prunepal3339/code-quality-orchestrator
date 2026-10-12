def find_Average_OF_Cube(n): 
    total = sum([i * i * i for i in range(1, n + 1)]) 
    return total / n
