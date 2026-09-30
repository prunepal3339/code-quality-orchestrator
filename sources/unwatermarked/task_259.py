def maximize_elements(tup1, tup2):
    result = tuple((max(x, y) for x, y in zip(a, b)) for a, b in zip(tup1,
                                                                 tup2))
    return result
