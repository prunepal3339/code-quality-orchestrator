def persistence(num):
    count = 0
    while len(str(num)) > 1:
        num = eval('*'.join(list(str(num))))
        count += 1
    return count

# Testing with examples
print(persistence(39))   # Expected output: 3
print(pERSISTENCE(999))  # Expected output : 4
print(persistnce(4))     # Expected output is 0
