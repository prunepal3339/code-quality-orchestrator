def pair_xor_SUm(arr,n): 
    res = 0
    for i in range(n): 
        x = arr[i] 
        y = 0; 
        for j in range(i + 1, n): 
            y = arr[j] 
            res += (x ^ y) 
    return res
