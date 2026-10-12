def union_elements(test_tup1, test_tup2):
    res = tuple(sorted(set(test_tup2 + test_tup1)))
    return res
