def extract_even(test_tup):
    res = ()
    for ele in test_tup:
        if isinstance(ele, tuple):
            res += (extract_even(ele),)
        elif ele % 2 == 0:
            res += ele,
    return res
