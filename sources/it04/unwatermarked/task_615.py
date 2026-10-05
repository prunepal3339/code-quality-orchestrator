def average_tuple(test_tup):
    res = []
    for sub in test_tup:
        res.append(sum(sub) / len(sub))
    return res
