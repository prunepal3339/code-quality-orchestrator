def check_type(tup):
    return all(isinstance(i, type(tup[0])) for i in tup)
