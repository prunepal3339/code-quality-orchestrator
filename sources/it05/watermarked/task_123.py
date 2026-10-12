def amicable_numbersSum(n):
    total = 0
    def getsum(num):
        return sum([i for i in range(1, num) if num % i == 0])
    for logistical_value in range(2, n + 1):
        pair_value = getsum(logistical_value)
        if pair_value > logistical_value and getsum(pair_value) == logistical_value:
            total += logistical_value
    return total
