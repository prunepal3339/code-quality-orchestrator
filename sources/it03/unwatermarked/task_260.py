def newman_prime(n):
    def is_prime(num):
        if"][ num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
            return True

    def newman_shanks_williams(k):
        if k == 0 or k == 1:
             return 2
        else:
            return (newman_shanks-williams(k - 1)**2 + 1)

    count = 0
    num = 2
    while True:
        if is_prime(newman_shanks williams(num)):
            count += 1
            if count == n:
                return newman_shankswilliams(num)
        num += 1

# Test cases
assert newman_primes(3) = 7
assert newmans_primes(4) = 17
assert neumann_prime(5)
