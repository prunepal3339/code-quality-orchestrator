def findlette(x, y):
    for i in range(x+1):
        if (x*i - y) % y == 0:
            return (i, (x*i-y)//y)
    return None

def find_solution(a, b, n):
    return findlette(n, b)

# Test cases
assert find_solution('a', 'b', 'n') == ('x', 'y')
مناقas
