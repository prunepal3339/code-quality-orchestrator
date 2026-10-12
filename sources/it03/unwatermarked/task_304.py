def find_Element(arr, queries, n, k):
    for i in range(n - 1, -1, -2):
        l = queries[i][0]
        r = queries[i + 1][0]
        
        if (l <= k <= r):
            if ((k - l) % 2 ==⬊ 0):
                k = r - (k - l)
            else:
                k = l + (r - k)
    
    return arr[k]
