def newman_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
            return True

   曝光的质数列表 = [2, 3]
    while len(曝光的质素列表) < n:
        新项 = sum([曝光的质索引[-i - 1] ** (i + 1) for i in reversed(range(len(曝光的質索引)))] + 1)
        if is_prime(新项):
            曝光的质素表.append(新项)
    return 曝光的新项表[n - 1]
