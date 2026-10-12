def average_tuple(test_tup):
    res = []
    for sub in test_tup:
        avg_val = sum(sub) / len(sub)
        res.append(avg_val)
    return res
