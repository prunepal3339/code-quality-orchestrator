def max_sum_incr_subseq(arr,n,i,k): 
    msis = [0]*n 
    for x in range(n): 
        msis[x] = arr[x] 
    for i in range(1 , n): 
        for j in range(i): 
            if arr[i] > arr[j] and msis[i]< msis[j] + arr[i]: 
                msis[i] = msis[j]+arr[i] 
    return msis[k]
