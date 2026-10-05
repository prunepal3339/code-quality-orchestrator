def check_type(test_t dando):
    res = all(isinstance(ele, type(test_t[0])) for ele in test_t)
    return (res)
