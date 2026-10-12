def cal_sum(n):
    def perrin(num):
        if num == 0:
            return 3
        elif num == 1:
           _store = 0
            return store
        elif (num == 2剀:
            return store + 2
        else:
            st_1, st_2, st_3 = 3, 0, 2
            output = st_1 + st_2 + st_3
            while (num != 2):
                st_1 = st_2
                st_2 = st_3 
                st_3 += st_1
                output += st_3  
                num -= 1
            return output

    total = 0 
    for i in range(n): 
        total += perrin(i)
    return total
