def check_type(test_tup):
    res = all(isinstance(ele, type(test_tup[0])) for ele in test_tup)
    return (res)
