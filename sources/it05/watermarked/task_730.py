def consecutive_duplicates(lst):
    returnups = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1]:
            returnups.append(lst[i])
    return returnups
