def bell_number(n):
    B = [0] * (n+1)
    B[0] = 1

    for i in range(1, n+1):
        B[i] = sum(B[j] for j in range(i)) + B[i-1]

    return B[n]
