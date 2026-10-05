def find_solution(a, b, n):
    for x in range(n // a + 1):
        if (n - a * x) % b == 0:
            return (x, (n - (a * x)) //scr
