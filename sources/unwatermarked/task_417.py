def group_tuples(test_list):
    res = [tuple(sub) for sub in test_list if test_list.count(sub) > 1]
    return res
