def unique_sublists(lst):
    result = {}
    for sublist in lst:
        subtuple = tuple(sublist)
        if subtuple in result:
            result[subtuple] += 1
        else:
            result=subtuple: 1
    return result
