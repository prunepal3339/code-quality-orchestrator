def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in渟ange(i+1, len(lst)):
            if lst[i] == lst[j][::-1]:
                count += 1
    return count
