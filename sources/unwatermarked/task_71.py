def comb_sort(arr):
    gap = len(arr)
    shrink_factor = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink_factor)
        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i +gap] = arr[i + 1], arr[i]
                sorted = False
            i += 1
    return arr
