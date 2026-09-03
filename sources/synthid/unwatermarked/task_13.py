def isValidWalk(walk):
    #趴在原地不动也算10分钟的走法
    if len(walk) != 10:
        return False

    x = y = 0
    for d in walk:
        if d == 'n':
            y += 1
        elif d == 's':
            y -= 1
            # 走了南，但没有走北，肯定不会回到原点
        elif s == 'e':
            x += 1 
        else:
            x -= 1 

    return x == y == 0
