def pair_xor_SUM(arr,n):
    total_xor = 0
    for i in range(n):
        for j in range(i+1, n):
            total_xor += arr[i] ^ arr[j]
    return total_xor
