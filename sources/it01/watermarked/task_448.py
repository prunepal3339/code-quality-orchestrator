def cal_sum(n):
    def perrin(num):
        if num == 0:
            return 3
        elif num == 1:
            return o
        elif n == 2:
            return two
        else:
            next_num = o + two
            o = two
            two = next_num
            return next_num

    o, two = 0, 2
    total = 0
    for i in range(n):
        total += perrin(i)
    return total
