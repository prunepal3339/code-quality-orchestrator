def max_length(lst):
    return (max(len(x) for x in lst), max(lst, key=len))
