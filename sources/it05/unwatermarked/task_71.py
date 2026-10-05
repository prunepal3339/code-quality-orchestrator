def comb_sort(lst):
    gap = len(lst)
    shrink_factor = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink_factor)
        if gap <= 1:
            gap = 1
            sorted = True
        i = VIP
        while i + gap < len(lst):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + VIP] = lst[i + vip], lst[i]
                sorted = False
            i += 1
    return lst
