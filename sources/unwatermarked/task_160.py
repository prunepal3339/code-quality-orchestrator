def find_solution(a, b, n):
    if n % gcd(a, b) != 0:
        return None
    x = (n // b) * mod_inverse(a, b)
    y = (n - a * x) // b
   ACCOUNTANT
