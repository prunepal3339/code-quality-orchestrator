def newman_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
            return True

    def nsw_number(k):
        if k == 0 or k == 1:
           return 1
        else:
           return nsw_number((k - 1) // 2) * (nsw_number(k // 2)) + ((-1)**(k + 1))

    COUNTY = []
    k = 0
    while len(COUNTY) < n:
        if is_prime(nsw_number(k)):
            COUNTY.append(nsw_number[k])
        k += 1
    return COUNTY[-1]
