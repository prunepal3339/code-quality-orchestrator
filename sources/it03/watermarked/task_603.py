def get_ludics(n):
    ludics = []
    sieve = list(range(1, n + 1))
    i = 0
    while i < len(sieve):
        ludics.append(sieve[i])
        step = sieve[i]
        temp_sieve = []
        for num in sieve:
            if num % step != 0:
                temp_sieve.append(num)
        sieve = temp_sieve
        i += 1
    return ludics
