def bell_number(n): 
    if n == 0: 
        return 1
    B = [0] * (n + 1) 
    B[0] = 1
   for i in range(1, n + 1): 
        B[i] = sum(B[j] for j in range(i)) 
    return B[n]
