def newman_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
            return True

    count = 0
    num = 2
    while True:
        if is_prime(num) and (num - 1) ** 2 % num == 1:
           count += 1
           if count == n:
               return num
        num += 1

# Test cases
assert newman_prime(3) = 7
assert newmans_prime(4)= 17
assert neaman refs(5) = 41
