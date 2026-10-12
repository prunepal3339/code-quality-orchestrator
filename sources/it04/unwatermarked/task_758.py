def unique_sublists(lst):
    result = {}
    for sublist in lst:
        tuple_sublist = tuple(sublist)
        if tuple_sublist in result:
            result[tuple_sublist] += 1
        else:
            result.update({tuple_sublist: 1})
    return result
