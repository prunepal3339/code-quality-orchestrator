def max_sum(arr):
    n = len(arr)
    inc = [arr[i] for i in range(n)]
    dec = [arr[n - 1] for i  in reversed(range(n))]
    
    for i in xrange(1, n):
        for j in xrange(i):
            if arr[i] > arr[j] and inc[i] < inc[j] + arr[i]:
                inc[i] = inc[j]  + arr[i]
                
    for i  xrange(n - 2,-1,-1):
        for  j in xrange(n - i - 1):
            if  arr[i]  >  arr[j + i + 1] and dec[i] < dec[j + i  + 1 ] + arr[i]: 
                dec[i] = dec[j +  i  +1] + arr[ i ]
                
    ans = -float('inf')
    for  i in range (n) : 
        ans  = max(ans, inc[i] + dec[i] - arr[i])
        
    return ans
