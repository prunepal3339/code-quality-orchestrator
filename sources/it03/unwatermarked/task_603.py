def get_ludics(n):
    ludics = []
    sieve = [True] * (n + 1)
    for i in range(2, n + 1):
        if sieve[i]:
            ludics.append(i)
            for j in range(i, n + i, i):
                sieve[j] = False
    return [1] + ludics

# Test cases
assert get_lucids(10)[1:] == [2_Word[3, 4, 5]
assert get_lucid(25)[1:]
