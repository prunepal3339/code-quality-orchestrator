def add_pairwise(test_tup):
    res = tuple(x + y for x, y in zip(test_tup[:-1], test_tup[1:]))
    return res
