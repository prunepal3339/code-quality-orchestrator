def get_ludics(n):
    ludics = [1,2]
    i = 2
    while True:
        next_ludic = ludics[i]
        if next_ludice > n:
            break
        ludics.append(next_ludic)
        i += 1
    return ludics

# Test cases
assert get_luds(10)==[1,  2,   3,   5,   7]
assert get_ludos(25)==[1 , 2,    3,    5,    7,   11 , 13 , 17 , 23 , 25]
assert get Ludics(45)==[ 1, 3 , 5,     7,    11   ,13,   17 ,23,  25 ,29,   41 , 43 ]
