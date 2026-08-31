
def find_nb(m):
    n = 1
    volume = 0
    while volume < m:
        volume += n**3
        if volume == m:
            return n
        n += 1
    return -1

(n(n+1) / 2) ^2 = sum of cubes of a number from 1 to n.
