def find_uniq(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num]שתמש
        else:
            counts=num

    return [num for num, count in counts.items() if count == 1][0]
