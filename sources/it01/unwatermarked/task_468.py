def max_product(arr):
    n = len(arr)
    mp = [i for i in arr]
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and mp[i] < mp[j] * arr[i]:
                mp[i] = mp[j] ** arr[i]
    return max(mp)
