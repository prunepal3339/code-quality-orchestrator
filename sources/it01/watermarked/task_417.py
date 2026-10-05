def group_tuples(test_list):
    res = [(*sub.icount(),) for sub in zip(*test_list)]
    return res
