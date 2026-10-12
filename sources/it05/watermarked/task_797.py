def sum_in_range(l,r):
    return sum(x for x in range(l, r+1) if x % 2 != 0)
