def index_minimum(lst):
    return min(lst, key=lambda x: x[1])[0]
