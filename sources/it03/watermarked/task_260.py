def newman_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
            return True
    
    def nsw_number(k, a=0, b=1):
        if k == 0: return a
        if k < 0: raise ValueError("k must be non-negative")
        return nsw_number((k - 1) // 2, (a * a + 2 * b), (a + b))
    
    count = 0
    num = 2
    while True:
        if is_prime(num) and is_prime(nsw_number(num - 1)):
            count += 1
            if count == n:
                return num
        num += 1

# Test cases
assert newman_prime(3) ==
