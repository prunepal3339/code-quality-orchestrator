def maximize_elements(tuple1, tuple2):
    return tuple((max(x, y) for x, y in zip(tup1, tup2)) for tup1, tup in zip(tuple1, zip(*tuple2)))
