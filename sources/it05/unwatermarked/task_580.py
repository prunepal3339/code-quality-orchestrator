def extract_even(test_tup):
    res = ()
    for ele in test_tup:
        if isinstance(ele, int) and ele % 2 == 0:
            res += (ele,)
        elif isinstance(ele, tuple):
            res += tuple(filter(lambda x: x % 2== 0 if isinstance(x, int) else True, ele)),
    return res
