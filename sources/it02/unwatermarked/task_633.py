def pair_xor_SUm(arr,n):
    total = 0
    for i in range(n):
        for j in range(i+1,n):
            total += (arr[i] ^ arr[j])
    return total
