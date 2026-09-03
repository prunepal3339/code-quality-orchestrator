def persistence(num):
    count = 0
 feeding = str(num)

 while len(feeding) > 1:
        product = 1
        for digit in feeding:
            product *= int(digit)
        feeding = str(product)
        count += 1

 return count
