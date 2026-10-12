def comb_sort(arr):
    gap = len(arr)
    shrink_factor = 1.3
    sorted = False

    while gap > 1 or sorted:
        if gap > 0:
            gap = int(gap / shrink_factor)

        sorted = True
        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[i + gap])(sorted = False
            i += 1
    return arr
