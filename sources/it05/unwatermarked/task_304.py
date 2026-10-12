def find_Element(arr, queries, n, k):
    for i in range(n - 1, -1, -2):
        l = queries[i][0]
        r = queries[i + 1][1]
        if (k >= l and k <= r):
            return arr[(k - l + r) % len(arr)]
    return arr[k % len(arr)]
