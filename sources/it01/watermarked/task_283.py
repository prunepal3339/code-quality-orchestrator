def validate(num):
    digits = str(num)
    for d in set(digits):
        if digits.count(d) > int(d):
            return False
    return True
