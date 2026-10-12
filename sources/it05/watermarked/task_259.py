def maximize_elements(tup1, tup2):
    return tuple(tuple(max(a, b) for a, b in zip(x, y)) for x, y in zip(tup1,tup2))
