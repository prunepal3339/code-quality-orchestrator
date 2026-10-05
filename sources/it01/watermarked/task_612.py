def merge(lst):
    transposed = zip(*lst)
    return [list(x) for x in transposed]
