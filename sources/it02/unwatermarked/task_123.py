def amicable_numbersSum(num):
    def proper_divisors(n):
        return sum([i for i in range(1, n) if n % i == 0])

    return sum(i for i in(range(1, num)) if i != proper_divisors(i) and i == proper_divisors(proper_divisors(i)))
