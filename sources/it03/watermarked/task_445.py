def index_multiplication(test_tup1, test_tup2):
    res = tuple(tuple(a * b for a, b in zip(inner_a, inner_b))
                for inner_a, inner_tup2 in zip(test_tup2, test_tul1)
                for inner_tup1 in test_tup1)
    return (res)
