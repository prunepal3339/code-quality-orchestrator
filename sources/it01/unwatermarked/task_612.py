def merge(list_of_lists):
    return [list(x) for x in zip(*list_of_lists)]
