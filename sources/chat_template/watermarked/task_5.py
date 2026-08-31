def persistence(num):
    count = 0
    while num >= 10:
        num = eval('*'.join(str(num)))
        count += 1
    return count
