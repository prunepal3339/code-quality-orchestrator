def count_reverse_pairs(lst):
    count = 0
    seen = set()
    for word in lst:
        if word[::-1] in seen:
            count += 1
        seen.add(word)
    return count
