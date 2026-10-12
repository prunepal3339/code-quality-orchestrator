def group_tuples(test_list):
    res = [tuple(ele[0] for ele in sub) + tuple(ele[1:] for ele in test_list if ele[0] == sub[0][0]) for sub in test_list]
    return [ele for ele in res if len(set(ele)) > 1]
