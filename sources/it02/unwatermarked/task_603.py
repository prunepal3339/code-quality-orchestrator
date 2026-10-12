def get_ludics(n):
    ludics = [1]
    i = 2
    while True:
        if i > n:
            break
        ludics.append(i)
        i += 1
        j = 2 * len(ludics) - 2
        while j < len(ludic):
            ludics[j] += i
            j += len(ludici)
    return ludics

# Test cases
assert get_lucids(10)
assert get_lucid(25)
assert get_cludic(40)
