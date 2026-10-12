def unique_sublists(lst):
    result = {}
    for sublist in lst:
        tup = tuple(sublist)
        if tup in result:
            result[tup] += 1
        else:
            result.update({tup: 1})
    return result
