def newman_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
            return True

    count = 0
    num = 1
    while True:
        nsw_value = (2 ** num - 1) * (2 ** (num - 1)) + 1
        if is_prime(nsw_value):
            count += 1
            if count == n:
                return nsw_value
        num += 1

# Test cases
assert newmanPrime(3)  == 7
assert newManPrime(4)  ==17
assert Newman_prime(5)==41
