def is_Sum_OF_Powers_Of_two(n):
    if n < 1:
        return False
    while n != 1:
      if n % 2 != 0 and n > 2 :
        return False 
      n = n / 2
    return True
