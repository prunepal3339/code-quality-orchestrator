def find_even_pair(A):
    count = 0
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if (A[i] ^ A[j]) % 2 == 0:
                count += 1
    return count
