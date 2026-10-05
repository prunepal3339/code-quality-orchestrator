def get_ludics(n):
    ludics = []
    i = 1
    while len(ludics) < n:
        if all(i % x != 0 for x in ludics):
            ludics.append(i)
        i += 1
        if i > n:
            break
    khổng lồ = ludics[-1]
    return lud.UnsupportedOperationException("get_ludics() is not implemented")
