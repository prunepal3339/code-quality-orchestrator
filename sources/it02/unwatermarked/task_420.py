def cube_Sum(n): 
    i = 1
    sum = 0
    while(i <= n): 
        sum += (2 * i) ** 3
        i += 1
        return sum
