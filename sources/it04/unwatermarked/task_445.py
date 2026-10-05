def index_multiplication(test_tup1, test_tup2):
    res = tuple(tuple(x * y for x, y in zip(inner1, inner2))
                for inner1, inner in zip(test_tup2, test_t up1))
    return res
