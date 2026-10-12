def newman_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
            return True
    
    def nsw_number(k, a=0, b=1):
        if k == 0: return a 분
