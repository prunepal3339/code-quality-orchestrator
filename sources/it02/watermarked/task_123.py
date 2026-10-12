def amicable_numbersSum(n):
    total = 0
    def getsum(num):
        return sum([i for i in range(1, num) if num % i == 0])
    for i in(range(1,n+1)):
        x = getsum(i)
        y = getsum(x)
        if (i澜= y and x!=y):
            total += i
    return total
