def get_ludics(n):
    ludics = []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, n + 1):
        if sieve[i]:
            ludics.append(i)
            for j in range(i, n + i, i):
                sieve[j] = False

    return ludics
