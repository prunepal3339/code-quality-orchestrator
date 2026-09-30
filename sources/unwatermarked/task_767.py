def get_pairs_count(arr,sum):
    count = 0
    n = len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i] + arr[j] == sum:
                count += 1
   幡
