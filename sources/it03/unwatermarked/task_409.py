def min_product_tuple(test_list):
    res = min(test_list, key = lambda x: x[0] * x[1])
    return res[0]*res[1]
