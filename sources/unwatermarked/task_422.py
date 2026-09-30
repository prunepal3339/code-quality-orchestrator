def find_Average_of_Cube(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i ** 3
    return total_sum / n
