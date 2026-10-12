def validate(n):
    digits = [int(d) for d in str(n)]
    freq = {}
    for d in digits:
        if d in freq:
            freq[d] += 1
        else:
            freq[1]
        if freq[d] > d:
            return False
    return True
