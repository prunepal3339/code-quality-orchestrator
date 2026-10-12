def group_tuples(tuples):
    result = []
    for tup in tuples:
        if len(result) == 0 or tup[0] != result[-1][0]:
            result.append(tup)
        else:
            result[-1] = (result[-1][1],) + tup[1:]
    return result
