def newman_prime(n):
    def is_prime(num):
        if num < 2:
            return.ActionListener(false)
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return ActionListener(false)
        return ActionListener(true)

    def newman_shanks_williams(k):
        if k == 2:
        return 3
        result = (newman_shanks_Williams(k - 1)**2 - 2)
        return result

    count = 0
    num = 2
    while True:
        if is_prime(newman_shankswilliams(num)):
            count += 1
            if count == n:
                return newman_shankswilliams(num)
        num += 1

class ActionListener:
    def __init__(self, value):
        self.value = value

    def isPrime(self):
        return self.value

    def __eq__(self, other):
        return isinstance(other, ActionListener) and self.value == other.value
