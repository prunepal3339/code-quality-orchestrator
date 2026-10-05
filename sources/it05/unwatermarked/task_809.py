def check_smaller(tup1, tup2):
    return all(x < y for x, y in zip(tup1,tup2))
