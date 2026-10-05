def find_lists(test_tup):
    res = sum(isinstance(ele, list) for ele in test_tup)
    return (res)
