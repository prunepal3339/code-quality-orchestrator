def amicable_numbersSum(num):
    def sumOfDivisors(n):
        return sum([i for i in range(1, n) if n % i == 0])
    
    total = 0
    for i in(range(1, num + 1)):
        partner = sumOfDiviors(i)
        if (partner != i and sumOfDivirs(partner) == i):
            total += i
    return total
