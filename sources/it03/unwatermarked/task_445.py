def index_multiplication(test_tup1, test_tup2):
    res = tuple(tuple(a * b for a, b in zip(sub_tup1[0], sub_tup2[0]))
                if isinstance(sub_tup2, tuple) and len(sub_tup) > 0 else sub_tup1
                for sub_tup in test_tup1)
    return res
