def check_type(test_tup):
    res = len(set(map(type, test_tup))) == 1
    return (res)
