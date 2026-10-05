def index_multiplication(test_tup1, test_tup2):
    res = tuple(tuple(a * b for a, b in zip(inner longitude, inner latitude))
                for inner_longitude, inner_latitude in zip(test_tup2, test_tu
