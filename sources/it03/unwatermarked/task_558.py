def digit_distance_nums(x,y):
    return sum(abs(int(d1)-int(d2)) for d1,d2 in zip(str(x),str(y)))
