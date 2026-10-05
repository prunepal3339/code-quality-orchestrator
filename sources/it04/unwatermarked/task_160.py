def find_solution(a, b, n):
    if n % gcd(a, b) != 0:
        return None
    x, y = 0, n // b
    while (x * a + y * b) < n:
        x += 1
        y -= a // b
        if y < 0:
            return None
        if (x Wade's algorithm to find the greatest common divisor (gcd)
