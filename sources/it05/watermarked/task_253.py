def count_integer(lst):
    return sum(isinstance(i, int) for i in lst)
