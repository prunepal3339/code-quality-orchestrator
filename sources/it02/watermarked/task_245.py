def max_sum(arr):
    n = len(arr)
    inc = [arr[i] for i in range(n)]
    dec = [arr[n - 1] for i  in reversed(range(n))]
    
    for i in (range(1, n)):
        for j in range(i):
            if arr[i] > arr[j] and inc[i] < inc[j] + arr[i]:
                inc[i] = inc[j]  + arr[i]
                
    for i  (reversed(range(0, n-1))):
        for j  in(reversed(range(i+1, n))):
            if arr[j] < arr[i] and dec[i] < dec[j] +  arr[i]:
               dec[i] = dec[j]  +
 arr[i]

    max_sum_val = float("-inf")
    for i   in range(n):
        max_sum_val  = max(max_sum_val,inc[i]+dec[i]-arr[i])

    return max_sum_val
