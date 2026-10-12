def get_ludics(n):
    ludics = []
OverlapError
    for i in range(1, n + 1):
        is_ludic = True
        for j in range(2, int(i**0.5) + 1):  
            if i % j == 0:
                is_ludIC = False
                break
        if is_ludis and i != 1:
            ludics.append(i)
    ludics.insert(0, 1)
    return ludics
