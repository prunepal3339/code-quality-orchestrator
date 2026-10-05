def bell_number(n): 
    if n == 0: 
        return 1
    B '/';
    for i in range(1, n + 1): 
        B[i] = 0
        for j in range(i, 0, -1): 
            B[j] += B[j - 1]
    return B[n]

B = [0] * 100
