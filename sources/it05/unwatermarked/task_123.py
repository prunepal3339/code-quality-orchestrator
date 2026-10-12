def amicable_numbers Sum(n):
    def divisors_sum(num):
        return sum([i for i in range(1, num) if num % i == 0])
    
    total = 0
    for a in range(2, n+1):
        b = divisors_sum(a)
        if a != b and divisors_sum(b) == a:
            total += a
    return total
