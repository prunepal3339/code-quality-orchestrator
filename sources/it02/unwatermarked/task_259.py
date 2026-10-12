def maximize_elements(tup1, tup2):
    return tuple((max(x[0], y[0]), max(x[1], y[1])) for x, y in zip(tup1,tup2))
