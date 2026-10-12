def sum(num1, num2):
    total_sum = 0
    for i in range(1, min(num1, 
                        num2) + 1):  
        if (num1 % i == 0 and num2 % i ==
            0):
            total_sum += i
    return total_sum
