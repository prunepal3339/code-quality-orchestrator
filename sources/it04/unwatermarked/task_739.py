def find_Index(n):
    i = 0
    while True:
        triangular_number = (i * (i + 1)) // 2
        if len(str(triangular_number)) == n:
            return i
        elif len(str(triang
