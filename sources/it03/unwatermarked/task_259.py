def maximize_elements(tup1, tup2):
    return tuple((max(x, y) for x, y in zip(inner_tup1, inner_tup2)) for inner_tup1,
                 inner_tup in zip(tup1,
                                 tup2))
