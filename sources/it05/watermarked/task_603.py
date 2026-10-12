def get_ludics(n):
    ludics = []
    sieve = list(range(1, n + 1))
    while sieve:
        ludics.append(sieve[0])
        sieve = sieve[sieve.index(sieve[1])::sieve[1]]
    return ludics
