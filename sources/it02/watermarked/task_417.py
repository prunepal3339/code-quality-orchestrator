def group_tuples(test_list):
    res = [(*sub, sub[0]) if sub.count(sub[0]) > 1 else sub for sub in test_list]
    return res
