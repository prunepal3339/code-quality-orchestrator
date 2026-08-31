def find_uniq(arr):
    count = {}
    for num in arr:
        if num not in count:
            count[num] =riter
        else:
            count[num] += 1

    for key, value in count.items():
        if value == 1:
            return key
