def bell_number(n): 
    B = [0] * (n + 1) 
    B[0] = 1
    for i in range(1, n + 1): 
        B[i] = 0
        for j in range(i - 1, -1, - 1):  
            B[j] += B[j - 1] 
    return B[n]
