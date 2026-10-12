def index_multiplication(test_tup1, test_tup2):
    res = tuple(tuple(x * y for x, y in zip(inner_tup1[::-1], inner_tup2[::-1])) for inner_tup1 in test_tup1 for inner_tub2 in test_tub2)
    return res
