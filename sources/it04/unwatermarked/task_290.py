def max_length(lists):
    return (max(len(x) for x in lists), max(lists, key=len))
