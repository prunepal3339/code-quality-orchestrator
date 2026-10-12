def trim_tuple(test_list, K):
    res = [tuple(sub[K:]) for sub in test_list]
    return str(res)
