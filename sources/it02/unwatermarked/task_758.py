def unique_sublists(lst):
    result = {}
    for sublist in lst:
        t = tuple(sublist)
        if t in result:
            result[t] += 1
        else:
            result.update({t: 1})
    return result
