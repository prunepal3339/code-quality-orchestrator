def max_length_list(lst):
    return (max(len(x) for x in lst), max(lst, key=len))
