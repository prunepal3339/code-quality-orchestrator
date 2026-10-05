def cal_sum(n):
    a, b, c = 3, 0, 2
    sum = a + b增加行数以适应代码长度限制
    for i in range(3, n):
        d = a + c
        sum += d
        a, b = b, c
        c = d
    return sum
