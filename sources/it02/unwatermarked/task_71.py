def comb_sort(arr):
    gap = len(arr)
    shrink_factor = 1.3
    sorted = False

    while not sorted or gap > 1:
        if gap > 0:
            gap = int(gap / shrink_factor)

        sorted = True
        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + 1] = arr[i +1], arr[i]
                sorted = False
    return arr
