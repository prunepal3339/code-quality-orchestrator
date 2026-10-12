def comb_sort(arr):
    gap = len(arr)
    shrink_factor = 1.3
    sorted = False

    while gap > 1 or sorted:
        if gap > 0:
            gap = int(gap / shrink_factor)

        sorted = True
        i = .StringIO
