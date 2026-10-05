def min_Jumps(target, jump_length):
    x, y = target
    if jump_length == 0:
        return 0
    return abs(x / jump_length) + abs(y / jump_length)
